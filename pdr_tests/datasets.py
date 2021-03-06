"""handler functions and classes for ix workflow"""

import json
import os
from importlib import import_module
from pathlib import Path
from typing import Mapping, Optional

import numpy as np
import pandas as pd
import pyarrow as pa
from pyarrow import parquet
import warnings

import pdr
from pdr_tests.utilz.ix_utilz import (
    get_product_row,
    console_and_log,
    stamp,
    download_product_row,
    verbose_temp_download,
    assemble_urls,
    flip_ends_with,
    read_and_hash,
    record_comparison,
)
from pdr_tests.utilz.dev_utilz import FakeStopwatch, Stopwatch


# ############ INDEX & TESTING CLASSES #############

class MissingHashError(ValueError):
    pass


class DatasetDefinition:
    """
    base class for this module. defines and encapsulates references / directory
    structure for the ix workflow.
    """

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
        return Path(
            self.def_path, "sample_lists", f"{product_type}_subset.csv"
        )

    def shared_list_path(self):
        return Path(
            self.def_path, "shared_lists", f"{self.dataset}_shared.csv"
        )

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
        output = []
        for product_type in self.rules:
            result = getattr(self, method_name)(product_type, *args, **kwargs)
            output.append(result)
        return output


class ProductPicker(DatasetDefinition):
    def __init__(self, name):
        super().__init__(name)

    # TODO, maybe: it is possibly time-inefficient to iterate through
    #  the manifest a bunch of times, although it's very
    #  memory-efficient. idk. it might not be as bad as i think,
    #  though, unless we did clever segmentation of results on each group.
    def make_product_list(self, product_type: str):
        """
        construct and write full-set parquet file for a given product type.
        """
        if product_type is None:
            return self.across_all_types("make_product_list")
        os.makedirs(
            self.complete_list_path(product_type).parent, exist_ok=True
        )
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
        products = pa.concat_tables(results)
        try:
            size_gb = round(pa.compute.sum(products["size"]).as_py() / 10**9, 2)
        except TypeError:
            raise ValueError('No matches found, please check selection_rules and try again.')
        # TODO: this estimate is bad for products with several large files
        print(f"{len(products)} products found, {size_gb} estimated GB")
        parquet.write_table(products, self.complete_list_path(product_type))

    def filter_table(self, product_type: str, table: pa.Table) -> pa.Table:
        """
        construct list of filter functions -- methods of pa.compute --
        based on selection rules for dataset and product type. apply them
        to select examples of specified product type from manifest table.
        """
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
        """
        randomly select a subset of products from a given product type; write
        this subset to disk as a csv file. optionally specify subset size and
        cap file size in GB.
        """
        if product_type is None:
            return self.across_all_types("random_picks", subset_size, max_gb)
        print(
            f"picking test subset for {self.dataset} {product_type} ...... ",
            end="",
        )
        max_bytes = max_gb * 10**9
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
        ix_base, picks = 0, []
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
                    print(
                        f"regex has been set to {regex} for {product_type} "
                        f"label replacement rules."
                    )
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
                size = round(subset.loc[~present]["size"].sum() / 10**9, 1)
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
        self.skip_files = ()
        if hasattr(rules_module, "SKIP_FILES"):
            self.skip_files = getattr(rules_module, "SKIP_FILES")

    def download_index(self, product_type: str, get_test: bool = False):
        if product_type is None:
            return self.across_all_types("download_index", get_test)
        ptype = "subset files" if get_test is False else "test files"
        console_and_log(f"Downloading {self.dataset} {product_type} {ptype}.")
        data_path = self.product_data_path(product_type)
        temp_path = self.temp_data_path(product_type)
        self.data_mkdirs(product_type)
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
    hash_rows, log_rows = {}, {}

    def dump_test_paths(self, product_type):
        if product_type is None:
            return self.across_all_types("dump_test_paths")
        index = pd.read_csv(self.test_path(product_type))
        data_path = self.product_data_path(product_type)
        return [
            str(Path(data_path, product["label_file"]))
            for ix, product in index.iterrows()
        ]

    def compare_test_hashes(
        self,
        product_type,
        regen=False,
        write=True,
        debug=True,
        dump_browse=False,
        dump_kwargs=None,
        quiet=False,
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
                dump_kwargs,
                quiet,
            )
        console_and_log(f"Hashing {self.dataset} {product_type}.", quiet=quiet)
        index = pd.read_csv(self.test_path(product_type))
        if "hash" not in index.columns:
            console_and_log(f"no hashes found for {product_type}, writing new", quiet=quiet)
        elif regen is True:
            console_and_log(f"regenerate=True passed, overwriting hashes", quiet=quiet)
        compare = not ((regen is True) or ("hash" not in index.columns))
        # compare/overwrite are redundant rn, but presumably we might want
        # different logic in the future.
        overwrite = (regen is True) or ("hash" not in index.columns)
        data_path = self.product_data_path(product_type)
        self.hash_rows, self.log_rows = {}, {}
        for ix, product in index.iterrows():
            console_and_log(f"testing {product['product_id']}", quiet=quiet)
            data, self.hash_rows[ix], self.log_rows[ix] = test_product(
                product, Path(data_path, product["label_file"]), compare, debug, quiet=quiet
            )
            if (dump_browse is True) and (data is not None):
                console_and_log(
                    f"dumping browse products for {product['product_id']}", quiet=quiet
                )
                self.dump_test_browse(data, product_type, dump_kwargs)
                console_and_log(
                    f"dumped browse products for {product['product_id']}", quiet=quiet
                )
        if (overwrite is True) and (write is False):
            console_and_log("write=False passed, not updating hashes in csv", quiet=quiet)
        elif overwrite is True:
            index["hash"] = pd.Series(self.hash_rows)
            index.to_csv(self.test_path(product_type), index=False)
        return self.write_test_log(product_type)

    def write_test_log(self, product_type):
        log_df = pd.DataFrame.from_dict(self.log_rows, orient="index")
        log_df["dataset"] = self.dataset
        log_df["product_type"] = product_type
        timestamp = stamp()[:-2].replace(":", "_").replace("-", "_")
        Path(self.def_path, "logs").mkdir(exist_ok=True)
        log_df.to_csv(
            Path(self.def_path, "logs", f"{product_type}_log_{timestamp}.csv"),
            index=False,
        )
        log_df.to_csv(
            Path(self.def_path, "logs", f"{product_type}_log_latest.csv"),
            index=False,
        )
        return log_df

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
            self.check_product(dump_browse, dump_kwargs, product, product_type)

    def check_product(self, dump_browse, dump_kwargs, product, product_type):
        console_and_log(f"checking {product['product_id']}")
        path = Path(
            self.product_data_path(product_type), product["label_file"]
        )
        data = pdr.read(str(path))
        data.load("all")
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


class CorpusFinalizer(DatasetDefinition):
    def __init__(self, name):
        super().__init__(name)

    def create_and_upload_test_subset(self, product_type, product=None, subset_size=1, regen=False, local=False):
        if product_type is None:
            return self.across_all_types("create_and_upload_test_subset")
        if not self.test_path(product_type).is_file() or regen:
            self.create_test_subset_csv(product_type, product, subset_size)
        if local:
            return
        self.upload_to_s3(product_type)

    def create_test_subset_csv(self, product_type, product, subset_size):
        with open(self.index_path(product_type)) as index_f, open(self.test_path(product_type), 'w+') as test_f:
            if not product:
                index_length = sum(1 for _ in index_f)
                integer_choice = np.random.choice(np.arange(1, index_length-1), size=subset_size)
                index_f.seek(0)
                for pos, line in enumerate(index_f):
                    if pos == 0 or any(pos == integer_choice):
                        test_f.write(line)
            else:
                for pos, line in enumerate(index_f):
                    if pos == 0 or product in line:
                        test_f.write(line)
                test_f.seek(0)
                test_length = sum(1 for _ in test_f)
                if test_length < 2:
                    print(f'{product} not found in {self.dataset} {product_type} index. '
                          f'Check your spelling and try again using regen=True.')

    def upload_to_s3(self, product_type):
        from killscreen.aws.s3 import put
        with open(self.test_path(product_type)) as test_f:
            next(test_f)
            for line in test_f:
                file_list = line.replace(']', '[').split('[')[1].replace('"', '').split(',')
                for file in file_list:
                    try:
                        file = file.strip()
                        put(bucket='mc-pdr-permanent-test-corpus',
                            obj=Path(self.product_data_path(product_type), file),
                            key=f'{self.dataset}/{product_type}/{file}')
                        print(f'{self.dataset} {product_type}: {file} uploaded to s3.')
                    except FileNotFoundError:
                        print(f'{file} not present in subset folder. '
                              f'Please put it in data/{self.dataset}/{product_type} and retry.')


# ############## STANDALONE / HANDLER FUNCTIONS ###############

def test_product(
    product: Mapping[str, str], path: Path, compare: bool, debug: bool, quiet: bool
) -> tuple[Optional[pdr.Data], str, dict]:
    """
    handler function for testing an individual product: records exceptions
    and (when instructed) hash/index comparisons.
    """
    data, hash_json = None, ""
    log_row = {
        "product_id": product["product_id"],
        "status": "ok",
        "error": None,
        "hashtime": None,
        "readtime": None
    }
    try:
        data, hashes, runtimes = read_and_hash(path, product, debug, quiet)
        if compare is True:
            if isinstance(product["hash"], float):
                if np.isnan(product["hash"]):
                    raise MissingHashError
            log_row = record_comparison(
                hashes, json.loads(product["hash"]), log_row
            )
        hash_json = json.dumps(hashes)
        log_row |= runtimes
    except MissingHashError:
        console_and_log(
            "Hash column present but hash value missing for one or more "
            "products. This may indicate a corrupt file or an interrupted "
            "hash generation process. Pass --regen=True to ignore this error "
            "and populate these values."
        )
        raise MissingHashError
    except KeyboardInterrupt:
        raise
    except Exception as ex:
        log_row["status"] = "read exception"
        log_row["error"] = f"{type(ex)}: {ex}".replace(",", ";")
    output_string = f"status: {log_row['status']}"
    if log_row["error"] is not None:
        output_string += f"; {log_row['error']}"
    if log_row['status'] != 'ok' and quiet:
        quiet = False
        problem_file = str(path).split('data/')[-1].split('/')
        print(" ".join(problem_file)+':')
    console_and_log(output_string, quiet=quiet)
    return data, hash_json, log_row


def directory_to_index(target, manifest, output="index.csv", debug=False, filters=None):
    """
    standalone function for producing an index from all labels in a directory.
    does not rely on a dataset definitions module. does require a manifest.
    """
    product_rows = []
    for file in Path(target).iterdir():
        try:
            pluck_row_from_manifest(file, manifest, product_rows, filters)
        except KeyboardInterrupt:
            raise
        except Exception as ex:
            if debug is True:
                raise ex
            console_and_log(f"failed on {file.name}: {type(ex)}: {ex}")
    pd.DataFrame(product_rows).to_csv(output, index=False)


def pluck_row_from_manifest(file, manifest, product_rows, filters):
    """inner row constructor for index_directory"""
    match = parquet.read_table(
        manifest, filters=[("filename", "=", file.name)]
    )
    assert len(match) >= 1, f"{file.name} not found in manifest"
    if len(match) > 1:
        warnings.warn(f'There are multiple matches to {file.name}. '
                      f'If necessary to differentiate use filters="[("y/n", "substring_in_url")]"')
    if filters: 
        match = filter_by_substring(match, filters)
    else:
        match = match.to_pandas().iloc[0]
    row = get_product_row(file, assemble_urls(match))
    product_rows.append(row)


def filter_by_substring(matches, filters):
    y = []
    n = []
    for fil in filters:
        if fil[0] == 'y':
            y = y + [fil[1]]
        if fil[0] == 'n':
            n = n + [fil[1]]
    matches = matches.to_pandas()
    for i in range(len(matches)):
        if all(sub in matches.iloc[i].url for sub in y) and not any(sub in matches.iloc[i].url for sub in n):
            match = matches.iloc[i]
            return match
