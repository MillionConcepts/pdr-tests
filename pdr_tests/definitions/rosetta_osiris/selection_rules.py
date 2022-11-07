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

# Note about .img vs .fit products:
# The .img products have attached labels, the .fit products have detached.
# pdr will try to open the .img products with the detached labels if they are in the same directory.
# In reality, the files being opened by pdr using the detached labels will be the .fit products.
# To open the .img products, make sure they are in a separate directory from the .fit and .lbl files.

file_information = {
    
# start narrow angle camera data products
	"EDR_narrow_fit": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['-osinac-2-', '/data/fit'],
        "label": "D",
    },
    "EDR_narrow_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-osinac-2-', '/data/img'],
        "label": "A",
    },
    "RDR_narrow_fit": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['/data/fit'],
        "url_regex": [r'(-osinac-3-)|(-osinac-4-)'],
        "label": "D",
    },
    "RDR_narrow_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['/data/img'],
        "url_regex": [r'(-osinac-3-)|(-osinac-4-)'],
        "label": "A",
    },
    "DDR_narrow": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-osinac-5-', '/data'],
        "label": "A",
    },
    
# start wide angle camera data products
    "EDR_wide_fit": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['-osiwac-2-', '/data/fit'],
        "label": "D",
    },
    "EDR_wide_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-osiwac-2-', '/data/img'],
        "label": "A",
    },
    "RDR_wide_fit": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['/data/fit'],
        "url_regex": [r'(-osiwac-3-)|(-osiwac-4-)'],
        "label": "D",
    },
    "RDR_wide_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['/data/img'],
        "url_regex": [r'(-osiwac-3-)|(-osiwac-4-)'],
        "label": "A",
    },
    "DDR_wide": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-osiwac-5-', '/data'],
        "label": "A",
    },
    
    # shape models - level 5 products
    "shape": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.wrl'],
        "url_must_contain": ['-osinac_osiwac-5-', '-shape-', '/data'],
        "label": "D",
    },
    
}


