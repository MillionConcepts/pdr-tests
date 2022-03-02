import json
import os
from importlib import import_module
from pathlib import Path
from typing import Mapping, Optional

import numpy as np
import pandas as pd
import pyarrow as pa
import requests
import sh
from dustgoggles.func import disjoint, intersection
from pyarrow import parquet

import pdr
from pdr.utils import check_cases
from pdr_tests.utilz.test_utilz import (
    get_product_row,
    just_hash,
    console_and_log,
    check_product, stamp,
)

# TODO: I'm inclined not to hardcode this...but not sure. --michael

headers = {
    "User-Agent": "MillionConcepts-PDART-pdrtestsuitespider (sierra@millionconcepts.com)"
}

PARQUET_SETTINGS = {
    "row_group_size": 100000,
    "version": "2.6",
    "use_dictionary": ["domain", "url", "size"],
}


class DatasetDefinition:
    def __init__(self, name):
        rules_module = import_module(f"definitions.{name}.selection_rules")
        self.rules = getattr(rules_module, "file_information")
        self.def_path = Path(rules_module.__file__).parent
        self.data_path = Path(self.def_path.parent.parent, "data", name)
        self.browse_path = Path(self.def_path.parent.parent, "browse", name)
        self.temp_path = Path(Path.home(), "pdr_test_temp")
        self.dataset = name

    def complete_list_path(self, product_type):
        return Path(
            self.def_path, "sample_lists", f"{product_type}_complete.parquet"
        )

    def subset_list_path(self, product_type):
        return Path(self.def_path, "sample_lists", f"{product_type}_subset.csv")

    def shared_list_path(self):
        return Path(self.def_path, "shared_lists", f"{self.dataset}_shared.csv")

    def product_data_path(self, product_type):
        return Path(self.data_path, product_type)

    def temp_data_path(self, product_type):
        return Path(self.temp_path, product_type)

    def index_path(self, product_type):
        return Path(self.def_path, f"{product_type}.csv")

    def test_path(self, product_type):
        return Path(self.def_path, f"{product_type}_test.csv")

    def product_browse_path(self, product_type):
        return Path(self.browse_path, product_type)

    def data_mkdirs(self, product_type):
        os.makedirs(self.product_data_path(product_type), exist_ok=True)
        os.makedirs(self.temp_data_path(product_type), exist_ok=True)

    def across_all_types(self, method_name, *args, **kwargs):
        for product_type in self.rules:
            getattr(self, method_name)(product_type, *args, **kwargs)


class ProductPicker(DatasetDefinition):
    def __init__(self, name):
        super().__init__(name)

    # TODO, maybe: it is possibly time-inefficient to iterate through
    #  the manifest a bunch of times, although it's very
    #  memory-efficient. idk. it might not be as bad as i think,
    #  though, unless we did clever segmentation of results on
    #  each group.
    def make_product_list(self, product_type):
        if product_type is None:
            return self.across_all_types("make_product_list")
        os.makedirs(self.complete_list_path(product_type).parent, exist_ok=True)
        print(f"Making product list for {product_type} ...... ", end="")
        self.complete_list_path(product_type).unlink(missing_ok=True)
        manifest = self.rules[product_type]["manifest"]
        manifest_parquet = parquet.ParquetFile(manifest)
        results = []
        for group_ix in range(manifest_parquet.num_row_groups):
            results.append(
                self.filter_table(
                    product_type, manifest_parquet.read_row_group(group_ix)
                )
            )
        product_list_table = pa.concat_tables(results)
        size_gb = round(
            pa.compute.sum(product_list_table["size"]).as_py() / 10**9, 2
        )
        print(
            f"{len(product_list_table)} products found, {size_gb} estimated GB"
        )
        parquet.write_table(
            product_list_table,
            self.complete_list_path(product_type),
        )

    def filter_table(self, product_type, table):
        info = self.rules[product_type]
        filts = []
        if "url_must_contain" in info.keys():
            for string in info["url_must_contain"]:
                filts.append((pa.compute.match_substring, "url", string))
        if "fn_ends_with" in info.keys():
            ends = info["fn_ends_with"]
            assert len(ends) == 1, "only one filename ending may be specified"
            filts.append((flip_ends_with, "filename", ends[0]))
        if "fn_must_contain" in info.keys():
            for string in info["fn_must_contain"]:
                filts.append((pa.compute.match_substring, "filename", string))
        if "fn_regex" in info.keys():
            for string in info["fn_regex"]:
                filts.append(
                    (pa.compute.match_substring_regex, "filename", string)
                )
        if len(filts) == 0:
            raise ValueError("filters must be specified for product types.")
        for method, column, substring in filts:
            table = table.filter(method(table[column], substring))
        return table

    def random_picks(
        self,
        product_type: str,
        subset_size: int = 200,
        max_gb: float = 8,
    ):
        if product_type is None:
            return self.across_all_types("random_picks", subset_size, max_gb)
        print(
            f"picking test subset for {self.dataset} {product_type} ...... ",
            end="",
        )
        max_bytes = max_gb * 10 ** 9
        complete = self.complete_list_path(product_type)
        subset = self.subset_list_path(product_type)
        total = parquet.read_metadata(complete).num_rows
        if total < subset_size:
            # pick them all (if not too big)
            small_enough = parquet.read_table(
                complete, filters=[("size", "<", max_bytes)]
            )

            print(
                f"{total} products; {len(small_enough)}/{total} < {max_gb} GB "
                f"cutoff; taking all {len(small_enough)}"
            )
            small_enough.to_pandas().to_csv(subset, index=None)
            return
        sizes = parquet.read_table(complete, columns=["size"])[
            "size"
        ].to_numpy()
        small_enough_ix = np.nonzero(sizes < max_bytes)[0]
        pick_ix = np.sort(np.random.choice(small_enough_ix, subset_size))
        print(
            f"{total} products; {len(small_enough_ix)}/{total} < {max_gb} GB "
            f"cutoff; randomly picking {subset_size}"
        )
        # TODO: this is not very clever
        ix_base = 0
        picks = []
        complete_parquet = parquet.ParquetFile(complete)
        for group_ix in range(complete_parquet.num_row_groups):
            group = complete_parquet.read_row_group(group_ix)
            available = [
                ix - ix_base for ix in pick_ix if ix - ix_base < len(group)
            ]
            if len(available) != 0:
                picks.append(group.take(available))
        pa.concat_tables(picks).to_pandas().to_csv(subset, index=None)


class IndexMaker(DatasetDefinition):
    def __init__(self, name):
        super().__init__(name)

    def get_labels(self, product_type: str, dry_run: bool = False):
        if product_type is None:
            return self.across_all_types("get_labels", dry_run)
        self.data_mkdirs(product_type)
        dry = "" if dry_run is False else "(dry run)"
        print(f"Downloading labels for {self.dataset} {product_type} {dry}")
        subset = self.load_subset_table(product_type)
        if dry_run is True:
            return
        for url in subset["url"]:
            verbose_temp_download(
                self.product_data_path(product_type),
                self.temp_data_path(product_type),
                url,
            )

    def load_subset_table(self, product_type: str, verbose: bool = True):
        subset = pd.read_csv(self.subset_list_path(product_type))
        detached = self.rules[product_type]["label"] != "A"
        if detached:
            # TODO: PDS4
            label_rule = self.rules[product_type]["label"]
            if isinstance(label_rule, tuple):
                try:
                    regex = self.rules[product_type]["regex"]
                    print(f'regex has been set to {regex} for {product_type} label replacement rules.')
                except KeyError:
                    regex = False
                subset["filename"] = subset["filename"].str.replace(
                    *label_rule, regex
                )
            else:
                subset["filename"] = subset["filename"].map(
                    lambda fn: Path(fn).with_suffix(".LBL").name
                )
        subset["url"] = assemble_urls(subset)
        subset["path"] = subset["filename"].map(
            lambda fn: Path(self.product_data_path(product_type), fn)
        )
        if verbose is True:
            present = subset["path"].map(lambda path: path.exists())
            if detached:
                size_message = "detached labels; "
            else:
                size = round(subset.loc[~present]["size"].sum() / 10 ** 9, 1)
                size_message = f"attached labels; total download ~{size} GB"
            print(
                f"{len(subset)} labels; "
                f"{len(subset.loc[present])} already in system; {size_message}"
            )
        return subset

    def write_subset_index(self, product_type: str):
        if product_type is None:
            return self.across_all_types("write_subset_index")
        print(f"Writing index for {self.dataset} {product_type}")
        subset = self.load_subset_table(product_type, verbose=False)
        product_rows = []
        for ix, product in subset.iterrows():
            product_row = get_product_row(product["path"], product["url"])
            print(product_row)
            product_rows.append(product_row)
        # noinspection PyTypeChecker
        pd.DataFrame(product_rows).to_csv(
            self.index_path(product_type), index=None
        )
        print(f"Wrote index for {self.dataset} {product_type} subset.")


class IndexDownloader(DatasetDefinition):
    def __init__(self, name):
        super().__init__(name)
        rules_module = import_module(f"definitions.{name}.selection_rules")
        if hasattr(rules_module, "SKIP_FILES"):
            self.skip_files = getattr(rules_module, "SKIP_FILES")
        else:
            self.skip_files = ()

    def download_index(self, product_type: str, get_test: bool = False):
        if product_type is None:
            return self.across_all_types("download_index", get_test)
        ptype = "subset files" if get_test is False else "test files"
        console_and_log(f"Downloading {self.dataset} {product_type} {ptype}.")
        data_path = self.product_data_path(product_type)
        temp_path = self.temp_data_path(product_type)
        os.makedirs(data_path, exist_ok=True)
        os.makedirs(temp_path, exist_ok=True)
        if self.shared_list_path().exists():
            print(f"Checking shared files for {self.dataset}.")
            shared_index = pd.read_csv(self.shared_list_path())
            for ix, row in shared_index.iterrows():
                verbose_temp_download(
                    data_path, temp_path, row["url"], skip_quietly=False
                )
        if get_test is True:
            index = pd.read_csv(self.test_path(product_type))
        else:
            index = pd.read_csv(self.index_path(product_type))
        for ix, row in index.iterrows():
            console_and_log(f"Downloading product id: {row['product_id']}")
            download_product_row(data_path, temp_path, row, self.skip_files)


class ProductChecker(DatasetDefinition):
    def __init__(self, name):
        super().__init__(name)

    def compare_test_hashes(
        self,
        product_type,
        regen=False,
        write=True,
        debug=True,
        dump_browse=False,
        dump_kwargs=None
    ):
        """
        generate and / or compare test hashes for a specified mission and
        dataset. writes new hashes into test index files if no hashes are
        present.

        regenerate: if True, skip hash comparisons and instead overwrite any
        hashes found in test index files

        write: if False, do a 'dry run' -- don't write anything besides logs
        regardless of other settings/results

        debug: should we open products in debug mode?

        dump_browse: if True, also write browse products

        dump_kwargs: kwargs for browse writer
        """
        if product_type is None:
            return self.across_all_types(
                "compare_test_hashes",
                regen,
                write,
                debug,
                dump_browse,
                dump_kwargs
            )
        console_and_log(f"Hashing {self.dataset} {product_type}.")
        index = pd.read_csv(self.test_path(product_type))
        if "hash" not in index.columns:
            console_and_log(f"no hashes found for {product_type}, writing new")
        elif regen is True:
            console_and_log(f"regenerate=True passed, overwriting hashes")
        compare = not ((regen is True) or ("hash" not in index.columns))
        # compare/overwrite are redundant rn, but presumably we might want
        # different logic in the future.
        overwrite = ((regen is True) or ("hash" not in index.columns))
        hash_rows = {}
        log_rows = {}
        data_path = self.product_data_path(product_type)
        for ix, product in index.iterrows():
            console_and_log(f"testing {product['product_id']}")
            data, hash_rows[ix], log_rows[ix] = test_product(
                product, Path(data_path, product["label_file"]), compare, debug
            )
            if (dump_browse is True) and (data is not None):
                console_and_log(
                    f"dumping browse products for {product['product_id']}"
                )
                self.dump_test_browse(data, product_type, dump_kwargs)
                console_and_log(
                    f"dumped browse products for {product['product_id']}"
                )
        if (overwrite is True) and (write is False):
            console_and_log("write=False passed, not updating hashes in csv")
        elif overwrite is True:
            index["hash"] = pd.Series(hash_rows)
            index.to_csv(self.test_path(product_type), index=False)
        log_df = pd.DataFrame.from_dict(log_rows, orient='index')
        timestamp = stamp()[:-2].replace(":", "_").replace("-", "_")
        Path(self.def_path, "logs").mkdir(exist_ok=True)
        log_df.to_csv(
            Path(self.def_path, "logs", f"{product_type}_log_{timestamp}.csv"),
            index=False
        )
        log_df.to_csv(
            Path(self.def_path, "logs", f"{product_type}_log_latest.csv"),
            index=False
        )

    def check_product_type(
        self, product_type, dump_browse=True, dump_kwargs=None
    ):
        """
        generate browse products for a specified mission and dataset.

        dump_browse: if True, also write browse products (by default, write to
        browse/mission/dataset/, although this can be overridden by passing a
        different path in dump_kwargs

        dump_kwargs: kwargs for browse writer
        """
        if product_type is None:
            return self.across_all_types(
                "check_product_type", dump_browse, dump_kwargs
            )
        console_and_log(f"Checking {self.dataset} {product_type}.")
        index = pd.read_csv(self.index_path(product_type))
        for _, product in index.iterrows():
            console_and_log(f"checking {product['product_id']}")
            path = Path(
                self.product_data_path(product_type), product["label_file"]
            )
            data = pdr.read(str(path))
            console_and_log(f"opened {product['product_id']}")
            if dump_browse:
                console_and_log(
                    f"dumping browse products for {product['product_id']}"
                )
                self.dump_test_browse(data, product_type, dump_kwargs)
                console_and_log(
                    f"dumped browse products for {product['product_id']}"
                )

    def dump_test_browse(self, data, product_type, dump_args):
        kwargs = {} if dump_args is None else dump_args.copy()
        if "outpath" not in kwargs.keys():
            kwargs["outpath"] = self.product_browse_path(product_type)
        os.makedirs(kwargs["outpath"], exist_ok=True)
        if "purge" not in kwargs.keys():
            kwargs["purge"] = True
        if "scaled" not in kwargs.keys():
            kwargs["scaled"] = "both"
        data.dump_browse(**kwargs)


def download_product_row(data_path, temp_path, row, skip_files=()):
    files = json.loads(row["files"])
    for file in files:
        if Path(data_path, file).exists():
            console_and_log(f"... {file} present, skipping ...")
            continue
        if any((file == skip_file for skip_file in skip_files)):
            continue
        url = f"{row['url_stem']}/{file}"
        verbose_temp_download(data_path, temp_path, url)


# TODO / note: this is yet one more download
#  thing that we should somehow unify and consolidate
def verbose_temp_download(data_path, temp_path, url, skip_quietly=True):
    try:
        check_cases(Path(data_path, Path(url).name))
        if skip_quietly is False:
            console_and_log(
                f"{Path(url).name} already present, skipping download."
            )
        return
    except FileNotFoundError:
        pass
    console_and_log(f"attempting to download {url}.")
    response = requests.get(url, stream=True, headers=headers)
    if not response.ok:
        console_and_log(f"Download of {url} failed.")
        return
    with open(Path(temp_path, Path(url).name), "wb+") as fp:
        for chunk in response.iter_content(chunk_size=10 ** 7):
            fp.write(chunk)
    sh.mv(Path(temp_path, Path(url).name), Path(data_path, Path(url).name))
    console_and_log(f"completed download of {url}.")


# noinspection HttpUrlsUsage
def assemble_urls(subset: pd.DataFrame):
    return "http://" + subset.domain + "/" + subset.url + "/" + subset.filename


def record_mismatches(results, absent, novel):
    """Assigns strings of "missing from output" and "not found in reference" to
    the value of the missing and new keys in the results dictionary."""
    for key in absent:
        results[key] = "missing from output"
    for key in novel:
        results[key] = "not found in reference"
    return results


def compare_hashes(
    test: Mapping[str, str], reference: Mapping[str, str]
) -> Mapping[str, str]:
    """
    Compares two mappings, notionally from object name to hashed value of
    object.

    Returns a dictionary containing new keys, missing keys, and keys with
    mismatched hash values.
    """
    problems = {}
    new_keys, missing_keys = disjoint(test, reference)
    # note keys that are completely new or missing
    if len(new_keys + missing_keys):
        problems |= record_mismatches(problems, missing_keys, new_keys)
    # do comparisons between others
    for key in intersection(test, reference):
        if test[key] != reference[key]:
            problems[key] = (
                f"hashes !=; test: {test[key]}; reference: {reference[key]}"
            )
    return problems


def flip_ends_with(strings, ending):
    return pa.compute.ends_with(strings, pattern=ending)


def read_and_hash(log_row, path, product, debug):
    data = pdr.read(str(path), debug=debug)
    hashes = just_hash(data)
    console_and_log(f"Opened and hashed {product['product_id']}")
    return data, hashes, log_row


def record_comparison(test, reference, log_row):
    result = compare_hashes(test, reference)
    if result != {}:
        log_row["status"] = "hash mismatch"
        log_row["error"] = str(result)
    return log_row


def test_product(
    product: Mapping[str, str], path: Path, compare: bool, debug: bool
) -> tuple[Optional[pdr.Data], str, dict]:
    data, hash_json = None, ""
    log_row = {
        "product_id": product['product_id'], "status": "ok", "error": None
    }
    try:
        data, hashes, log_row = read_and_hash(log_row, path, product, debug)
        if compare is True:
            log_row = record_comparison(
                hashes, json.loads(product['hash']), log_row
            )
        hash_json = json.dumps(hashes)
    except KeyboardInterrupt:
        raise
    except Exception as ex:
        log_row["status"] = "read exception"
        log_row["error"] = f"{type(ex)}: {ex}".replace(",", ";")
    output_string = f"status: {log_row['status']}"
    if log_row["error"] is not None:
        output_string += f"; {log_row['error']}"
    console_and_log(output_string)
    return data, hash_json, log_row
