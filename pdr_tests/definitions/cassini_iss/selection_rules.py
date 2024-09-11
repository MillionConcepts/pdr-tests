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
IMG_FILE = "img_usgs_cassini"
ATM_FILE = "atm"


# Note: this is another dataset that uses multiple format files with the same name but 
# slightly different contents: tlmtab.fmt. calib, edr_evj, and edr_sat each have their own.

file_information = {
	
    # line_prefix_tables are unsupported with eventual support planned
	
    # Calibration files
    "calib": {
        "manifest": IMG_FILE,
        "fn_regex": [r'(.img)|(.IMG)'],
        "url_must_contain": ['coiss_0', 'data'],
        "label": "D",
    },
    # coiss_0011 volume at ATM is not a perfect mirror of coiss_0011 at IMG
    "calib_atm": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['coiss_0011/data'],
        "label": "D",
    },
    # Earth/Venus/Jupiter EDRs
    "edr_evj": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['coiss_1', 'data'],
        "label": "D",
    },
    # Saturn EDRs
    "edr_sat": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['coiss_2', 'data'],
        "label": "D",
    },
    # MIDR (Mosaicked Image Data Record)
    "midr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['coiss_3', 'data/images'],
        "label": "A",
    },
    # the MIDR directory includes 'maps' in addition to the 'images' product above. they
    # are publication/presentation quality versions of the images in PDF format.
}

SKIP_FILES = ["VICAR2.TXT"]
