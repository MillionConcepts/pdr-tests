"""
This is a dictionary of information about each product type. 
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .parquet file that contains urls, file sizes, etc., scraped directly
from the hosting institution for this product type. for some data sets, all
urls will be found in the same .parquet file; for others, they may be split
between nodes or scraping sessions.

fn_must_contain: a list of strings that must be in the file name (not counting
directories, domains, etc.) to differentiate it from the other types in the
manifest file

url_must_contain: an optional additional list of strings that must be in the 
url (counting the entire url) to differentiate this from other types in the
manifest file. useful for specifying directories.

label: "A" if the labels for this product type are attached; "D" if the labels
are detached.
"""
from pathlib import Path

import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .parquet files
MANIFEST_FILE = Path(MANIFEST_DIR, "plasm_full.parquet")

file_information = {
    # Level 0 primary science data
    # All bit columns; many rows are missing from the tables; format spec doesn't match
    # number of bytes in file
    # "edr_pri": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['PRI', '.DAT'],
    #     "url_must_contain": ['LRO-L-CRAT-2-EDR-RAWDATA-V1.0/DATA'],
    #     "label": 'D',
    # },
    # Level 0 secondary science data
    # Each table is consistently missing 1 row
    "edr_sec": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['SEC', '.DAT'],
        "url_must_contain": ['LRO-L-CRAT-2-EDR-RAWDATA-V1.0/DATA'],
        "label": 'D',
    },
    # Level 0 housekeeping data
    # Tables open fine, but ix test throws error:
    # <class 'OverflowError'>: Maximum recursion level reached
    "edr_hk": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['HK', '.DAT'],
        "url_must_contain": ['LRO-L-CRAT-2-EDR-RAWDATA-V1.0/DATA'],
        "label": 'D',
    },
    # Level 1 primary science data
    "cdr_pri": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['PRI', '.TAB'],
        "url_must_contain": ['LRO-L-CRAT-3-CDR-CALIBRATED-V1.0/DATA'],
        "label": 'D',
    },
    # Level 1 secondary science data
    "cdr_sec": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['SEC', '.TAB'],
        "url_must_contain": ['LRO-L-CRAT-3-CDR-CALIBRATED-V1.0/DATA'],
        "label": 'D',
    },
    # Level 1 housekeeping data
    "cdr_hk": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['HK', '.TAB'],
        "url_must_contain": ['LRO-L-CRAT-3-CDR-CALIBRATED-V1.0/DATA'],
        "label": 'D',
    },
    # Level 2 primary science data
    "ddr_pri": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['PRI','.TAB'],
        "url_must_contain": ['LRO-L-CRAT-3_4-DDR-PROCESSED-V1.0/DATA'],
        "label": 'D',
    },
    # Level 2 secondary science data
    "ddr_sec": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['SEC','.TAB'],
        "url_must_contain": ['LRO-L-CRAT-3_4-DDR-PROCESSED-V1.0/DATA'],
        "label": 'D',
    },
    # Level 2 housekeeping data
    "ddr_hk": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['HK','.TAB'],
        "url_must_contain": ['LRO-L-CRAT-3_4-DDR-PROCESSED-V1.0/DATA'],
        "label": 'D',
    },
}
