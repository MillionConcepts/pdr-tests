import sys
from ast import literal_eval
from pathlib import Path
from typing import Optional

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
from pdr_tests.settings import SETTINGS
from pdr_tests.utilz.ix_utilz import (
    clean_logs,
    console_and_log,
    download_datasets,
    list_datasets,
)
from pdr_tests.utilz.cli_utilz import cli_action


def validate_dataset(ds: str) -> str:
    """
    Check that 'ds' names a valid data set, i.e. one that has
    selection rules associated with it.
    """
    # Written this way because we are calling __getitem__
    # for its side effects (i.e. possibly throwing a KeyError).
    # TODO: parse, don't validate. That is, return the
    # RULES_MODULES entry instead of the string.
    try:
        RULES_MODULES.__getitem__(ds)
        return ds
    except KeyError as e:
        # It improves the diagnostics slightly if we unwrap the
        # KeyError and rethrow the original ModuleNotFoundError.
        if e.__cause__ is not None:
            raise e.__cause__

# Define help, short options, etc. for each option used by two or
# more actions here, so that they are handled consistently across
# all actions.  They will only be available to actions whose
# execution function actually has a matching argument.
# All options whose default comes from settings should also be here
# even if they are only used by one action.
cli_action.add_common_argspecs(
    dataset = {
        "help": "PDS data set to be processed",
        "parse": validate_dataset,
    },
    product_type = {
        "help": "Process only data products of this type",
    },
    manifest_dir = {
        "help": "Directory containing manifest .parquet files",
    },
    data_root = {
        "help": "Directory tree storing copies of PDS data for testing",
    },
    browse_root = {
        "help": "Directory tree where browse products will be written",
    },
    tracker_log_dir = {
        "help": "Directory to store tracker logs in",
    },
    headers = {
        "help": (
            "Additional HTTP request headers to send when downloading files"
            " (expects a Python dictionary literal)"
        ),
    },
    bucket = {
        "short": "b",
        "help": "AWS S3 bucket to use",
    },

    pdr_debug = {
        "help": "Enable debug mode in PDR",
        "neg_help": "Don't enable debug mode in PDR",
    },
    warn = {
        "short": "w",
        "help": "Print warnings",
        "neg_help": "Do not print warnings",
    },
    quiet = {
        "short": "q",
        "help": "Print only errors",
    },
    subset_size = {
        "short": "s",
        "help": (
            "Maximum number of files to select per product type"
            " (default: 200)"
        ),
    },
    max_size = {
        "short": "m",
        "help": (
            "Maximum size of each file to select, in *decimal* megabytes"
            " (default: 8 GB)"
        ),
    },
    dump_browse = {
        "short": "d",
        "help": "Generate readable 'browse products' for each product",
        "neg_help": "Do not generate readable 'browse products' for each product",
    },
    dump_kwargs = {
        "short": "k",
        "help": (
            "Additional keyword arguments passed to pdr.Data.dump_browse"
            " (expects a Python dictionary literal)"
        ),
    },
)


@cli_action
def sort(
    dataset: str,
    product_type: Optional[str] = None,
    *,
    manifest_dir: Optional[Path] = None,
    data_root: Optional[Path] = None,
    browse_root: Optional[Path] = None,
):
    """
    Filter a manifest down to a single data set, using selection rules.
    """
    if manifest_dir is None:
        manifest_dir = SETTINGS.manifest_dir
    if data_root is None:
        data_root = SETTINGS.data_root
    if browse_root is None:
        browse_root = SETTINGS.browse_root
    picker = ProductPicker(dataset, data_root, browse_root)
    picker.make_product_list(manifest_dir, product_type)


@cli_action
def pick(
    dataset: str,
    product_type: Optional[str] = None,
    *,
    subset_size: int = 200,
    max_size: int = 8000,
    data_root: Optional[Path] = None,
    browse_root: Optional[Path] = None,
):
    """
    Choose a random subset of a data set for manual systematic testing.
    """
    if data_root is None:
        data_root = SETTINGS.data_root
    if browse_root is None:
        browse_root = SETTINGS.browse_root
    picker = ProductPicker(dataset, data_root, browse_root)
    picker.random_picks(product_type, subset_size, max_size)


@cli_action(
    dry_run = {
        "short": "d",
        "help": "Do not actually download any labels"
    },
)
def index(
    dataset: str,
    product_type: Optional[str] = None,
    *,
    dry_run: bool = False,
    data_root: Optional[Path] = None,
    browse_root: Optional[Path] = None,
    headers: Optional[str] = None,
):
    """
    Download detached labels and create a comprehensive index for the
    products selected by 'ix pick'.
    """
    if data_root is None:
        data_root = SETTINGS.data_root
    if browse_root is None:
        browse_root = SETTINGS.browse_root
    if headers is None:
        headers = SETTINGS.headers
    else:
        headers = literal_eval(headers)
    indexer = IndexMaker(dataset, data_root, browse_root)
    indexer.get_labels(product_type, dry_run, add_req_headers=headers)
    if dry_run:
        return
    indexer.write_subset_index(product_type)


@cli_action(
    get_test = {
        "short": "t",
        "help": "Download only the files that would be used by 'ix test'",
    },
    full_lower = {
        "short": "l",
        "help": "Try lowercasing the names of any files that fail to download"
    },
)
def download(
    dataset: Optional[str] = None,
    product_type: Optional[str] = None,
    *,
    get_test: bool = False,
    full_lower: bool = False,
    data_root: Optional[Path] = None,
    browse_root: Optional[Path] = None,
    headers: Optional[str] = None,
):
    """
    Download all of the indexed products for a data set.
    """
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
    if data_root is None:
        data_root = SETTINGS.data_root
    if browse_root is None:
        browse_root = SETTINGS.browse_root
    if headers is None:
        headers = SETTINGS.headers
    else:
        headers = literal_eval(headers)
    for dataset in datasets:
        downloader = IndexDownloader(dataset, data_root, browse_root)
        downloader.download_index(
            product_type, get_test, full_lower=full_lower,
            add_req_headers=headers,
        )


@cli_action
def check(
    dataset: str,
    product_type: Optional[str] = None,
    *,
    pdr_debug: bool = True,
    warn: bool = True,
    dump_browse: bool = True,
    dump_kwargs: Optional[str] = None,
    data_root: Optional[Path] = None,
    browse_root: Optional[Path] = None,
    tracker_log_dir: Optional[Path] = None,
):
    """
    Attempt to use PDR to read every indexed product in a data set.
    """
    if data_root is None:
        data_root = SETTINGS.data_root
    if browse_root is None:
        browse_root = SETTINGS.browse_root
    if tracker_log_dir is None:
        tracker_log_dir = SETTINGS.tracker_log_dir
    if dump_kwargs is not None:
        dump_kwargs = literal_eval(dump_kwargs)
    hasher = ProductChecker(dataset, data_root, browse_root, tracker_log_dir)
    hasher.check_product_type(
        product_type, dump_browse, dump_kwargs, pdr_debug, not warn
    )


@cli_action(
    regen = {
        "short": "r",
        "help": "Regenerate hashes for all tested products",
    },
    write = {
        "short": "w",
        "help": "Write new hashes for products without recorded hashes",
        "neg_help": "Don't write new hashes for products without recorded hashes",
    },
    skip_hash = {
        "short": "s",
        "help": "Don't check any hashes, just load each test input (like 'ix check')",
    },
    max_size = {
        "help": "Maximum size of file to process, in *decimal* megabytes",
    },
    filetypes = {
        "help": "Space-separated list of file extensions to process",
    },
)
def test(
    dataset: Optional[str] = None,
    product_type: Optional[str] = None,
    *,
    max_size: int = 0,
    filetypes: str = "",
    regen: bool = False,
    write: bool = True,
    pdr_debug: bool = True,
    quiet: bool = False,
    skip_hash: bool = False,
    dump_browse: bool = False,
    dump_kwargs: Optional[str] = None,
    data_root: Optional[Path] = None,
    browse_root: Optional[Path] = None,
    tracker_log_dir: Optional[Path] = None,
):
    """
    Generate and/or compare test hashes for a data set (or all data sets).
    """
    if data_root is None:
        data_root = SETTINGS.data_root
    if browse_root is None:
        browse_root = SETTINGS.browse_root
    if tracker_log_dir is None:
        tracker_log_dir = SETTINGS.tracker_log_dir
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
        hasher = ProductChecker(dataset, data_root, browse_root,
                                tracker_log_dir)
        hasher.tracker.paused = True
        try:
            test_logs = hasher.compare_test_hashes(
                product_type,
                regen,
                write,
                pdr_debug,
                dump_browse,
                dump_kwargs,
                quiet,
                max_size,
                filetypes,
                skip_hash
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


@cli_action
def test_paths(
    dataset: Optional[str] = None,
    product_type: Optional[str] = None,
    *,
    data_root: Optional[Path] = None,
    browse_root: Optional[Path] = None,
    tracker_log_dir: Optional[Path] = None,
):
    """
    Print the names of the test inputs for a data set (or all data sets).
    """
    if data_root is None:
        data_root = SETTINGS.data_root
    if browse_root is None:
        browse_root = SETTINGS.browse_root
    if tracker_log_dir is None:
        tracker_log_dir = SETTINGS.tracker_log_dir
    if dataset is None:
        print("no dataset argument provided; listing all defined datasets")
        datasets = list_datasets()
    else:
        datasets = [dataset]
    for dataset in datasets:
        lister = ProductChecker(dataset, data_root, browse_root,
                                tracker_log_dir)
        for test_paths in lister.dump_test_paths(product_type):
            for path in test_paths:
                print(path)


@cli_action(
    product = {
        "help": "Select only files with this string in their product name",
    },
    regen = {
        "short": "r",
        "help": "Discard and regenerate existing test index files",
    },
    local = {
        "short": "l",
        "help": "Operate locally; do not upload anything to S3",
    },
    subset_size = {
        "short": "n",
        "help": "Number of files to select for each product type (default: 1)",
    },
)
def finalize(
    dataset: Optional[str] = None,
    product_type: Optional[str] = None,
    product: Optional[str] = None,
    *,
    regen: bool = False,
    local: bool = False,
    subset_size: int = 1,
    bucket: Optional[str] = None,
    data_root: Optional[Path] = None,
    browse_root: Optional[Path] = None,
):
    """Create a test subset (if necessary) and upload relevant test files to S3."""
    if bucket is None:
        bucket = SETTINGS.test_corpus_bucket
    if bucket is None:
        raise ValueError(
            "The name of the s3 bucket you would like to upload to must be"
            " given via the settings or via --bucket."
        )
    if dataset is None:
        raise ValueError(
            "finalize requires a dataset argument. We don't want to re-upload"
            " all the files in the s3 bucket."
        )
    if data_root is None:
        data_root = SETTINGS.data_root
    if browse_root is None:
        browse_root = SETTINGS.browse_root

    finalizer = CorpusFinalizer(dataset, data_root, browse_root)
    finalizer.create_and_upload_test_subset(
        product_type, product, subset_size, regen, local, bucket,
    )


@cli_action(
    target = {
        "help": "Directory to be indexed",
    },
    manifest = {
        "help": "Manifest file for contents of the target directory",
    },
    output = {
        "help": "Name of output file",
    },
    filters = {
        "help": "Only index files matching these filter rules",
    },
    stop_on_first_error = {
        "help": ("If any error is encountered, stop immediately;"
                 " do not go on to other files in the directory.")
    },
)
def index_directory(
    target: str,
    manifest: str,
    output: str = "index.csv",
    *,
    stop_on_first_error: bool = False,
    filters: Optional[str] = None,
):
    """Create an index file for the contents of a specific directory."""
    if filters is not None:
        filters = literal_eval(filters)
    directory_to_index(target, manifest, output, stop_on_first_error, filters)


@cli_action
def count(dataset: Optional[str] = None):
    """
    Count the product types in a data set (or all data sets).
    """
    if dataset is None:
        print("no dataset argument provided; listing all defined datasets")
        datasets = list_datasets()
    else:
        datasets = [dataset]
    cnt = 0
    for dataset in datasets:
        cnt += len(RULES_MODULES[dataset].file_information)
    print(f"There are {cnt} total product types.")


@cli_action(
    clean = {
        "help": "Delete local files not present on the remote",
    },
    force = {
        "help": "Re-download everything on the remote"
    },
    replace_newer = {
        "help": "Replace files more recently modified on the remote"
    },
    replace_offsize = {
        "help": "Replace files whose sizes don't match the remote",
        "neg_help": "Don't replace files whose sizes don't match the remote",
    },
    dry_run = {
        "short": "d",
        "help": "Do not actually sync any files"
    },
)
def sync(
    dataset: Optional[str] = None,
    *,
    clean: bool = False,
    force: bool = False,
    replace_newer: bool = False,
    replace_offsize: bool = True,
    dry_run: bool = False,
    bucket: Optional[str] = None,
):
    """
    Download test files from an S3 bucket.
    """
    if bucket is None:
        bucket = SETTINGS.test_corpus_bucket
    if bucket is None:
        raise ValueError(
            "The name of the s3 bucket you would like to sync with must be "
            " given via settings or via --bucket."
        )
        return
    if dataset is None:
        print("no dataset argument provided; syncing all defined datasets")
        datasets = list_datasets()
    else:
        datasets = [dataset]
    download_datasets(
        datasets,
        bucket_name=bucket,
        clean=clean,
        force=force,
        replace_newer=replace_newer,
        replace_offsize=replace_offsize,
        dry_run=dry_run
    )


@cli_action
def clean():
    """
    Erase most pdr-tests log files.
    """
    clean_logs()
