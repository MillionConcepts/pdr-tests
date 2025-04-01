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
SBN_FILE = "tiny_sbnarchive"


file_information = {
    # GRS EDR - grb products
    "grs_edr_b": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_GRS_2_EDR_', 'data/grb'],
        "label": "D",
    },
    # GRS EDR - grf products
    "grs_edr_f": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_GRS_2_EDR_', 'data/grf'],
        "label": "D",
    },
    # GRS EDR - grs products
    "grs_edr_s": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_GRS_2_EDR_', 'data/grs'],
        "label": "D",
    },
    # GRS L2 orbit spectra
    "grs_orbit": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['NEAR_A_GRS_3_EDR_EROS_ORBIT', '/data'],
        "label": "D",
    },
    # GRS L2 surface spectra
    "grs_surface_l2": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['NEAR_A_GRS_3_EDR_EROS_SURFACE', '/data/level2'],
        "label": "D",
    },
    # GRS L3 surface spectra
    "grs_surface_l3": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['NEAR_A_GRS_3_EDR_EROS_SURFACE', '/data/level3'],
        "label": "D",
    },
    
    
    # NIS EDR
    "nis_edr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_NIS_2_EDR_', '/data'],
        "label": "D",
    },
    "nis_edr_extras": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_NIS_2_EDR_', '/extras'],
        "support_np": True # no PDS labels
    },
    # NIS L2 data - original version
    "nis_l2_orig": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_NIS_5_EDR_EROS_ORBIT_V1_0/data'],
        "label": "D",
    },
    # NIS L2 data - same data as above, just subdivided into smaller tables 
    "nis_superseded": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_NIS_5_EDR_', '/data'],
        "url_regex": [r'(CRUISE)|(EARTH)|(EROS_FLY)|(EROS_ORBIT_(.+)V)'],
        "label": "D",
    },
    # NIS L2 data - revised version
    "nis_l2_revis": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_NIS_5_EDR_ALL_PHASES_PDSREV_V1_0/data'],
        "label": "D",
    },
    
    
    # XRS EDR - xrf products
    "xrs_edr_f": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.'],
        "url_must_contain": ['NEAR_A_XRS_2_EDR_', '/data/xrf'],
        "label": "D",
    },
    # XRS EDR - xrs products
    "xrs_edr_s": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_XRS_2_EDR_', '/data/xrs'],
        "label": "D",
    },
    # XRS L2 spectra
    "xrs_l2": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['NEAR_A_XRS_3_EDR_', '/data/level2'],
        "label": "D",
    },
    # XRS L3 spectra
    "xrs_l3": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['NEAR_A_XRS_3_EDR_', '/data/level3'],
        "label": "D",
    },
}
