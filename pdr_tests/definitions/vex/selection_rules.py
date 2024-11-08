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
ATM_FILE = "atm"

file_information = {

    # Radio Science Data
    # DSN Keyword File (DKF)
    "dkf": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.DKF'],
        "url_must_contain": ['VXRS_110', '/DKF'],
        "label": "D",
    },
    # Earth Orientation Parameters (EOP)
    "eop": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.EOP'],
        "url_must_contain": ['VXRS_110', '/EOP'],
        "label": "D",
    },
    # Ionospheric Media Calibration (ION)
    "ion": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.ION'],
        "url_must_contain": ['VXRS_110', '/ION'],
        "label": "D",
    },
    # Orbit Data Files (ODFs)
    "odf": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.ODF'],
        "url_must_contain": ['VXRS_110', '/ODF'],
        "label": "D",
    },
    # Radio Science Receiver (RSR)
    "rsr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.RSR'],
        "url_must_contain": ['VXRS_110', '/RSR'],
        "label": "D",
    },
    # Tropospheric Media Calibration (TRO)
    "tro": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TRO'],
        "url_must_contain": ['VXRS_110', '/TRO'],
        "label": "D",
    },
    # DSN Weather (WEA)
    "wea": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.WEA'],
        "url_must_contain": ['VXRS_110', '/WEA'],
        "label": "D",
    },

    # Support not planned:
    # spice kernels
    "unsupported_spice": {
        "manifest": ATM_FILE,
        "fn_regex": [r'((BCK)|(BSP)|(FRK)|(LSK)|(PCK)|(SCK))$'],
        "url_must_contain": ['VXRS_110'],
        "label": "D",
        "support_np": True
    },
    # incomplete labels
    "unsupported_mft": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.MFT'],
        "url_must_contain": ['VXRS_110', '/MFT'],
        "label": "A",
        "support_np": True
    },
    # incomplete labels
    "unsupported_tnf": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TNF'],
        "url_must_contain": ['VXRS_110', '/TNF'],
        "label": "D",
        "support_np": True
    },
    # PostScript files
    "unsupported_bro": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.PS1'],
        "url_must_contain": ['VXRS_110', '/BRO'],
        "label": "D",
        "support_np": True
    },
}
