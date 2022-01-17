from pdr_tests.datasets import ProductPicker, IndexMaker, IndexDownloader


COMMANDS = ["pl", "pick", "labels", "index", "download"]


def pl(dataset):
    picker = ProductPicker(dataset)
    picker.create_product_lists()


def pick(dataset, product_type=None, *, subset_size: "s"=200, max_gb: "m"=8):
    picker = ProductPicker(dataset)
    if product_type is None:
        picker.pick_randomly_from_all(subset_size, max_gb)
    else:
        picker.random_picks(product_type, subset_size, max_gb)


def index(dataset, product_type=None):
    indexer = IndexMaker(dataset)
    if product_type is None:
        indexer.get_all_labels()
        indexer.write_indices()
    else:
        indexer.get_labels(product_type)
        indexer.write_subset_index(product_type)


def download(dataset, product_type=None):
    downloader = IndexDownloader(dataset)
    if product_type is None:
        downloader.download_indices()
    else:
        downloader.download_index(product_type)


def ix_help(*_, **__):
    print(f"Usage: valid subcommands are: {', '.join(COMMANDS)}.")