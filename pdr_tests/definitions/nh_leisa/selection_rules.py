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

# shorthand variables for specific .csv files
SB_FILE = Path(MANIFEST_DIR, "tiny.parquet")

file_information = {
    # post-launch raw and calibrated data
    "launch_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-leisa-2-launch-v1.1/data'],
        "label": "D",
    },
    "launch_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-leisa-3-launch-v1.1/data'],
        "label": "D",
    },
    # jupiter flyby raw and calibrated data
    "jupiter_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-j-leisa-2-jupiter-v1.1/data'],
        "label": "D",
    },
    "jupiter_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-j-leisa-3-jupiter-v1.1/data'],
        "label": "D",
    },
    # pluto cruise raw and calibrated data
    "cruise_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-leisa-2-plutocruise-v1.0/data'],
        "label": "D",
    },
    "cruise_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-leisa-3-plutocruise-v1.0/data'],
        "label": "D",
    },
    # pluto encounter raw and calibrated data
    "pluto_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-p-leisa-2-pluto-v3.0/data'],
        "label": "D",
    },
    "pluto_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-p-leisa-3-pluto-v3.0/data'],
        "label": "D",
    },
}