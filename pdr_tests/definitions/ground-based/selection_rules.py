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
ATM_FILE = "atm"
GEOLAB_FILE = "geolab"
RMS_FILE = "ringvolumes"
SBN_FILE = "tiny_other"

file_information = {
    # Ground-based spectrophotometry of the Jovian planets and Titan.
    # Methane absorption and albedos
    "gbat": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gbat_0001/data'],
        "label": "D",
    },
    # Bloomsburg University Goniometer Mars soil analogs
    # Analogs: AREF_235, AREF_236, AREF_237, AREF_238, and JSC_Mars1
    "bug_dist_funct": {
        "manifest": GEOLAB_FILE,
        "fn_must_contain": ['0.tab'],
        "url_must_contain": ['bug_9001/data'],
        "label": "D",
    },
    "bug_spectra": {
        "manifest": GEOLAB_FILE,
        "fn_must_contain": ['spectrum.tab'],
        "url_must_contain": ['bug_9001/data'],
        "label": "D",
    },
    # 1989 Saturn ring occultation of 28 Sagittarii
    "ring_occ_1989": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['EBROCC_0001/DATA'],
        "label": "D",
    },
    # Lowell Observatory Cometary Database and Production Rates
    "lowell_comet": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ear-c-phot-3-rdr-lowell-comet-db-v1.0/data'],
        "label": "D",
    },
    "lowell_comet_pr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ear-c-phot-5-rdr-lowell-comet-db-pr-v1.0/data'],
        "label": "D",
    },
    # Northern Arizona University - Lab CH3D Ice Absorption Coefficients
    "nau_lab_ice": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ear-x-i2041-5-ch3dicespec-v1.0/data'],
        "label": "D",
    },
    
}

"""
    # Mars Analog Handlens-Scale Image Data Base
    # Not supported: "The DOCUMENT pointer is not yet fully supported."
    "mahl": {
        "manifest": GEOLAB_FILE,
        "fn_must_contain": ['.jpg'],
        "url_must_contain": ['mahl_0001/data'],
        "label": "D",
    },
"""
