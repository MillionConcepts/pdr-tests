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
    
# start RPCICA
    "EDR_RPCICA": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcica-2-', '/data'],
        "label": "D",
    },
    "RDR_RPCICA": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcica-3-', '/data'],
        "label": "D",
    },
    "REFDR_RPCICA": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcica-4-', '/data'],
        "label": "D",
    },
    "DDR_RPCICA": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcica-5-', '/data'],
        "label": "D",
    },
    
# start RPCIES
    "EDR_RPCIES": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcies-2-', '/data'],
        "label": "D",
    },
    "RDR_RPCIES": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcies-3-', '/data'],
        "label": "D",
    },
    "DDR_RPCIES": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcies-5-', '/data'],
        "label": "D",
    },
    
# start RPCLAP
    "EDR_RPCLAP": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpclap-2-', '/data'],
        "label": "D",
    },
    "RDR_RPCLAP": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpclap-3-', '/data'],
        "label": "D",
    },
    "DDR_RPCLAP": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpclap-5-', '/data'],
        "label": "D",
    },
    
# start RPCMAG
    "EDR_RPCMAG": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcmag-2-', '/data'],
        "label": "D",
    },
    "RDR_RPCMAG": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcmag-3-', '/data'],
        "label": "D",
    },
    "REFDR_RPCMAG": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcmag-4-', '/data'],
        "label": "D",
    },
    
# start RPCMIP
    "RPCMIP": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rpcmip-3-', '/data'],
        "label": "D",
    },

}


