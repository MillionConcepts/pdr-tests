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

# shorthand variables for specific .parquet files
GEO_FILE = "geomer"

file_information = {
    # MER 1 and 2 uhfd (ultra-high frequency doppler) products; ascii tables
    "uhfd": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['/uhf'],
        "url_regex": [r'mer[12]-m-rss-1-edr-v1'],
        "label": "D",
    },
    # MER 1 and 2 odf products; binary tables
    # volumes: mer1rs_0001, mer1rs_0002, mer2rs_0001
    "odf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['/odf'],
        "url_regex": [r'mer[12]-m-rss-1-edr-v1/((mer1rs)|(mer2rs_0001))'],
        "label": "D",
    },
    # mer2rs_0002 -- several table pointers are opening wrong
    # The labels miscount how many rows are in some tables. The problem starts 
    # with the ODF3B table's ROWS value, and miscounted bytes propagate through 
    # the tables from there
    "odf_unsupported": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['mer2-m-rss-1-edr-v1/mer2rs_0002/odf'],
        "label": "D",
        "support_np": True,
    },
}
