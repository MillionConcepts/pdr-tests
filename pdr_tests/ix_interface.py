from ast import literal_eval

from pdr_tests.datasets import (
    ProductPicker,
    IndexMaker,
    IndexDownloader,
    ProductChecker, directory_to_index,
)

COMMANDS = [
    "sort", "pick", "index", "download", "check", "test", "index_directory"
]


def sort(dataset, product_type=None):
    picker = ProductPicker(dataset)
    picker.make_product_list(product_type)


def pick(
    dataset, product_type=None, *, subset_size: "s" = 200, max_gb: "m" = 8
):
    picker = ProductPicker(dataset)
    picker.random_picks(product_type, subset_size, max_gb)


def index(dataset, product_type=None, *, dry_run: "d" = False):
    indexer = IndexMaker(dataset)
    indexer.get_labels(product_type, dry_run)
    if dry_run:
        return
    indexer.write_subset_index(product_type)


def download(dataset, product_type=None, *, get_test: "t"=False):
    downloader = IndexDownloader(dataset)
    downloader.download_index(product_type, get_test)


def check(
    dataset,
    product_type=None,
    *,
    dump_browse: "d" = True,
    dump_kwargs: "k" = None,
):
    if dump_kwargs is not None:
        dump_kwargs = literal_eval(dump_kwargs)
    hasher = ProductChecker(dataset)
    hasher.check_product_type(product_type, dump_browse, dump_kwargs)


def test(
    dataset,
    product_type=None,
    *,
    regen: "r" = False,
    write: "w" = True,
    debug: "g" = True,
    dump_browse: "d" = False,
    dump_kwargs: "k" = None,
):
    if dump_kwargs is not None:
        dump_kwargs = literal_eval(dump_kwargs)
    hasher = ProductChecker(dataset)
    hasher.compare_test_hashes(
        product_type, regen, write, debug, dump_browse, dump_kwargs
    )


def index_directory(target, manifest, output="index.csv", debug=False):
    """simple wrapper for datasets.directory_to_index"""
    directory_to_index(target, manifest, output, debug)


def ix_help(*_, **__):
    print(f"Usage: valid subcommands are: {', '.join(COMMANDS)}.")
