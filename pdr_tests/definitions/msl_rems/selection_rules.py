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

from itertools import product

# variables naming specific parquet files in node_manifests
ATM_FILE = "atm"

file_information = {
    # Rover Environmental Monitoring Station (REMS)
    # RDRs
    "rdr_rtl": {
        "manifest": ATM_FILE,
        "fn_must_contain": ["RTL", ".TAB"],
        "url_must_contain": ["mslrem_1001/DATA/SOL"],
        "label": "D",
    },
    "rdr_rnv": {
        "manifest": ATM_FILE,
        "fn_must_contain": ["RNV", ".TAB"],
        "url_must_contain": ["mslrem_1001/DATA/SOL"],
        "label": "D",
    },
    "rdr_rmd": {
        "manifest": ATM_FILE,
        "fn_must_contain": ["RMD", ".TAB"],
        "url_must_contain": ["mslrem_1001/DATA/SOL"],
        "label": "D",
    },
    "rdr_adr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ["ADR", ".TAB"],
        "url_must_contain": ["mslrem_1001/DATA/SOL"],
        "label": "D",
    },
    # RDR UV corrected products
    "corrected": {
        "manifest": ATM_FILE,
        "fn_must_contain": [".TAB"],
        "url_must_contain": ["mslrem_1001/DATA_UV_CORRECTED"],
        "label": "D",
    },
}

# EDRs
base = {
    "manifest": ATM_FILE,
    "url_must_contain": ["mslrem_0001/DATA"],
    "label": "D",
}
for ptype in (
    'ACQ', 'ENG', 'ERROR', 'GTSGAIN', 'HSREG', 'RESET', 
    'SLEEP', 'SP', 'GTSCAL', 'HSDEF', 'EVENT'
    ):
    info = base | {"fn_must_contain": [ptype, ".TAB"]}
    file_information[f"edr_{ptype}"] = info

