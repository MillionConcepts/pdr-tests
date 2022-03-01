from pdr_tests.datasets import (
    ProductPicker,
    IndexMaker,
    IndexDownloader,
    TestHasher,
)

COMMANDS = ["sort", "pick", "index", "download", "check", "index_directory"]


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


def index_directory(
    target,
    manifest,
    output="index.csv",
    debug=False
):
    from pathlib import Path
    import pandas as pd
    from pyarrow import parquet
    from pdr_tests.utilz.test_utilz import console_and_log, get_product_row
    product_rows = []
    for file in Path(target).iterdir():
        try:
            match = parquet.read_table(
                manifest, filters=[("filename", "=", file.name)]
            )
            assert len(match) == 1
            url = match['url'].to_numpy()[0]
            product_rows.append(get_product_row(file, url))
        except KeyboardInterrupt:
            raise
        except Exception as ex:
            if debug is True:
                raise ex
            console_and_log(f"failed on {file.name}: {type(ex)}: {ex}")
    pd.DataFrame(product_rows).to_csv(output, index=None)


def ix_help(*_, **__):
    print(f"Usage: valid subcommands are: {', '.join(COMMANDS)}.")
