"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .parquet file that contains urls, file sizes, etc., scraped
directly from the hosting institution for this product type. for some data
sets, all urls will be found in the same .parquet file; for others, they may
be split between nodes or scraping sessions.

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

# shorthand variables for specific .csv files
ATM_FILE = Path(MANIFEST_DIR, "atm.parquet")
PPI_FILE = Path(MANIFEST_DIR, "plasm_full.parquet")

file_information = {
    
    # Derived Triton atmospheric profile
    "derived": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vg_2499/data'],
        "label": "D",
    },
    # Low-level RSS data from Saturn and Titan occultations. Mirrored at RMS
    # (support not planned; labels are missing pointers to the data files)
##    "odr": {
##        "manifest": PPI_FILE,
##        "fn_must_contain": ['.ODR'],
##        "url_must_contain": ['VG', 'RSS-1-ROCC', '/DATA'],
##        "label": "D",
##    },
}

