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
MANIFEST_FILE = "img_usgs"

file_information = {
    # Experiment Data Record; uncalibrated data
    # Acquisition list table is missing all but 1 row
    # "door open" image header is a copy of the "door closed" image header
##    "edr": {
##        "manifest": MANIFEST_FILE,
##        "fn_must_contain": ['.fit'],
##        "url_must_contain": ['LROLAM_0', 'DATA'],
##        "label": 'D',
##    },
    # Reduced Data Record; calibrated data
    # Acquisition list table is missing all but 1 row
    # "door open" image header is a copy of the "door closed" image header
    # Unique histogram image pointers are defined by one non-unique image object
##    "rdr": {
##        "manifest": MANIFEST_FILE,
##        "fn_must_contain": ['.fit'],
##        "url_must_contain": ['LROLAM_1', 'DATA'],
##        "label": 'D',
##    },
    # Gridded Data Record; calibrated LAMP data, gridded into polar
    # stereographic maps
    "gdr_month": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'[a-z]_[0-9]+_[0-9]+\.img$'],
        "url_must_contain": ['LROLAM_2', 'DATA'],
        "label": 'D',
    },
    "gdr_year": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'[a-z]_[0-9]+\.img$'],
        "url_must_contain": ['LROLAM_2', 'DATA'],
        "label": 'D',
    },
}
