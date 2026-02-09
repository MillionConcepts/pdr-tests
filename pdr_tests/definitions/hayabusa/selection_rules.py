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

# not including the shape models generated from Hayabusa data
# (ITOKAWASHAPE etc)

# I don't know why but some of the lbl files in the parquet file for the SBN
# are "LBL" instead of "lbl" like that are online. But most of them are the
# correct "lbl"

# variables naming specific parquet files in node_manifests
SBN = "tiny_sbnarchive"

file_information = {
    "nirs_cal": {
        "manifest": SBN,
        "fn_must_contain": ["_lvl3_", ".fit"],
        "url_must_contain": ['HAY', 'NIRSCAL', 'NIRS_3', 'data'],
        "label": (".fit", ".lbl"),
    },
    "nirs_raw": {
        "manifest": SBN,
        "fn_must_contain": [".fit", "_lvl1_"],
        "url_must_contain": ['HAY', 'NIRSRAW', 'NIRS_2', 'data'],
        "label": (".fit", ".lbl"),
    },
    "lidar_3_edr": {
        "manifest": SBN,
        "fn_must_contain": ["edr2", ".tab"],
        "url_must_contain": ['HAY', 'LIDAR_3', 'data'],
        "label": (".tab", ".lbl"),
    },
    "lidar_3_cdr": {
        "manifest": SBN,
        "fn_must_contain": [".tab", "cdr"],
        "url_must_contain": ['HAY', 'LIDAR_3', 'data'],
        "label": (".tab", ".lbl"),
    },
    "amica_images": {
        "manifest": SBN,
        "fn_must_contain": [".fit", "st_"],
        "url_must_contain": ['HAY', 'AMICA', 'data'],
        "label": (".fit", ".lbl"),
    },
    # there are more things on jaxa darts (AMICA DDRs etc)

}
