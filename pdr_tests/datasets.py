from importlib import import_module
import json
import os
from pathlib import Path
import random

import pandas as pd
import pyarrow as pa
from pyarrow import parquet
import requests
import sh

# TODO: I'm inclined not to hardcode this...but not sure. --michael


from pdr_tests.utilz.test_utilz import (
    split_node_manifest_line,
    get_product_row,
)

headers = {
    "User-Agent": "MillionConcepts-PDART-pdrtestsuitespider (sierra@millionconcepts.com)"
}


class Dataset:
    def __init__(self, name):
        rules_module = import_module(f"definitions.{name}.selection_rules")
        self.rules = getattr(rules_module, "file_information")
        self.def_path = Path(rules_module.__file__).parent
        self.data_path = Path(
            Path(rules_module.__file__).parent.parent.parent, "data", name
        )
        self.temp_path = Path(Path.home(), "pdr_test_temp")
        self.dataset = name

    def complete_list_path(self, product_type_name):
        return Path(
            self.def_path, "url_lists", f"{product_type_name}_complete.parquet"
        )

    def subset_list_path(self, product_type_name):
        return Path(
            self.def_path, "url_lists", f"{product_type_name}_subset.csv"
        )

    def shared_list_path(self, product_type_name):
        return Path(
            self.def_path, "url_lists", f"{product_type_name}_shared.csv"
        )

    def product_data_path(self, product_type_name):
        return Path(self.data_path, product_type_name)

    def temp_data_path(self, product_type_name):
        return Path(self.temp_path, product_type_name)


class ProductPicker(Dataset):
    def __init__(self, name):
        super().__init__(name)
        # TODO: maybe expose this as an option
        # TODO: i removed destination_folder for now to rigidly constrain
        #  directory structure. we can add it again if we need it. --michael
        # TODO: I am not in favor of the class firing itself off as soon as it
        #  is initialized. this is equivalent to just making it a script with
        #  every attribute defined as module-level constants. if it's
        #  inconvenient, we can put it back. --michael

    def create_product_lists(self):
        os.makedirs(self.complete_list_path("").parent, exist_ok=True)
        for product_type in self.rules.keys():
            # TODO, maybe: it is possibly time-inefficient to iterate through
            #  the manifest a bunch of times, although it's very
            #  memory-efficient. idk. it might not be as bad as i think,
            #  though, unless we did clever segmentation of results on
            #  each group.
            print(f"Making product list for {product_type}")
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
            parquet.write_table(
                product_list_table,
                self.complete_list_path(product_type),
                row_group_size=100000,
                version="2.6",
                use_dictionary=["domain", "url", "size"],
            )

    def filter_table(self, product_type, table):
        info = self.rules[product_type]
        filts = []
        if "url_must_contain" in info.keys():
            for string in info["url_must_contain"]:
                filts.append(("url", string))
        for string in info["fn_must_contain"]:
            filts.append(("filename", string))
        for column, substring in filts:
            table = table.filter(
                pa.compute.match_substring(table[column], substring)
            )
        return table

    def pick_randomly_from_all(
        self, subset_size: int = 200, max_gb: float = 8
    ):
        for product_type in self.rules:
            print(f"making random picks for {product_type}")
            self.random_picks(product_type, subset_size, max_gb)

    # TODO: I've made downloading functionality separate; it seems awkward
    #  to have it ensuite. --michael
    def random_picks(
        self,
        product_type: str,
        subset_size: int = 200,
        max_gb: float = 8,
    ):
        max_bytes = max_gb * 10 ** 9
        pl = open(self.complete_list_path(product_type))
        line_count = 0
        for _ in pl:
            line_count += 1
        pl.seek(0)
        sl = open(self.subset_list_path(product_type), "w+")
        if line_count < subset_size:
            # pick them all (if not too big)
            for fn, url, size in map(split_node_manifest_line, pl):
                if size < max_bytes:
                    sl.write(url + "\n")
            pl.close()
            sl.close()
            return
        # we selected these urls; they were not too big
        urls_selected = []
        # we looked at these indices, and perhaps rejected them; or perhaps not
        indices_considered = []
        while (len(urls_selected) < subset_size) and (
            len(indices_considered) < line_count - 1
        ):
            ind = random.randint(0, line_count - 1)
            if ind in indices_considered:
                continue
            indices_considered = indices_considered + [ind]
            for ix, line in enumerate(pl):
                if ind == ix:
                    fn, url, size = split_node_manifest_line(line)
                    if size < max_bytes:
                        urls_selected.append(url)
                    break
            pl.seek(0)
        sl.write("\n".join(urls_selected))
        sl.close()


class IndexMaker(Dataset):
    def __init__(self, name):
        super().__init__(name)

    def get_all_labels(self):
        for product_type in self.rules:
            print(
                f"Downloading labels for {self.dataset} {product_type} subset."
            )
            self.get_labels(product_type)

    def write_indices(self):
        for product_type in self.rules:
            self.write_subset_index(product_type)

    def get_labels(self, product_type: str):
        if not self.data_path.exists():
            os.makedirs(self.data_path)
        with open(self.subset_list_path(product_type)) as subset:
            for url in subset:
                self.download_label(url.strip(), product_type)

    # TODO / note: this is yet one more download
    #  thing that we should somehow unify and consolidate; also, I split
    #  the label and 'product' downloading stages so that indexing can happen
    def download_label(self, url: str, product_type: str):
        data_path = self.product_data_path(product_type)
        temp_path = self.temp_data_path(product_type)
        os.makedirs(data_path, exist_ok=True)
        os.makedirs(temp_path, exist_ok=True)
        if self.rules[product_type]["label"] == "D":
            # TODO: both cases, xml, etc. -- hacky
            fn = Path(url).with_suffix(".LBL").name
            url = os.path.dirname(url) + "/" + fn
        verbose_temp_download(data_path, temp_path, url)

    def write_subset_index(self, product_type: str):
        data_path = self.product_data_path(product_type)
        with open(self.subset_list_path(product_type)) as sl:
            urls = [line.strip() for line in sl.readlines()]
            labels = [Path(data_path, Path(url).name) for url in urls]
        rows = []
        for label, url in zip(labels, urls):
            row = get_product_row(label, url)
            print(row)
            rows.append(row)
        # noinspection PyTypeChecker
        pd.DataFrame(rows).to_csv(
            Path(self.def_path, f"{product_type}.csv"), index=None
        )
        print(f"Wrote index for {self.dataset} {product_type} subset.")


class IndexDownloader(Dataset):
    def __init__(self, name):
        super().__init__(name)

    def download_index(self, product_type: str):
        data_path = self.product_data_path(product_type)
        temp_path = self.temp_data_path(product_type)
        os.makedirs(data_path, exist_ok=True)
        os.makedirs(temp_path, exist_ok=True)
        index = pd.read_csv(Path(self.def_path, f"{product_type}.csv"))
        for ix, row in index.iterrows():
            print(f"Downloading {row['product_id']}")
            download_product_row(data_path, temp_path, row)
        if self.shared_list_path(product_type).exists():
            print(f"Checking shared files for {self.dataset} {product_type}.")
            shared_index = pd.read_csv(self.shared_list_path(product_type))
            for ix, row in shared_index.iterrows():
                verbose_temp_download(
                    data_path, temp_path, row["url"], skip_quietly=False
                )

    def download_indices(self):
        for product_type in self.rules:
            print(f"Downloading {self.dataset} {product_type} subset.")
            self.download_index(product_type)


class TestHasher(Dataset):
    def __init__(self, name):
        super().__init__(name)

    def regenerate_hashes(
        self, dump_browse=False, write=True, dump_kwargs=None
    ):
        for product_type in self.rules:
            print(f"Regenerating hashes for {self.dataset} {product_type}.")
            self.hash_product_type(
                product_type, dump_browse, write, dump_kwargs
            )

    def hash_product_type(
        self, product_type, dump_browse=False, write=True, dump_kwargs=None
    ):
        """
        (re)generate test hashes for a specified mission and dataset.

        dump_browse: if True, also write browse products (by default, write to
        browse/mission/dataset/, although this can be overridden by passing a
        different path in dump_kwargs

        write: if False, do a 'dry run' -- don't write any hashes

        dump_kwargs: kwargs for dump_browse
        """
        products, references = find_test_paths(mission, dataset, rules)
        #     if len(products) == 0:
        #         pdrtestlog.warning(f"no products found for {mission} {dataset}")
        #         return None
        #     results = {}
        #     for _, product in products.iterrows():
        #         pdrtestlog.info(f"hashing {product['product_id']}")
        #         results[product["product_id"]], data = check_product(
        #             product, references, [just_hash]
        #         )
        """
                


#
#     mission,
#     dataset,
#     dump_browse=False,
#     write=True,
#     dump_kwargs=None
# ):
#     """


#     (re)generate test hashes for a specified mission and dataset defined in
#     pdr_tests.definitions.datasets.DATASET_TESTING_RULES. Doesn't care about
#     any other checks defined in those rules, and doesn't even care if "nohash"
#     is set in the rules; just hashes.
#
#     dump_browse: if True, also write browse products (by default write to
#     reference/temp/browse/mission/dataset/, although this can be overridden
#     by passing a different path in dump_kwargs
#
#     write: if False, do a 'dry run' -- don't write any hashes
#
#     dump_kwargs: kwargs for dump_browse
#     """
#     rules = DATASET_TESTING_RULES[mission][dataset]
#     products, references = find_test_paths(mission, dataset, rules)
#     if len(products) == 0:
#         pdrtestlog.warning(f"no products found for {mission} {dataset}")
#         return None
#     results = {}
#     for _, product in products.iterrows():
#         pdrtestlog.info(f"hashing {product['product_id']}")
#         results[product["product_id"]], data = check_product(
#             product, references, [just_hash]
#         )
#         pdrtestlog.info(f"hashed {product['product_id']}")
#         if dump_browse:
#             pdrtestlog.info(
#                 f"dumping browse products for {product['product_id']}"
#             )
#             dump_test_browse(data, dataset, dump_kwargs, mission)
#             pdrtestlog.info(
#                 f"dumped browse products for {product['product_id']}"
#             )
#     serial = {
#         product_id: json.dumps(hashes)
#         for product_id, hashes in results.items()
#     }
#     serialframe = pd.DataFrame.from_dict(serial, orient="index")
#     serialframe.columns = ["hashes"]
#     serialframe["product_id"] = serialframe.index
#     if write:
#         hash_path = Path(REF_ROOT, "temp", "hash", f"{mission}_{dataset}.csv")
#         os.makedirs(hash_path.parent, exist_ok=True)
#         # noinspection PyTypeChecker
#         serialframe.to_csv(hash_path, index=None)
#     return serialframe


def download_product_row(data_path, temp_path, row):
    files = json.loads(row["files"])
    for file in files:
        if Path(data_path, file).exists():
            print(f"{file} present, skipping")
            continue
        url = row["url_stem"] + file
        verbose_temp_download(data_path, temp_path, url)


def verbose_temp_download(data_path, temp_path, url, skip_quietly=True):
    if Path(data_path, Path(url).name).exists():
        if skip_quietly is False:
            print(f"{Path(url).name} already present, skipping download.")
        return
    print(f"attempting to download {url}.")
    response = requests.get(url, stream=True, headers=headers)
    if not response.ok:
        print(f"Download of {url} failed.")
        return
    with open(Path(temp_path, Path(url).name), "wb+") as fp:
        for chunk in response:
            fp.write(chunk)
    sh.mv(Path(temp_path, Path(url).name), Path(data_path, Path(url).name))
    print(f"completed download of {url}.")
