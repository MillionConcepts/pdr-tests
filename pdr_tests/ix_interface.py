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
from pdr_tests.definitions import RULES_MODULES
from pdr_tests.settings.base import (
    BROWSE_ROOT,
    DATA_ROOT,
    HEADERS,
    MANIFEST_DIR,
    TEST_CORPUS_BUCKET,
    TRACKER_LOG_DIR,
)
from pdr_tests.utilz.ix_utilz import (
    clean_logs,
    console_and_log,
    download_datasets,
    list_datasets,
)


COMMANDS = [
    "sort",
    "pick",
    "index",
    "download",
    "check",
    "finalize",
    "test",
    "index_directory",
    "test_paths",
    "count",
    "sync",
    "clean"
]


def sort(dataset, product_type=None, manifest_dir=None):
    if manifest_dir is not None:
        manifest_dir = Path(manifest_dir)
    else:
        manifest_dir = MANIFEST_DIR
    picker = ProductPicker(dataset, DATA_ROOT, BROWSE_ROOT)
    picker.make_product_list(manifest_dir, product_type)


def pick(
    dataset, product_type=None, *, subset_size: "s" = 200, max_size: "m" = 8000
):
    picker = ProductPicker(dataset, DATA_ROOT, BROWSE_ROOT)
    picker.random_picks(product_type, subset_size, max_size)


def index(dataset, product_type=None, *, dry_run: "d" = False):
    indexer = IndexMaker(dataset, DATA_ROOT, BROWSE_ROOT)
    indexer.get_labels(product_type, dry_run, add_req_headers=HEADERS)
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
                "Refusing to download full versions of all datasets. Specify "
                "a dataset or run with --get-test to get test subsets."
            )
        print(
            "No dataset argument provided; downloading all defined dataset "
            "test subsets."
        )
        datasets = list_datasets()
    else:
        datasets = [dataset]
    for dataset in datasets:
        downloader = IndexDownloader(dataset, DATA_ROOT, BROWSE_ROOT)
        downloader.download_index(
            product_type, get_test, full_lower=full_lower,
            add_req_headers=HEADERS,
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
    hasher = ProductChecker(dataset, DATA_ROOT, BROWSE_ROOT, TRACKER_LOG_DIR)
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
        datasets = list_datasets()
    else:
        datasets = [dataset]
    logs = []
    for dataset in datasets:
        hasher = ProductChecker(dataset, DATA_ROOT, BROWSE_ROOT, TRACKER_LOG_DIR)
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
            logs += test_logs
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
        datasets = list_datasets()
    else:
        datasets = [dataset]
    paths = []
    for dataset in datasets:
        lister = ProductChecker(dataset, DATA_ROOT, BROWSE_ROOT)
        paths += lister.dump_test_paths(product_type)
    return tuple(chain.from_iterable(paths))


def finalize(
    dataset=None,
    product_type=None,
    product=None,
    *,
    regen: "r" = False,
    local: "l" = False,
    subset_size: "n" = 1,
    bucket: "b" = None,
):
    """
    Creates a test subset (if necessary) and uploads relevant test files to
    s3.
    """
    if dataset is None:
        raise ValueError(
            "finalize requires a dataset argument. We don't want to re-upload "
            "all the files in the s3 bucket."
        )
    if bucket is None:
        bucket = TEST_CORPUS_BUCKET

    finalizer = CorpusFinalizer(dataset, DATA_ROOT, BROWSE_ROOT)
    finalizer.create_and_upload_test_subset(
        product_type, product, subset_size, regen, local, bucket,
    )


def index_directory(
    target, manifest, output="index.csv", debug=False, filters=None
):
    """simple wrapper for datasets.directory_to_index"""
    if filters is not None:
        filters = literal_eval(filters)
    directory_to_index(target, manifest, output, debug, filters)


def ix_help(*_, **__):
    print(f"Usage: valid subcommands are: {', '.join(COMMANDS)}.")


def count(dataset=None):
    if dataset is None:
        print("no dataset argument provided; listing all defined datasets")
        datasets = list_datasets()
    else:
        datasets = [dataset]
    cnt = 0
    for dataset in datasets:
        cnt += len(RULES_MODULES[dataset].file_information)
    print(f"There are {cnt} total product types.")


def sync(
    dataset=None,
    clean=False,
    force=False,
    replace_newer=False,
    replace_offsize=True,
    dry_run=False
):
    if TEST_CORPUS_BUCKET is None:
        print(
            "The name of the bucket you would like to sync with must be "
            "given as TEST_CORPUS_BUCKET in pdr_tests.settings.user."
        )
        return
    if dataset is None:
        print("no dataset argument provided; syncing all defined datasets")
        datasets = list_datasets()
    else:
        datasets = [dataset]
    download_datasets(
        datasets,
        bucket_name=TEST_CORPUS_BUCKET,
        clean=clean,
        force=force,
        replace_newer=replace_newer,
        replace_offsize=replace_offsize,
        dry_run=dry_run
    )


def clean():
    clean_logs()
