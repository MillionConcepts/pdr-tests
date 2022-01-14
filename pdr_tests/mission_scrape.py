import json
import os
import random
from pathlib import Path

import pandas as pd
import requests
import sh
from importlib import import_module

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
            self.def_path, "url_lists", f"{product_type_name}_complete.csv"
        )

    def subset_list_path(self, product_type_name):
        return Path(
            self.def_path, "url_lists", f"{product_type_name}_subset.csv"
        )

    def product_data_path(self, product_type_name):
        return Path(self.data_path, product_type_name)

    def temp_data_path(self, product_type_name):
        return Path(self.temp_path, product_type_name)


class ProductPicker(Dataset):
    def __init__(self, name):
        super().__init__(name)
        # TODO: maybe expose this as an option
        self.max_bytes = 8 * 10 ** 9
        self.subset_size = 200
        # TODO: i removed destination_folder for now to rigidly constrain
        #  directory structure. we can add it again if we need it. --michael
        # TODO: I am not in favor of the class firing itself off as soon as it
        #  is initialized. this is equivalent to just making it a script with
        #  every attribute defined as module-level constants. if it's
        #  inconvenient, we can put it back. --michael

    def create_product_lists(self):
        # TODO: feels gross. should fix this big-file issue.
        manifests = set(info["manifest"] for info in self.rules.values())
        os.makedirs(self.complete_list_path("").parent, exist_ok=True)
        for manifest in manifests:
            product_types = [
                pt
                for pt, info in self.rules.items()
                if info["manifest"] == manifest
            ]
            print(
                f"making lists from {manifest.name}; corresponding product "
                f"types are {product_types}"
            )
            for pt in product_types:
                self.complete_list_path(pt).unlink(missing_ok=True)
            in_file = open(manifest)
            for line in in_file:
                for pt in product_types:
                    if self.pick_line(pt, line):
                        with open(self.complete_list_path(pt), "a+") as file:
                            file.write(line)
            in_file.close()

    def pick_line(self, product_type, line):
        info = self.rules[product_type]
        fn, url, size = split_node_manifest_line(line)
        if size == 0:
            return False
        if not all(val in fn for val in info["fn_must_contain"]):
            return False
        if info.get("url_must_contain") is not None:
            if not all(val in url for val in info["url_must_contain"]):
                return False
        return True

    def pick_randomly_from_all(self):
        for product_type in self.rules:
            print(f"making random picks for {product_type}")
            self.random_picks(product_type)

    # TODO: I've made downloading functionality separate; it seems awkward
    #  to have it ensuite. --michael
    def random_picks(self, product_type_name: str):
        pl = open(self.complete_list_path(product_type_name))
        line_count = 0
        for _ in pl:
            line_count += 1
        pl.seek(0)
        sl = open(self.subset_list_path(product_type_name), "w+")
        if line_count < self.subset_size:
            # pick them all (if not too big)
            for fn, url, size in map(split_node_manifest_line, pl):
                if size < self.max_bytes:
                    sl.write(url + "\n")
            pl.close()
            sl.close()
            return
        # we selected these urls; they were not too big
        urls_selected = []
        # we looked at these indices, and perhaps rejected them; or perhaps not
        indices_considered = []
        while (len(urls_selected) < self.subset_size) and (
            len(indices_considered) < line_count - 1
        ):
            ind = random.randint(0, line_count - 1)
            if ind in indices_considered:
                continue
            indices_considered = indices_considered + [ind]
            for ix, line in enumerate(pl):
                if ind == ix:
                    fn, url, size = split_node_manifest_line(line)
                    if size < self.max_bytes:
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
            url = os.path.dirname(url) + '/' + fn
        verbose_temp_download(data_path, temp_path, url)

    def write_subset_index(self, product_type: str):
        data_path = self.product_data_path(product_type)
        with open(self.subset_list_path(product_type)) as sl:
            urls = [line.strip() for line in sl.readlines()]
            labels = [Path(data_path, Path(url).name) for url in urls]
        rows = []
        for label, url in zip(labels, urls):
            rows.append(get_product_row(label, url))
        with open(Path(self.def_path, product_type + ".csv")) as index_file:
            index_file.write("\n".join(rows))


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

    def download_indices(self):
        for product_type in self.rules:
            print(f"Downloading {self.dataset} {product_type} subset.")
            self.download_index(product_type)
        if Path(self.def_path, "shared.csv").exists():
            shared_path = Path(self.data_path, "shared")
            shared_index = pd.read_csv(self.def_path, "shared.csv")
            for ix, row in shared_index.iterrows():
                if Path(shared_path, row["filename"]).exists():
                    print(f"{row['filename']} present, skipping")
                    continue
                verbose_temp_download(shared_path, self.temp_path, row["url"])


def download_product_row(data_path, temp_path, row):
    files = json.loads(row["files"])
    for file in files:
        if Path(data_path, file).exists():
            print(f"{file} present, skipping")
            continue
        url = row["url_stem"] + file
        verbose_temp_download(data_path, temp_path, url)


def verbose_temp_download(data_path, temp_path, url):
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
