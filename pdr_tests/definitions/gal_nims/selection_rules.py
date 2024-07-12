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
IMG_FILE = "img_usgs_galileo"
SB_FILE = "tiny_sbnarchive"

file_information = {
    # EDRs (go_1001-go_1004) - cruise phase, calibrations, Gaspra and Ida
    "pre_jup": {
        "manifest": IMG_FILE,
        "fn_regex": [r'e[0-9]{7}\.[0-9]{2}[a-z]'],
        "url_must_contain": ['Galileo/NIMS', 'edr'],
        "url_regex": [r'go_100[1-4]'],
        "label": "A",
    },
    # EDRs (go_1005-go_1008) - Jupiter and its moons
    # DATA_TABLE and HEADER_TABLE do not open. KeyError: 'NAME'
##    "edr": {
##        "manifest": IMG_FILE,
##        "fn_must_contain": ['.edr'],
##        "url_must_contain": ['Galileo/NIMS', '/edr'],
##        "url_regex": [r'go_100[5-8]'],
##        "label": "A",
##    },
    # Cubes (go_1101-go_1120)
    # QUBEs do not open because they are VAX_REAL
    # HISTOGRAM_IMAGEs also don't open. ValueError: This table's byte sizes are underspecified.
    "cube": {
       "manifest": IMG_FILE,
       "fn_regex": [r'qu[bt]$'],
       "url_must_contain": ['Galileo/NIMS'],
       "url_regex": [r'go_11..'],
       "label": "A",
    },
    # Data from a Shoemaker-Levy 9 fragment's impact with Jupiter
    "impact": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['Galileo/NIMS', 'sl9'],
        "label": "D",
    },
    # Ida and Gaspra specific products at the SB Node:
    "sb_spectra": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['galileo/derived', '_NIMS_', 'SPEC', '/data'],
        "label": "D",
    },
    "sb_cube": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['galileo/derived', '_NIMS_', 'CUBE', '/data'],
        "label": "D",
    },
}
