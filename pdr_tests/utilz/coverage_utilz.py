from collections import defaultdict
from functools import reduce
from importlib import import_module

import pyarrow as pa
import pyarrow.compute as pac
from more_itertools import chunked
from pyarrow import parquet
from pathlib import Path

import pdr_tests


def add_coverage_column(input_manifest):
    input_manifest = Path(
        Path(Path(pdr_tests.__file__).parent, "node_manifests"), input_manifest
    )
    rules_modules = load_all_rules()
    relevant_rules = find_relevant_rules(rules_modules, input_manifest)
    check_coverage_in_chunks(
        input_manifest,
        relevant_rules,
        row_group_size=100000,
        use_dictionary=[
            'domain', 'url', 'volume', 'dataset_pds3', 'dataset_ix', 'ptype'
        ]
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
                str(rules_modules[key][subkey]["manifest"]).split("/")[-1]
                == str(input_manifest).split("/")[-1]
            ):
                relevant_rules[(key, subkey)] = rules_modules[key][subkey]
    return relevant_rules


def check_coverage_in_chunks(
    input_file,
    relevant_rules,
    row_group_size=None,
    use_dictionary=None,
    version="2.6",
    n_chunks=20
):
    output_file = Path(
        str(input_file).split(".parquet")[0] + "_coverage.parquet"
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
        output_file,
        version=version,
        schema=pa.schema(schemadict, schema.metadata),
        **open_kwargs,
    )
    try:
        ix_chunks = tuple(
            chunked(range(sort_reader.metadata.num_row_groups), 5)
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
        table = table.append_column(
            pa.field(name, pa.string()), pa.array(array)
        )
    return table


def get_pa_extensions(filenames: pa.Array):
    extensions = pac.extract_regex(filenames, r'\.(?P<extension>\w+)$')
    return pac.struct_field(extensions, [0])


# defining these separately from the 'special' label search
IRRELEVANT_EXTENSIONS = [
    'backup', 'bak', 'btupd', 'cat', 'cmdlog', 'gif', 'htm', 'html', 'jpg',
    'log', 'pdf', 'png', 'temp', 'tmp', 'txt', 'asc'
]

LABEL_EXTENSIONS = ['fmt', 'lbl', 'xml']

# TODO, maybe: explicitly ignore some 'calib', 'geometry', etc. directories?


def pnot(val):
    return pac.invert(val)


def count_coverage(manifest: pa.Table):
    covered, uncovered = find_covered(manifest)
    if covered is None:
        return {}, []
    uncovered_extensions = pac.unique(
        get_pa_extensions(uncovered['filename'])
    ).to_pylist()
    metrics = defaultdict(list)
    for field in ("dataset_ix", "ptype"):
        metrics[field] = get_ix_metrics(covered, field)
    for field in ("volume", "dataset_pds"):
        metrics[field] = get_pds_metrics(manifest, covered, uncovered, field)
    return metrics, uncovered_extensions


def find_covered(manifest):
    preds = {'cover': pac.invert(pac.equal(manifest['dataset_ix'], ''))}
    if pac.sum(preds['cover']).as_py() == 0:
        print("none of this manifest is covered.")
        return None, None
    extensions = get_pa_extensions(manifest['filename'])
    preds['label'] = pac.is_in(
        pac.ascii_lower(extensions), pa.array(LABEL_EXTENSIONS)
    )
    if pac.any(pac.and_(preds['cover'], preds['label'])).as_py() is True:
        print("note: some labels are assigned as top-level covered.")
    preds['irrelevant'] = pac.is_in(
        pac.ascii_lower(extensions), pa.array(IRRELEVANT_EXTENSIONS)
    )
    preds['good'] = pac.invert(pac.or_(preds['irrelevant'], preds['label']))
    preds['uncover'] = pac.and_(pnot(preds['cover']), preds['good'])
    uncovered = manifest.filter(preds['uncover'])
    covered = manifest.filter(preds['cover'])
    return covered, uncovered


# noinspection PyDictCreation
def get_ix_metrics(covered, field):
    recs = []
    vals = pac.unique(covered[field]).to_pylist()
    for val in filter(lambda v: v != "", vals):
        match = covered.filter(pac.equal(covered[field], val))
        rec = {'value': val, 'count': len(match)}
        rec['volumes'] = pac.unique(match['volume']).to_pylist()
        rec['datasets_pds'] = pac.unique(match['dataset_pds']).to_pylist()
        rec['n_dataset'] = len(rec['datasets_pds'])
        rec['n_volume'] = len(rec['volumes'])
        rec['total_mb'] = pac.sum(match['size']).as_py() / 1024 ** 2
        rec['mean_mb'] = rec['total_mb'] / rec['count']
        recs.append(rec)
    return recs


def get_pds_metrics(manifest, covered, uncovered, field):
    recs = []
    vals = pac.unique(manifest[field]).to_pylist()
    for val in filter(lambda v: v != "", vals):
        rec = {
            'value': val,
            'count': pac.sum(pac.equal(manifest[field], val)).as_py()
        }
        match = covered.filter(pac.equal(covered[field], val))
        rec['datasets_ix'] = pac.unique(match['dataset_ix']).to_pylist()
        rec['ptypes'] = pac.unique(match['ptype']).to_pylist()
        rec['n_datasets_ix'] = len(rec['datasets_ix'])
        rec['n_ptypes'] = len(rec['ptypes'])
        rec['n_covered'] = len(match)
        ucmatch = uncovered.filter(pac.equal(uncovered[field], val))
        rec['n_uncovered'] = len(ucmatch)
        if (len(ucmatch) + len(match)) == 0:
            rec['coverage'] = float('nan')
        else:
            rec['coverage'] = (
                rec['n_covered'] / (rec['n_covered'] + rec['n_uncovered'])
            )
        recs.append(rec)
    return recs


def load_and_count(manifest_path):
    manifest = parquet.read_table(manifest_path)
    return count_coverage(manifest)
