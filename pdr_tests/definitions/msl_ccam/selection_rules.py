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
GEO_FILE = "geomsl"

file_information = {
    # the quality of at least the metadata in the LIBS EDR corpus is
    # extremely spotty. it is not currently supported (and not planned).

    # "CCAM_LIBS_EDR": {
    #     "manifest": GEO_FILE,
    #     "fn_regex": [r"cl[0-9].*edr.*ccam.*\.dat"],
    #     "url_must_contain": ["msl-m-chemcam-libs-2-edr-v1"],
    #     "label": "D",
    # },
    # "CCAM_LIBS_EDR_RARE": {
    #     "manifest": GEO_FILE,
    #     "fn_regex": [r"cl[378].*edr.*ccam.*\.dat"],
    #     "url_must_contain": ["msl-m-chemcam-libs-2-edr-v1"],
    #     "label": "D",
    # },
    "CCAM_RMI_EDR": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cr0.*edr.*ccam.*\.img"],
        "url_must_contain": ["msl-m-chemcam-libs-2-edr-v1"],
        "label": "D",
    },
    "CCAM_LIBS_L2": {
        "manifest": GEO_FILE,
        "fn_regex": [r"([mu][oe]c|rsm|tec)_\d{4}_\d{4}\.csv"],
        "url_must_contain": ["msl-m-chemcam-libs-4_5-rdr-v1"],
        "label": "D",
    },
    "CCAM_LIBS_L1B": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cl[0-9].*(ccs|rdr).*ccam.*\.(tab|csv)"],
        "url_must_contain": ["msl-m-chemcam-libs-4_5-rdr-v1"],
        "label": "D",
    },
    "CCAM_RMI_RDR": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cr0.*prc.*ccam.*\.tif"],
        "url_must_contain": ["msl-m-chemcam-libs-4_5-rdr-v1"],
        "label": "D",
    },
}

#irrelevant
SKIP_FILES = ["VICAR2.TXT ", "ODL.TXT"]
