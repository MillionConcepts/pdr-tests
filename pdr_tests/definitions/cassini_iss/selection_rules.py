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
    # "Raw Ground Calibration for WACFM and NACFM Volumes 1-10. Volume 11 
    # contains calibration data, software, algorithms, sample images, and 
    # related calibration documentation"
    "calib": {
        "manifest": IMG_FILE,
        "fn_regex": [r'(.img)|(.IMG)'],
        "url_must_contain": ['data'],
        "url_regex": [r'(coiss_000[0-9])|(coiss_0010)'],
        "label": "D",
    },
    # "direct access" calibration images
    # Note: ix grabs the wrong filename from the labels when writing the index 
    # (*.ZIP instead of *.DA). A quick find/replace fixes it before ix download
    "calib_da": {
        "manifest": IMG_FILE,
        "fn_regex": [r'(da$)|(DA$)'],
        "url_must_contain": ['coiss_0', 'data'],
        "label": "D",
    },
    # Volume coiss_0011_v3 is technically superseded by coiss_0011_v4.3 at the 
    # IMG JPL node, but the v4.3 products have multiple errors in their labels.
    # Products in v3 at IMG USGS appear to open correctly. 
    "calib_0011": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['coiss_0011_v3/data'],
        "label": "D",
    },
    # Other superseded versions of coiss_0011 at IMG USGS
    "calib_superceded": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_regex": [r'(coiss_0011/data)|(coiss_0011_v2/data)'],
        "label": "D",
        "support_np": True
    },
    # coiss_0011 at ATM is a mirror of coiss_0011_v4.3 at IMG JPL.
    # The products have multiple BYTES/RECORD_BYTES mistakes in their labels 
    # that cause them to open incorrectly. The mistakes are inconsistent enough 
    # that writing special cases for them is extremely tedious
    "calib_atm": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['coiss_0011/data'],
        "label": "D",
        "support_np": True
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

SKIP_FILES = ["VICAR2.TXT", "ZIPINFO.TXT"]
