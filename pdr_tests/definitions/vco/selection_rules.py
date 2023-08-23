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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
ATM_FILE = Path(MANIFEST_DIR, "atm.parquet")


file_information = {
    # IR1 and IR2 raw, calibrated, and geometry data
    "ir_raw": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_regex": [r'vcoir[12]_0001/data'],
        "label": "D",
    },
    "ir_cal": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_regex": [r'vcoir[12]_1001/data'],
        "label": "D",
    },
    "ir_geo": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_regex": [r'vcoir[12]_2001/geometry'],
        "label": "D",
    },
    # LIR raw, calibrated, and geometry data
    "lir_raw": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['vcolir_00','/data'],
        "label": "D",
    },
    "lir_cal": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['vcolir_10','/data'],
        "label": "D",
    },
    "lir_geo": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['vcolir_20','/geometry'],
        "label": "D",
    },
    # UVI raw, calibrated, and geometry data
    "uvi_raw": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['vcouvi_00','/data'],
        "label": "D",
    },
    "uvi_cal": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['vcouvi_10','/data'],
        "label": "D",
    },
    "uvi_geo": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['vcouvi_20','/geometry'],
        "label": "D",
    },
    # Doppler Profiles
    "doppler": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['rs_', '.tab'],
        "url_must_contain": ['vcors_10','/data'],
        "label": "D",
    },
    # Temperature-Pressure Profiles
    "temp_pres": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['rs_', '.tab'],
        "url_must_contain": ['vcors_20','/data'],
        "label": "D",
    },
}

