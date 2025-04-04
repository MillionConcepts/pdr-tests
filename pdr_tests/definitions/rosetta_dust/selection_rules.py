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
SB_FILE = "tiny_rosetta"

file_information = {
	
# start GIADA data products
    # EDRs
    "EDR_giada": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-gia-2-', '/data'],
        "label": "D",
    },
    # RDRs
    "RDR_giada": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-gia-3-', '/data'],
        "label": "D",
    },
    # DDRs
    "DDR_giada": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-gia-5-', '/data'],
        "label": "D",
    },
	
# start MIDAS data products
    # RDRs
    "RDR_midas_fsc": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-midas-3-', '/data/fsc'],
        "label": "D",
    },
    "RDR_midas_lin": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-midas-3-', '/data/lin'],
        "label": "D",
    },
    "RDR_midas_spa": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-midas-3-', '/data/spa'],
        "label": "D",
    },
    "RDR_midas_sps": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-midas-3-', '/data/sps'],
        "label": "D",
    },
    "RDR_midas_hk": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-midas-3-', '/data/hk'],
        "label": "D",
    },
    "RDR_midas_roi": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-midas-3-', '/data/roi'],
        "label": "D",
    },
    "RDR_midas_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-midas-3-', '/data'],
        "label": "D",
    },
    "RDR_midas_tab": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-midas-3-', '/data'],
        "label": "D",
    },
    # DDRs
    "DDR_midas_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-midas-5-', '/data'],
        "label": "D",
    },
    "DDR_midas_tab": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-midas-5-', '/data'],
        "label": "D",
    },
	
}

SKIP_FILES = ["MID_EAICD.PDF", "MID_CALIBRATION.PDF", 
              "MID_TIP_IMAGES.PDF", "MID_FS_SUMMARY.PDF"]
