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
RMS_FILE = "ringvolumes"

file_information = {
    "data": {
        "manifest": RMS_FILE,
        "fn_regex": [r'((bdb)|(bep)|(bes)|(tf)|(ti)|(tls)|(bpc)|(tpc)'
                     r'|(tsc)|(bsp))$'],
        "url_must_contain": ['COSP_xxxx/COSP_1000/data'],
        "label": 'D',
        "support_np": True,
    },
    "extras": {
        "manifest": RMS_FILE,
        "fn_regex": [r'((orb)|(tm)|(zip))$'],
        "url_must_contain": ['COSP_xxxx/COSP_1000/extras'],
        "label": 'A', # no PDS labels
        "support_np": True,
    },
}

