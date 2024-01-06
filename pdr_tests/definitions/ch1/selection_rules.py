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
GEO_FILE = "img_usgs_chandrayaan_1"

file_information = {
    "M3_L0": {
        "manifest": GEO_FILE,
        "fn_ends_with": ["_L0.IMG"],
        "url_must_contain": ["Chandrayaan_1/M3/", "DATA", "/L0"],
        "label": "D"
    },
    "M3_L1B": {
        "manifest": GEO_FILE,
        "fn_ends_with": ["_RDN.IMG"],
        "url_must_contain": ["Chandrayaan_1/M3", "DATA", "/L1B"],
        "label": ("RDN.IMG", "L1B.LBL"),
    },
    "M3_L2": {
        "manifest": GEO_FILE,
        "fn_ends_with": ["_RFL.IMG"],
        "url_must_contain": ["Chandrayaan_1/M3", "DATA", "/L2"],
        "label": ("RFL.IMG", "L2.LBL")
    },
}
