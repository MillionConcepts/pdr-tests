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

file_information = {
    # Note for IMG node products:
    # Most products have attached labels. Sometimes they ALSO have a detached label.
    # The detached labels include info on the compressed (.zip) versions of the products.
    # All have detached PDS4 labels.	
    
    # Cassini Radar Long Burst Data Record
    "lbdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CORADR', 'DATA/LBDR'],
        "label": "A",
    },
    # Cassini Radar Short Burst Data Record
    "sbdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CORADR', 'DATA/SBDR'],
        "label": "A",
    },
    # Cassini Radar Altimeter Burst Data Record
    "abdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CORADR', 'DATA/ABDR'],
        "label": "A",
    },
    # Basic Image Data Record
    "bidr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['CORADR', 'DATA/BIDR'],
        "label": "A",
    },
    # Synthetic Aperture Radar Topograpgy (SARTopo)
    "stdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['CORADR', 'DATA/STDR'],
        "label": "D",
    },
    # Cassini Radar Altimeter Burst Data Record Summary
    "asum": {
        "manifest": IMG_FILE,
        "fn_regex": [r'\.CSV$'],
        "url_must_contain": ['CORADR', 'DATA/ASUM'],
        "label": "D",
    },
    
    # ATM node products:
    # Saturn mapping results; CO-S-RADAR-5-RADIOMETRY-V1.0
    # "calibrated time-ordered data"
    "cal_tod": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['coradr_5001/data'],
        "label": "D",
    },
}
