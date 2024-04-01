from ast import literal_eval
from itertools import chain
from pathlib import Path

from pdr_tests.datasets import (
    ProductPicker,
    IndexMaker,
    IndexDownloader,
    ProductChecker,
    CorpusFinalizer,
    directory_to_index,
    MissingHashError,
)
from pdr_tests.utilz.ix_utilz import console_and_log

COMMANDS = [
    "sort",
    "pick",
    "index",
    "download",
    "check",
    "finalize",
    "test",
    "index_directory",
    "test_paths"
]


def sort(dataset, product_type=None):
    picker = ProductPicker(dataset)
    picker.make_product_list(product_type)


def pick(
    dataset, product_type=None, *, subset_size: "s" = 200, max_size: "m" = 8000
):
    picker = ProductPicker(dataset)
    picker.random_picks(product_type, subset_size, max_size)


def index(dataset, product_type=None, *, dry_run: "d" = False):
    indexer = IndexMaker(dataset)
    indexer.get_labels(product_type, dry_run)
    if dry_run:
        return
    indexer.write_subset_index(product_type)


def download(
    dataset=None,
    product_type=None,
    *,
    get_test: "t" = False,
    full_lower: "l" = False
):
    if dataset is None:
        if get_test is False:
            raise ValueError(
                "Refusing to download full versions of all datasets. Specify a "
                "dataset or run with --get-test to get test subsets."
            )
        print(
            "No dataset argument provided; downloading all defined dataset "
            "test subsets."
        )
        datasets = [
            d.name
            for d in Path("definitions").iterdir()
            if (d.is_dir() and ("cache" not in d.name))
        ]
    else:
        datasets = [dataset]
    for dataset in sorted(datasets):
        downloader = IndexDownloader(dataset)
        downloader.download_index(
            product_type, get_test, full_lower=full_lower
        )


def check(
    dataset,
    product_type=None,
    *,
    dump_browse: "d" = True,
    dump_kwargs: "k" = None,
    debug: "b" = True,
    nowarn: "w" = False
):
    if dump_kwargs is not None:
        dump_kwargs = literal_eval(dump_kwargs)
    hasher = ProductChecker(dataset)
    hasher.check_product_type(
        product_type, dump_browse, dump_kwargs, debug, nowarn
    )


def test(
    dataset=None,
    product_type=None,
    *,
    regen: "r" = False,
    write: "w" = True,
    debug: "g" = True,
    dump_browse: "d" = False,
    dump_kwargs: "k" = None,
    quiet: "q" = False,
    max_size=0,
    filetypes="",
    skiphash: "s" = False
):
    if len(filetypes) > 0:
        filetypes = {f.lower().strip(".") for f in filetypes.split(" ")}
    if dump_kwargs is not None:
        dump_kwargs = literal_eval(dump_kwargs)
    if dataset is None:
        print("no dataset argument provided; testing all defined datasets")
        datasets = [
            d.name
            for d in Path("definitions").iterdir()
            if (d.is_dir() and ("cache" not in d.name))
        ]
    else:
        datasets = [dataset]
    logs = []
    for dataset in sorted(datasets):
        hasher = ProductChecker(dataset)
        hasher.tracker.paused = True
        try:
            test_logs = hasher.compare_test_hashes(
                product_type,
                regen,
                write,
                debug,
                dump_browse,
                dump_kwargs,
                quiet,
                max_size,
                filetypes,
                skiphash
            )
            if isinstance(test_logs, list):
                logs += test_logs
            else:
                logs += [test_logs]
        except MissingHashError:
            return
        except FileNotFoundError as fnf:
            print(f"Necessary file missing for this dataset: {fnf}")
        except KeyboardInterrupt:
            console_and_log("received keyboard interrupt, halting")
            break
        finally:
            hasher.tracker.outpath.unlink(missing_ok=True)
            hasher.tracker.paused = False
            hasher.tracker.dump()
    if len(logs) > 0:
        import pandas as pd

        pd.concat(logs).to_csv(
            "combined_test_log_latest.csv", index=False
        )


def test_paths(dataset=None, product_type=None):
    if dataset is None:
        print("no dataset argument provided; listing all defined datasets")
        datasets = [
            d.name
            for d in Path(Path(__file__).parent, "definitions").iterdir()
            if (d.is_dir() and ("cache" not in d.name))
        ]
    else:
        datasets = [dataset]
    paths = []
    for dataset in datasets:
        lister = ProductChecker(dataset)
        paths += lister.dump_test_paths(product_type)
    return tuple(chain.from_iterable(paths))


def finalize(dataset=None, product_type=None, product=None, *,
             regen: "r" = False,
             local: "l" = False,
             subset_size: "n" = 1):
    """Creates a test subset (if necessary) and uploads relevant test files to s3."""
    if dataset is None:
        print("Upload requires a dataset argument. We don't want to re-upload all the files in the s3 bucket.")
        return
    else:
        finalizer = CorpusFinalizer(dataset)
        finalizer.create_and_upload_test_subset(product_type, product, subset_size, regen, local)


def index_directory(target, manifest, output="index.csv", debug=False, filters=None):
    """simple wrapper for datasets.directory_to_index"""
    if filters is not None:
        filters = literal_eval(filters)
    directory_to_index(target, manifest, output, debug, filters)


def ix_help(*_, **__):
    print(f"Usage: valid subcommands are: {', '.join(COMMANDS)}.")
