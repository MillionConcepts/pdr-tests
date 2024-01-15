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
SB_FILE = "tiny_other"

file_information = {
    # NAVCAM - EDR
    "nav_edr": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['sdu-c_cal-navcam-2-next-tempel1-v1.0/data'],
        "label": "D",
    },
    # NAVCAM - RDR
    "nav_rdr": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['sdu-c_cal-navcam-3-next-tempel1-v1.0/data'],
        "label": "D",
    },
    # Derived Shape Model
    "shape": {
        "manifest": SB_FILE,
        "fn_regex": ['(tab$)|(wrl$)'],
        "url_must_contain": ['dif-c-hriv_its_mri-5-tempel1-shape-v2.0/data'],
        "label": "D",
    },
    # DFMI
    "dfmi": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c_d-dfmi-2_3-next-tempel1-v1.0/data'],
        "label": "D",
    },
    # CIDA
    "cida": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c_d-cida-2_3-next-tempel1-v1.0/data'],
        "label": "A",
    },
    
}
