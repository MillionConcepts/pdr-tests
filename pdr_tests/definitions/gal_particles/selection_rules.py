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
PLASM_FILE = "plasm_full"

file_information = {
    # GALILEO DUST DETECTION SYSTEM
    "gdds": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-D-GDDS-5-DUST-V4.1/DATA'],
        "label": "D",
    },
    
    # ENERGETIC PARTICLES DETECTOR
    "epd_samp": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-E-EPD-2-SAMP-', 'DATA'],
        "label": "D",
    },
    # EPD data from Earth encounters; 30 minute averages
    "epd_summ": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-E-EPD-4-SUMM-', 'DATA'],
        "label": "D",
    },
    # high resolution data from Jupiter and its satellites
    "epd_highres": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-J-EPD-2-REDR-HIGHRES-', 'DATA'],
        "label": "D",
    },
    # RTS 11 minute sector averages
    "epd_avg": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-J-EPD-2-REDR-RTS-SCAN-AVG-', 'DATA'],
        "label": "D",
    },

    # STAR SCANNER - derived electron flux data
    "ssd": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-J-SSD-5-DDR-STAR-SENSOR-V1.0/DATA'],
        "label": "D",
    },
    
    # RADIO SCIENCE SUBSYSTEM - derived electron density profiles
    "rss": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.EDS'],
        "url_must_contain": ['GO-J-RSS-5-ROCC-V1.0/DATA'],
        "label": "D",
    },
    
}
