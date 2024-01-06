import shutil
from collections import defaultdict
from functools import reduce
from importlib import import_module
from typing import Optional

import pandas as pd
import pyarrow as pa
import pyarrow.compute as pac
from cytoolz import keyfilter
from more_itertools import chunked
from pyarrow import parquet
from pathlib import Path

import pdr_tests

MANIFEST_DIR = Path(pdr_tests.__file__).parent / "node_manifests"


# defining these separately from the 'special' label search
IRRELEVANT_EXTENSIONS = (
    "backup",
    "bak",
    "btupd",
    "cat",
    "cmdlog",
    "gif",
    "htm",
    "html",
    "jpg",
    "log",
    "pdf",
    "png",
    "temp",
    "tmp",
    "txt",
)
LABEL_EXTENSIONS = ("fmt", "lbl", "xml")
IGNORE_DIRECTORIES = (
    "calib", "geometry", "document", "index", "catalog", "browse", "extras"
)


def add_coverage_column(fn):
    if not (path := Path(fn)).exists():
        path = MANIFEST_DIR / fn
    if not path.exists():
        raise FileNotFoundError(f"No manifest found with name/path {fn}")
    rules_modules = load_all_rules()
    relevant_rules = find_relevant_rules(rules_modules, path)
    check_coverage_in_chunks(
        path,
        relevant_rules,
        row_group_size=100000,
        use_dictionary=[
            "domain",
            "url",
            "volume",
            "dataset_pds3",
            "dataset_ix",
            "ptype",
        ],
    )


def load_all_rules():
    """
    loads rules for each product type in each dataset submodule of the
    pdr_tests.definitions module.
    """
    definitions_dir = Path(Path(pdr_tests.__file__).parent, "definitions")
    rules_modules = {}
    for entry in definitions_dir.iterdir():
        if entry.is_dir():
            try:
                selection_rules = import_module(
                    f"pdr_tests.definitions.{entry.name}.selection_rules"
                )
            except ModuleNotFoundError:
                continue
            rules_modules[entry.name] = getattr(
                selection_rules, "file_information"
            )
    return rules_modules


def find_relevant_rules(rules_modules, input_manifest):
    """select definition modules that use the specified manifest."""
    relevant_rules = {}
    for key in rules_modules.keys():
        for subkey in rules_modules[key].keys():
            if (
                Path(rules_modules[key][subkey]["manifest"]).name
                == input_manifest.name
            ):
                relevant_rules[(key, subkey)] = rules_modules[key][subkey]
    return relevant_rules


def check_coverage_in_chunks(
    input_file: Path,
    relevant_rules,
    row_group_size=None,
    use_dictionary=None,
    version="2.6",
    n_chunks=5,
):
    scratch_file = (
        input_file.parent / (input_file.stem + "_temp.parquet")
    )
    write_kwargs, open_kwargs = {}, {}
    if row_group_size is not None:
        write_kwargs["row_group_size"] = row_group_size
    if use_dictionary is not None:
        open_kwargs["use_dictionary"] = use_dictionary
    sort_reader = parquet.ParquetFile(input_file)
    schema = sort_reader.read_row_group(0).schema
    schemadict = {
        name: type_ for name, type_ in zip(schema.names, schema.types)
    } | {"dataset_ix": pa.string(), "ptype": pa.string()}
    sort_writer = parquet.ParquetWriter(
        scratch_file,
        version=version,
        schema=pa.schema(schemadict, schema.metadata),
        **open_kwargs,
    )
    try:
        ix_chunks = tuple(
            chunked(range(sort_reader.metadata.num_row_groups), n_chunks)
        )
        for i, ix_chunk in enumerate(ix_chunks):
            print(f"{i + 1}/{len(ix_chunks)}")
            chunk = sort_reader.read_row_groups(ix_chunk)
            sort_writer.write_table(
                add_rule_labels(relevant_rules, chunk), **write_kwargs
            )
            del chunk
    finally:
        sort_writer.close()
    shutil.move(
        scratch_file,
        MANIFEST_DIR
        / (input_file.stem.replace("_coverage", "") + "_coverage.parquet")
    )


def add_rule_labels(relevant_rules, table: pa.Table) -> pa.Table:
    """
    make a list of boolean masks for each rule in relevant_rules. the masks
    denote whether each row in 'table' meet the individual criteria of the
    rule. Then take the logical intersection of the masks, creating a mask that
    true if a given row meets all of a rule's criteria. Add columns to the
    input table indicating which rule(s) (if any) match each row.
    """
    rows = table.num_rows
    dataset_labels, ptype_labels = [""] * rows, [""] * rows
    for dataset, ptype in relevant_rules.keys():
        rule = relevant_rules[(dataset, ptype)]
        masks = []
        if "url_must_contain" in rule.keys():
            for string in rule["url_must_contain"]:
                masks.append(pac.match_substring(table["url"], string))
        if "url_regex" in rule.keys():
            for string in rule["url_regex"]:
                masks.append(pac.match_substring_regex(table["url"], string))
        if "fn_ends_with" in rule.keys():
            ends = rule["fn_ends_with"]
            assert len(ends) == 1, "only one filename ending may be specified"
            masks.append(pac.ends_with(table["filename"], pattern=ends[0]))
        if "fn_must_contain" in rule.keys():
            for string in rule["fn_must_contain"]:
                masks.append(pac.match_substring(table["filename"], string))
        if "fn_regex" in rule.keys():
            for string in rule["fn_regex"]:
                masks.append(
                    pac.match_substring_regex(table["filename"], string)
                )
        combined_mask = reduce(pac.and_, masks)
        for index, match in enumerate(combined_mask):
            if not match.as_py():
                continue
            for array, field in zip(
                (dataset_labels, ptype_labels), (dataset, ptype)
            ):
                if array[index] != "":
                    array[index] += f",{field}"
                else:
                    array[index] = field
    for array, name in zip(
        (dataset_labels, ptype_labels), ("dataset_ix", "ptype")
    ):
        field, array = pa.field(name, pa.string()), pa.array(array)
        if name in table.column_names:
            table = table.set_column(
                table.column_names.index(name), field, array
            )
        else:
            table = table.append_column(field, array)
    return table


def pa_split(array, sep="/"):
    max_depth = pac.max(pac.count_substring(array, sep)).as_py()
    pattern = "".join([f"(?:(?P<{n}>[^/]+){sep})?" for n in range(max_depth)])
    extracted = pac.extract_regex(array, pattern)
    # noinspection PyTypeChecker
    return pa.Table.from_arrays(
        {n: pac.struct_field(extracted, [n]) for n in range(max_depth)},
        tuple(map(str, range(max_depth))),
    )


def pa_extract_constants(table, drop_constants=False):
    constant_names = [
        n for n in table.schema.names if pac.count_distinct(table[n]) == 1
    ]
    constants = {n: table[n][0].as_py() for n in constant_names}
    if drop_constants is True:
        return constants, table.drop(constant_names)
    return constants, table


def get_extensions(filenames: pa.Array):
    extensions = pac.extract_regex(filenames, r"\.(?P<extension>\w+)$")
    return pac.struct_field(extensions, [0])


def make_countframe(
    directories: Optional[pa.Array] = None,
    filenames: Optional[pa.Array] = None,
    parts: Optional[pa.Table] = None
):
    if (parts is None) and ((directories is None) or (filenames is None)):
        raise ValueError("directories + filenames, or parts, must be passed")
    if parts is None:
        parts = make_part_table(directories, filenames)
        parts = pa_extract_constants(parts, drop_constants=True)[1].to_pandas()
    else:
        parts = parts.to_pandas()
    count_df = parts.value_counts(dropna=False)
    counts = count_df.values
    count_df = count_df.index.to_frame().reset_index(drop=True)
    count_df["count"] = counts
    return count_df


def make_part_table(directories, filenames):
    parts = pa_split(directories, "/").append_column(
        "ext", get_extensions(filenames)
    )
    return parts


def count_coverage(
    manifest: pa.Table,
    ignore_labels=(),
    label_extensions=LABEL_EXTENSIONS,
    ignore_extensions=IRRELEVANT_EXTENSIONS,
    ignore_directories=IGNORE_DIRECTORIES,
):
    manifest = filter_ignored_labels(ignore_labels, manifest)
    if ignore_directories is not None:
        manifest, parts, ignored_parts = filter_ignored_directories(
            ignore_directories, manifest
        )
    else:
        parts, ignored_parts = None, None
    print(f"finding coverage")
    cov, ucov, preds = find_covered(
        manifest, label_extensions, ignore_extensions
    )
    print("making countframes")
    frames = {}
    for name, tab in zip(("cov", "ucov"), (cov, ucov)):
        if len(tab) == 0:
            continue
        if parts is None:
            frames[name] = make_countframe(tab['url'], tab['filename'])
        else:
            frames[name] = make_countframe(parts=parts.filter(preds[name]))
    if ignored_parts is not None:
        frames["dir_ignore"] = make_countframe(parts=ignored_parts)
    del parts, ignored_parts
    metrics = defaultdict(list)
    if len(cov) > 0:
        for field in ("dataset_ix", "ptype"):
            metrics[field] = get_ix_metrics(cov, field)
    for field in ("volume", "dataset_pds"):
        metrics[field] = get_pds_metrics(manifest, cov, ucov, field)
    return {k: pd.DataFrame(v) for k, v in metrics.items()} | frames


def filter_ignored_directories(ignore_directories, manifest):
    print("making part table for directory exclusion...", end="")
    parts = make_part_table(manifest["url"], manifest["filename"])
    original_length = len(manifest)
    igd_array = pa.array(ignore_directories)
    exclusions = pac.is_in(pac.ascii_lower(parts[0]), igd_array)
    for n in parts.schema.names:
        if n in (0, "ext"):
            continue
        exclusions = pac.or_(
            exclusions, pac.is_in(pac.ascii_lower(parts[n]), igd_array)
        )
    manifest = manifest.filter(pac.invert(exclusions))
    if len(manifest) < original_length:
        print(f"{original_length - len(manifest)} files excluded")
    else:
        print("excluded no files")
    return (
        manifest,
        parts.filter(pac.invert(exclusions)),
        parts.filter(exclusions)
    )


def filter_ignored_labels(ignore_labels, manifest):
    for label in ignore_labels:
        print(f"excluding label '{label}'...", end="")
        original_length = len(manifest)
        manifest = manifest.filter(
            pac.invert(pac.match_substring(manifest["label"], label))
        )
        if len(manifest) < original_length:
            print(f"{original_length - len(manifest)} files excluded")
        else:
            print("excluded no files")
    return manifest


def find_covered(
    manifest,
    ignore_extensions=IRRELEVANT_EXTENSIONS,
    label_extensions=LABEL_EXTENSIONS,
):
    preds = {"cov": pac.invert(pac.equal(manifest["dataset_ix"], ""))}
    if pac.sum(preds["cov"]).as_py() == 0:
        print("note: none of this manifest is covered.")
    extensions = get_extensions(manifest["filename"])
    preds["label"] = pac.is_in(
        pac.ascii_lower(extensions), pa.array(label_extensions)
    )
    if pac.any(pac.and_(preds["cov"], preds["label"])).as_py() is True:
        print("note: some labels are assigned as top-level covered.")
    preds["irrelevant"] = pac.is_in(
        pac.ascii_lower(extensions), pa.array(ignore_extensions)
    )
    preds["good"] = pac.invert(pac.or_(preds["irrelevant"], preds["label"]))
    preds["ucov"] = pac.and_(pac.invert(preds["cov"]), preds["good"])
    uncovered = manifest.filter(preds["ucov"])
    covered = manifest.filter(preds["cov"])
    return covered, uncovered, keyfilter(lambda k: k in ("cov", "ucov"), preds)


# noinspection PyDictCreation
def get_ix_metrics(covered, field):
    print(f"counting {field}")
    recs = []
    if field == "ptype":
        ref = pac.binary_join_element_wise(
            covered['dataset_ix'], covered['ptype'], ';'
        )
    elif field == "dataset_ix":
        ref = covered["dataset_ix"]
    else:
        raise ValueError(f"unknown field {field}")
    vals = pac.unique(ref).to_pylist()
    for val in filter(lambda v: v not in ("", ";"), vals):
        match = covered.filter(pac.equal(ref, val))
        rec = {field: val, "count": len(match)}
        if field == "dataset_ix":
            rec["ptypes"] = pac.unique(match["ptype"]).to_pylist()
        rec["volumes"] = pac.unique(match["volume"]).to_pylist()
        rec["datasets_pds"] = pac.unique(match["dataset_pds"]).to_pylist()
        rec["n_dataset"] = len(rec["datasets_pds"])
        rec["n_volume"] = len(rec["volumes"])
        rec["total_mb"] = pac.sum(match["size"]).as_py() / 1024 ** 2
        rec["mean_mb"] = rec["total_mb"] / rec["count"]
        rec["labels"] = pac.unique(match["label"]).to_pylist()
        recs.append(rec)
    return recs


def null_pds_metric(count):
    return {
        "datasets_ix": [],
        "ptypes": [],
        "n_datasets_ix": 0,
        "n_ptypes": 0,
        "n_covered": 0,
        "n_uncovered": count,
        "coverage": 0,
    }


def get_pds_metrics(manifest, covered, uncovered, field):
    print(f"counting {field}")
    recs = []
    vals = pac.unique(manifest[field]).to_pylist()
    for val in filter(lambda v: v != "", vals):
        match_pred = pac.equal(manifest[field], val)
        rec = {
            field: val,
            "count": pac.sum(match_pred).as_py(),
            "labels": pac.unique(
                manifest.filter(match_pred)["label"]
            ).to_pylist(),
        }
        del match_pred
        if len(covered) == 0:
            recs.append(rec | null_pds_metric(rec["count"]))
            continue
        match = covered.filter(pac.equal(covered[field], val))
        rec["datasets_ix"] = pac.unique(match["dataset_ix"]).to_pylist()
        rec["ptypes"] = pac.unique(match["ptype"]).to_pylist()
        rec["n_datasets_ix"] = len(rec["datasets_ix"])
        rec["n_ptypes"] = len(rec["ptypes"])
        rec["n_covered"] = len(match)
        ucmatch = uncovered.filter(pac.equal(uncovered[field], val))
        rec["n_uncovered"] = len(ucmatch)
        if (len(ucmatch) + len(match)) == 0:
            rec["coverage"] = float("nan")
        else:
            rec["coverage"] = rec["n_covered"] / (
                rec["n_covered"] + rec["n_uncovered"]
            )
        recs.append(rec)
    return recs


def load_and_count(
    manifest_path,
    ignore_labels=(),
    ignore_extensions=IRRELEVANT_EXTENSIONS,
    label_extensions=LABEL_EXTENSIONS,
    ignore_directories=IGNORE_DIRECTORIES,
    write=False,
):
    manifest_path = Path(manifest_path)
    if "coverage.parquet" not in manifest_path.name:
        raise ValueError("this does not appear to be a coverage manifest.")
    metrics = count_coverage(
        parquet.read_table(
            manifest_path,
            columns=[
                "url",
                "filename",
                "dataset_ix",
                "dataset_pds",
                "volume",
                "ptype",
                "size",
                "label",
            ],
        ),
        ignore_labels,
        label_extensions,
        ignore_extensions,
        ignore_directories
    )
    if (write is True) and (len(metrics) > 0):
        for k, v in metrics.items():
            outpath = Path(
                manifest_path.parent,
                manifest_path.name.replace("_coverage.parquet", f"_{k}.csv"),
            )
            v.to_csv(outpath, index=None)
    return metrics
