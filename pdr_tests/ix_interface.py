import sys
from ast import literal_eval
from pathlib import Path
from typing import Optional

from .datasets import (
    ProductPicker,
    IndexMaker,
    IndexDownloader,
    ProductChecker,
    CorpusFinalizer,
    directory_to_index,
    MissingHashError,
)
from .definitions import RULES_MODULES
from .settings.base import (
    BROWSE_ROOT,
    DATA_ROOT,
    HEADERS,
    MANIFEST_DIR,
    TEST_CORPUS_BUCKET,
    TRACKER_LOG_DIR,
)
from .utilz.ix_utilz import console_and_log
from .utilz.cli_utilz import cli_action

def validate_dataset(ds: str) -> str:
    """
    Check that 'ds' names a valid data set, i.e. one that has
    selection rules associated with it.
    """
    try:
        # Written this way because we are calling __getitem__
        # for its side effects (i.e. possibly throwing a KeyError).
        # TODO: parse, don't validate. That is, return the
        # RULES_MODULES entry instead of the string.
        RULES_MODULES.__getitem__(ds)
        return ds
    except KeyError as e:
        # argparse does not recognize KeyError as a legitimate thing
        # for 'type' hooks to throw.  If we convert it to a ValueError,
        # we'll get a shitty error message.  TODO: don't rely on
        # 'type' for argument validation, do it in CLIAction with
        # better error reporting designed in.
        raise SystemExit(
            f"error: invalid data set {ds!r}: {e.__cause__}"
        )

# Note: these are not actually accepted by all subcommands, only by
# those subcommands whose run function has a matching argument.
COMMON_ARGUMENTS = {
    "dataset": {
        "help": "PDS data set to be processed",
        "parse": validate_dataset,
    },
    "product_type": {
        "help": "Process only data products of this type",
    },
    "debug": {
        "short": ["b", "g"],
        "help": "Enable debug mode in PDR",
        "neg_help": "Disable debug mode in PDR",
    },
    "warn": {
        "short": "w",
        "help": "Print warnings",
        "neg_help": "Do not print warnings",
    },
    "quiet": {
        "short": "q",
        "help": "Print only errors",
    },
    "dump_browse": {
        "short": "d",
        "help": "Generate readable 'browse products' for each product",
        "neg_help": "Do not generate readable 'browse products' for each product",
    },
    "dump_kwargs": {
        "short": "k",
        "help": (
            "Additional keyword arguments passed to pdr.Data.dump_browse"
            " (expects a Python dictionary literal)"
        ),
    },
}


@cli_action(
    manifest_dir = {
        "help": "Directory containing manifest .parquet files",
    },
    **COMMON_ARGUMENTS
)
def sort(
    dataset: str,
    product_type: Optional[str] = None,
    *,
    manifest_dir: Optional[Path] = None,
):
    """
    Filter a manifest down to a single data set, using selection rules.
    """
    if manifest_dir is None:
        manifest_dir = MANIFEST_DIR
    picker = ProductPicker(dataset, DATA_ROOT, BROWSE_ROOT)
    picker.make_product_list(manifest_dir, product_type)


@cli_action(
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
    **COMMON_ARGUMENTS,
)
def pick(
    dataset: str,
    product_type: Optional[str] = None,
    *,
    subset_size: int = 200,
    max_size: int = 8000,
):
    """
    Choose a random subset of a data set for manual systematic testing.
    """
    picker = ProductPicker(dataset, DATA_ROOT, BROWSE_ROOT)
    picker.random_picks(product_type, subset_size, max_size)


@cli_action(
    dry_run = {
        "short": "d",
        "help": "Do not actually download any labels"
    },
    **COMMON_ARGUMENTS,
)
def index(
    dataset: str,
    product_type: Optional[str] = None,
    *,
    dry_run: bool = False,
):
    """
    Download detached labels and create a comprehensive index for the
    products selected by 'ix pick'.
    """
    indexer = IndexMaker(dataset, DATA_ROOT, BROWSE_ROOT)
    indexer.get_labels(product_type, dry_run, add_req_headers=HEADERS)
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
    **COMMON_ARGUMENTS,
)
def download(
    dataset: Optional[str] = None,
    product_type: Optional[str] = None,
    *,
    get_test: bool = False,
    full_lower: bool = False,
):
    """
    Download all of the indexed products for a data set.
    """
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
        datasets = sorted(RULES_MODULES.keys())
    else:
        datasets = [dataset]
    for dataset in datasets:
        downloader = IndexDownloader(dataset, DATA_ROOT, BROWSE_ROOT)
        downloader.download_index(
            product_type, get_test, full_lower=full_lower,
            add_req_headers=HEADERS,
        )


@cli_action(**COMMON_ARGUMENTS)
def check(
    dataset: str,
    product_type: Optional[str] = None,
    *,
    debug: bool = True,
    warn: bool = True,
    dump_browse: bool = True,
    dump_kwargs: Optional[str] = None,
):
    """
    Attempt to use PDR to read every indexed product in a data set.
    """
    if dump_kwargs is not None:
        dump_kwargs = literal_eval(dump_kwargs)
    hasher = ProductChecker(dataset, DATA_ROOT, BROWSE_ROOT, TRACKER_LOG_DIR)
    hasher.check_product_type(
        product_type, dump_browse, dump_kwargs, debug, not warn
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
        "help": "???",
    },
    max_size = {
        "help": "Maximum size of file to process, in *decimal* megabytes",
    },
    filetypes = {
        "help": "Space-separated list of file extensions to process",
    },
    **COMMON_ARGUMENTS,
)
def test(
    dataset: Optional[str] = None,
    product_type: Optional[str] = None,
    *,
    max_size: int = 0,
    filetypes: str = "",
        regen: bool = False,
    write: bool = True,
    debug: bool = True,
    quiet: bool = False,
    skip_hash: bool = False,
    dump_browse: bool = False,
    dump_kwargs: Optional[str] = None,
):
    """
    Generate and/or compare test hashes for a data set (or all data sets).
    """
    if len(filetypes) > 0:
        filetypes = {f.lower().strip(".") for f in filetypes.split(" ")}
    if dump_kwargs is not None:
        dump_kwargs = literal_eval(dump_kwargs)
    if dataset is None:
        print("no dataset argument provided; testing all defined datasets")
        datasets = sorted(RULES_MODULES.keys())
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


@cli_action(**COMMON_ARGUMENTS)
def test_paths(
    dataset: Optional[str] = None,
    product_type: Optional[str] = None,
):
    """
    Print the names of the test inputs for a data set (or all data sets).
    """
    if dataset is None:
        sys.stderr.write(
            "no dataset argument provided; listing all defined datasets\n"
        )
        datasets = sorted(RULES_MODULES.keys())
    else:
        datasets = [dataset]
    for dataset in datasets:
        lister = ProductChecker(dataset, DATA_ROOT, BROWSE_ROOT,
                                TRACKER_LOG_DIR)
        for test_paths in lister.dump_test_paths(product_type):
            for path in test_paths:
                print(path)


@cli_action(
    subset_size = {
        "short": "n",
        "help": "Number of files to select for each product type (default: 1)",
    },
    bucket = {
        "short": "b",
        "help": "AWS S3 bucket to upload files to",
    },
    regen = {
        "short": "r",
        "help": "Discard and regenerate existing test index files",
    },
    local = {
        "short": "l",
        "help": "Operate locally; do not upload anything to S3",
    },
    product = {
        "help": "Select only files with this string in their product name",
    },
    **COMMON_ARGUMENTS,
)
def finalize(
    dataset: str,
    product_type: Optional[str] = None,
    product: Optional[str] = None,
    *,
    regen: bool = False,
    local: bool = False,
    subset_size: int = 1,
    bucket: Optional[str] = None
):
    """Create a test subset (if necessary) and upload relevant test files to S3."""
    if bucket is None:
        bucket = TEST_CORPUS_BUCKET
    if not dataset:
         raise ValueError(
             "finalize requires a dataset argument."
         )

    finalizer = CorpusFinalizer(dataset, DATA_ROOT, BROWSE_ROOT)
    finalizer.create_and_upload_test_subset(
        product_type,
        product,
        subset_size,
        regen,
        local,
        bucket,
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
    **COMMON_ARGUMENTS
)
def index_directory(
    target: str,
    manifest: str,
    output: str = "index.csv",
    *,
    debug: bool = False,
    filters: Optional[str] = None,
):
    """Create an index file for the contents of a specific directory."""
    if filters is not None:
        filters = literal_eval(filters)
    directory_to_index(target, manifest, output, debug, filters)


@cli_action(**COMMON_ARGUMENTS)
def count(dataset: Optional[str] = None):
    """
    Count the product types in a data set (or all data sets).
    """
    if dataset is None:
        print("no dataset argument provided; listing all defined datasets")
        cnt = sum(len(s.file_information) for s in RULES_MODULES.values())
    else:
        cnt = len(RULES_MODULES[dataset].file_information)
    print(f"There are {cnt} total product types.")
