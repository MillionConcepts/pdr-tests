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
PPI_FILE = "plasm_full"
ATM_FILE = "atm"
GEO_FILE = "geomariner"

file_information = {
    
    # Mariner 9 electron density profiles
    "ele_density": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['MR9-M-RSS-5','DATA/ELECTRON_DENSITY'],
        "label": "D",
    },
    # Mariner 9 IRIS spectral observations
    "iris": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['mr9_1001/data'],
        "label": "D",
    },
    # Mars cloud catalog (Viking Orbiters and Mariner 9 data)
    "clouds": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['vomr_0001/data'],
        "label": "D",
    },
}

"""
    # Spot check of Mariner 1969 PDS4 products. Not included in the test corpus
    "pds4_tab": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['duxbury_pdart14_mariner69/data_table'],
        "label": ('.tab', '.xml'),
    },
    "pds4_img": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['duxbury_pdart14_mariner69/data_mars_'],
        "label": ('.img', '.xml'),
    },
"""
