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
	
# start GIADA data products
    # EDRs
    "EDR_giada": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-gia-2-', '/data'],
        "label": "D",
    },
    # RDRs
    "RDR_giada": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-gia-3-', '/data'],
        "label": "D",
    },
    # DDRs
    "DDR_giada": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-gia-5-', '/data'],
        "label": "D",
    },
	
# start MIDAS data products
    # RDRs
    # frequency_series and time_series tables do not open
#     "RDR_midas_dat": {
#         "manifest": SB_FILE,
#         "fn_must_contain": ['.dat'],
#         "url_must_contain": ['-midas-3-', '/data'],
#         "label": "D",
#     },
    "RDR_midas_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-midas-3-', '/data'],
        "label": "D",
    },
    "RDR_midas_tab": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-midas-3-', '/data'],
        "label": "D",
    },
    # DDRs
    "DDR_midas_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-midas-5-', '/data'],
        "label": "D",
    },
    "DDR_midas_tab": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-midas-5-', '/data'],
        "label": "D",
    },
	
}


