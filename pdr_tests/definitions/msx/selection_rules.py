"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .parquet file that contains urls, file sizes, etc., scraped
directly from the hosting institution for this product type. for some data
sets, all urls will be found in the same .parquet file; for others, they may
be split between nodes or scraping sessions.

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
SBN_FILE = "tiny_sbnarchive"
GEO_FILE = "geolunar"

file_information = {    
    # Infrared images in cube format
    # ENVI_HEADERs do not open, FITS_HEADERs open fine
    # QUBE products open fine (although data.show and browsify don't like them)
    "cubes": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.qub'],
        "url_must_contain": ['msx-l-spirit3-2_4-v1/msx_9001/data'],
        "label": "D",
    },
    # Infrared Minor Planet Survey; MSX-A-SPIRIT3-5-SBN0003-MIMPS-V1.0
    "ir_survey": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['MSX_A_SPIRIT3_5_SBN0003_MIMPS_V1_0/data'],
        "label": "D",
    },
    # Small Bodies Images; MSX-C-SPIRIT3-3-MSXSB-V1.0
    "sb_images": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['MSX_C_SPIRIT3_3_MSXSB_V1_0/data'],
        "label": "D",
    },
    # Zodiacal Dust Data; MSX-D-SPIRIT3-3-MSXZODY-V1.0
    "dust": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['MSX_D_SPIRIT3_3_MSXZODY_V1_0/data'],
        "label": "D",
    },
}
