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

# variables naming specific parquet files in node_manifests
GEO_MESSENGER_FILE = "geomessenger"

file_information = {
    "ns_CDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['grns', "/cdr", '-ns-'],
        "label": "D",
    },
    "ns_DDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['grns', "/ddr", '-ns-'],
        "label": "D",
    },
    # opens from PDS4 labels, PDS3 labels give warning: cannot reshape array of size 64800 into shape (360,720)
    "grs_DAP": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": ['grs_dap', '.img'],
        "url_must_contain": ['grns', 'maps'],
        "label": ('.img', '.xml'),
    },
    "grs_CDRRDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['grns', '/grs_eng'],
        "label": ('.dat', '.xml'),
    },
    "ns_EDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['grns', "-ns-rawdata-"],
        "label": ('.dat', '.xml'),
    },
    "grs_EDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['grns', '-grs-rawdata-'],
        "label": "D",
    },
}
