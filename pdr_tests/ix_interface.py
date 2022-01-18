from pdr_tests.datasets import (
    ProductPicker,
    IndexMaker,
    IndexDownloader,
    TestHasher,
)

COMMANDS = ["sort", "pick", "index", "download", "check"]


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


def download(dataset, product_type=None):
    downloader = IndexDownloader(dataset)
    downloader.download_index(product_type)


def check(
    dataset,
    product_type=None,
    *,
    dump_browse: "d" = True,
    dump_kwargs: "k" = None,
):
    hasher = TestHasher(dataset)
    hasher.hash_product_type(product_type, dump_browse, dump_kwargs)


def ix_help(*_, **__):
    print(f"Usage: valid subcommands are: {', '.join(COMMANDS)}.")
