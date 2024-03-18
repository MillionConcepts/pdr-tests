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
    "V4_uncal_electrons": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "UNCALIBRATED", 'ELECTRONS'],
        "label": "D",
    },
    "V4_uncal_ide": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "UNCALIBRATED", 'ION_DIRECT_EVENTS'],
        "label": "D",
    },
    "V4_uncal_il": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "UNCALIBRATED", 'ION_LOGICALS'],
        "label": "D",
    },
    "V4_uncal_is": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "UNCALIBRATED", 'ION_SPECIES'],
        "label": "D",
    },
    "V4_uncal_itof": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "UNCALIBRATED", 'ION_TOF'],
        "label": "D",
    },
    "V4_cal_electrons": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "-CALIBRATED", 'ELECTRONS'],
        "label": "D",
    },
    "V4_cal_il": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "-CALIBRATED", 'ION_LOGICALS'],
        "label": "D",
    },
    "V4_cal_is": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "-CALIBRATED", 'ION_SPECIES'],
        "label": "D",
    },
    "V4_cal_itof": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-J_SW-JAD', "-CALIBRATED", 'ION_TOF'],
        "label": "D",
    },
    "V3_uncal_electrons": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-SW-JAD', "UNCALIBRATED", 'ELECTRONS'],
        "label": "D",
    },
    "V3_uncal_ide": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-SW-JAD', "UNCALIBRATED", 'ION_DIRECT_EVENTS'],
        "label": "D",
    },
    "V3_uncal_il": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-SW-JAD', "UNCALIBRATED", 'ION_LOGICALS'],
        "label": "D",
    },
    # ion spectra housekeeping products (HSK_ION_SPA) are not supported; the format files are incorrect
    "V3_uncal_is": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-SW-JAD', "UNCALIBRATED", 'ION_SPECTRA'],
        "label": "D",
    },
    "V3_uncal_itof": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-SW-JAD', "UNCALIBRATED", 'ION_TOF'],
        "label": "D",
    },
}
