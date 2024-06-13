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
GEO_FILE = "geomex"

file_information = {
    # Atmosphere profiles derived from occultation data
    "occ_atmo": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['_ai', '.tab'],
        "url_must_contain": ['mex-m-mrs-5-occ', 'data'],
        "label": "D",
    },
    # Ionosphere profiles derived from occultation data
    "occ_iono": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['_ii', '.tab'],
        "url_must_contain": ['mex-m-mrs-5-occ', 'data'],
        "label": "D",
    },
    # Level 1a data; open loop; binary tables
    # These appear to be opening correctly, except for the "SAMPLE WORDS"
    # field, which looks off and is difficult to verify.
    "lvl_1a_open": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1a/open'],
        "label": "D",
    },
    # Level 1a ODFs; closed loop; binary tables
    # Many of these products open fine, but those with "DSN_STATION_NUMBER = 0"
    # in their labels are unsupported (incomplete/non compliant labels).
    "lvl_1a_odf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['odf', '.dat'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1a/closed'],
        "label": "D",
    },
    # Level 1b ICL data; closed loop; ascii tables
    # subtypes: gain, doppler, and ranging tables
    "lvl_1b_icl": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['icl', '.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1b/closed'],
        "label": "D",
    },
    # Level 1b ODFs; closed loop; ascii tables
    # subtypes: doppler, ranging, and ramp tables
    "lvl_1b_odf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['odf', '.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1b/closed'],
        "label": "D",
    },
    # Level 1b TNFs; closed loop; ascii tables
    # subtypes: uplink and downlink tables
    "lvl_1b_tnf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['tnf', '.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1b/closed'],
        "label": "D",
    },
    # Level 2 data; open loop; ascii tables
    # subtypes: BSR, geometry, and doppler tables
    "lvl_2_open": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level02/open'],
        "label": "D",
    },
    # Level 2 ICL data; closed loop; ascii tables
    "lvl_2_icl": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['icl', '.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level02/closed'],
        "label": "D",
    },
    # Level 2 TCL data; closed loop; ascii tables
    "lvl_2_tcl": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['tcl', '.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level02/closed'],
        "label": "D",
    },
    # Level 2 ODFs; closed loop; ascii tables
    # subtypes: doppler and ranging tables
    "lvl_2_odf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['odf', '.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level02/closed'],
        "label": "D",
    },
    # Level 2 TNFs; closed loop; ascii tables
    "lvl_2_tnf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['tnf', '.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level02/closed'],
        "label": "D",
    },
}

SKIP_FILES = ["MARS_DESC.TXT", "MEX_POINTING_MODE_DESC.TXT"]

"""
    # Level 1a data; closed loop; binary tables
    # Support not planned --> incomplete/non compliant labels
    "lvl_1a_icl": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['icl', '.raw'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1a/closed'],
        "label": "D",
    },
    "lvl_1a_tcl": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['tcl', '.raw'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1a/closed'],
        "label": "D",
    },
    "lvl_1a_tnf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['tnf', '.dat'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1a/closed'],
        "label": "D",
    },
    
    # Level 1b open loop products appear to not exist in the archive, even
    # though they are listed in the dataset documentation.
    "lvl_1b_open": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mex-m-mrs-1_2_3', 'data/level1b/open'],
        "label": "D",
    },
"""
