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

# variables naming specific parquet files in node_manifests
ATM_FILE = "atm"

file_information = {
    "atm_phxao": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ["phxao_1001/DATA"],
        "label": "D",
    },
    "atm_phxase1": {
        "manifest": ATM_FILE,
        "url_must_contain": ["phxase_0001/DATA"],
        "fn_must_contain": ['.TAB'],
        "label": "D",
    },
    "atm_phxase2": {
        "manifest": ATM_FILE,
        "url_must_contain": ["phxase_0002/DATA"],
        "fn_must_contain": ['.TAB'],
        "label": "D",
    },
    "atm_phxwnd": {
        "manifest": ATM_FILE,
        "url_must_contain": ["phxwnd_0001/DATA"],
        "fn_must_contain": ['.TAB'],
        "label": "D",
    },
}
