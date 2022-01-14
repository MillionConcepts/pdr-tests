from pdr_tests.mission_scrape import ProductPicker, IndexMaker, IndexDownloader


def pl(dataset, _):
    picker = ProductPicker(dataset)
    picker.create_product_lists()


def pick(dataset, product_type=None):
    picker = ProductPicker(dataset)
    if product_type is None:
        picker.pick_randomly_from_all()
    else:
        picker.random_picks(product_type)


def labels(dataset, product_type=None):
    indexer = IndexMaker(dataset)
    if product_type is None:
        indexer.get_all_labels()
    else:
        indexer.get_labels(product_type)


def index(dataset, product_type=None):
    indexer = IndexMaker(dataset)
    if product_type is None:
        indexer.write_indices()
    else:
        indexer.write_subset_index(product_type)


def download(dataset, product_type=None):
    downloader = IndexDownloader(dataset)
    if product_type is None:
        downloader.download_indices()
    else:
        downloader.download_index(product_type)
