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
SBN_FILE = "tiny_other"
GEO_FILE = "geonear"


file_information = {
    # EDR
    "edr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_NLR_2_EDR_', '/data'],
        "label": "D",
    },
    # CDR - level 2 / topo (SBN and GEO)
    "cdr_topo": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['near-a-nlr-5-cdr-', 'level2/topo'],
        "label": "D",
    },
    # CDR - level 3 / ascii (SBN and GEO)
    "cdr_asc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['near-a-nlr-5-cdr-', 'level3/ascii'],
        "label": "D",
    },
    # CDR - level 3 / img (SBN and GEO)
    "cdr_img": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['near-a-nlr-5-cdr-', 'level3/img'],
        "label": "D",
    },
    # CDR - level 3 / shape models (SBN and GEO)
    "cdr_sha": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.sha'],
        "url_must_contain": ['near-a-nlr-5-cdr-', 'level3/sha'],
        "label": "D",
    },
    # Another Eros shape model dataset
    "shape": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['NEAR_A_NLR_5_EROS_SHAPE_GRAVITY_V1_0/eroshape'],
        "label": "D",
    },
}
