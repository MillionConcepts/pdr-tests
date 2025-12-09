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
PSA = "img_esa_ve"

file_information = {
    # ASPERA4

    # EDR
    "NPI_NORMAL": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "NPI", "NORMAL"],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    # RDR
    "NPI_HK3MUXX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "NPI", "HK3MUXX"],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    # literally only 1 data file of this type
    "SWM": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', 'SWM'],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    "ELS_ENGXXXX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "ELS", "ENGXXXX"],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    "ELS_HK3MUXX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB',  "ELS", "HK3MUXX"],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    "ELS_E128A16": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB',  "ELS", "E128A16"],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    "IMA_HK3IMAX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "IMA", "HK3IMAX"],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    "IMA_HK3MUXX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB',  "IMA", "HK3MUXX"],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    "IMA_M24XXXX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "IMA", "M24XXXX"],
        "url_must_contain": ['ASPERA4'],
        "label": "D",
    },
    "NPD_BIN16D0": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "BIN16D0"],
        "url_must_contain": ['ASPERA4', "NPD"],
        "label": "D",
    },
    "NPD_TOFXXXX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB',  "TOFXXXX"],
        "url_must_contain": ['ASPERA4', "NPD"],
        "label": "D",
    },
    "NPD_HK3MUXX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "HK3MUXX"],
        "url_must_contain": ['ASPERA4', "NPD"],
        "label": "D",
    },
    "NPD_BIN16D1": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB',  "BIN16D1"],
        "url_must_contain": ['ASPERA4', "NPD"],
        "label": "D",
    },
    "NPD_BIN16D2": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "BIN16D2"],
        "url_must_contain": ['ASPERA4', "NPD"],
        "label": "D",
    },
    "NPD_RAWXXXX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', "RAWXXXX"],
        "url_must_contain": ['ASPERA4', "NPD"],
        "label": "D",
    },
}
