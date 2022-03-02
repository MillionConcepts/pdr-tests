from ast import literal_eval

from pdr_tests.datasets import (
    ProductPicker,
    IndexMaker,
    IndexDownloader,
    ProductChecker,
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


def index_directory(
    target,
    manifest,
    output="index.csv",
    debug=False
):
    from pathlib import Path
    import pandas as pd
    from pyarrow import parquet
    from pdr_tests.datasets import assemble_urls
    from pdr_tests.utilz.test_utilz import console_and_log, get_product_row
    product_rows = []
    for file in Path(target).iterdir():
        try:
            match = parquet.read_table(
                manifest, filters=[("filename", "=", file.name)]
            )
            assert len(match) == 1, f"{file.name} not found in manifest"
            match = match.to_pandas().iloc[0]
            row = get_product_row(file, assemble_urls(match))
            product_rows.append(row)
        except KeyboardInterrupt:
            raise
        except Exception as ex:
            if debug is True:
                raise ex
            console_and_log(f"failed on {file.name}: {type(ex)}: {ex}")
    pd.DataFrame(product_rows).to_csv(output, index=False)


def ix_help(*_, **__):
    print(f"Usage: valid subcommands are: {', '.join(COMMANDS)}.")
