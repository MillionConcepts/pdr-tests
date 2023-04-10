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
from pathlib import Path

import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .parquet files
MANIFEST_FILE = Path(MANIFEST_DIR, "geolunar.parquet")

file_information = {
    # Lunar Spectral Profiler Data (PDS3)
    "sm_craters": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['kaguya-l-sp-5-spectra-v1/kagsp_1001/data'],
        "label": "D",
    },
    
# PDS4 Datasets
# Note: test cases have not been picked for these because they are PDS4 products
#       and very large files (especially grs_spectra).
    # Gamma-Ray Spectrometer Corrected Spectra
##    "grs_spectra": {
##        "manifest": MANIFEST_FILE,
##        "fn_must_contain": ['calibrated_spectra','.csv'],
##        "url_must_contain": ['kaguya_grs_spectra/data_spectra'],
##        "label": ('.csv','.xml'),
##    },
##    # Gamma-Ray Spectrometer ephemerides, pointing, and geometry (EPG)
##    "grs_EPG": {
##        "manifest": MANIFEST_FILE,
##        "fn_must_contain": ['kgrs_ephemerides','.csv'],
##        "url_must_contain": ['kaguya_grs_spectra/data_ephemerides'],
##        "label": ('.csv','.xml'),
##    },
##    # Lunar Space Weathering Maps 
##    "weathering": {
##        "manifest": MANIFEST_FILE,
##        "fn_must_contain": ['.img'],
##        "url_must_contain": ['trang2020_moon_space_weathering/data'],
##        "label": ('.img','.xml'),
##    },
}
