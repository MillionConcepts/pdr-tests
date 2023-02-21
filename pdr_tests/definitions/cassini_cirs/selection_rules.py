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

# shorthand variables for specific .csv files
ATM_FILE = Path(MANIFEST_DIR, "atm.parquet")
RMS_FILE = Path(MANIFEST_DIR, "ringvolumes.parquet")

file_information = {
	
    # navigational data (GEO, POI, RIN, TAR); fixed-length
    "nav": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/NAV_DATA'],
        "label": "D",
    },
    # housekeeping data (HSK, IHSK, OBS); fixed-length
    "hsk": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.DAT'],
        "fn_regex": [r'(HSK)|(IHSK)|(OBS)'],
        "url_must_contain": ['cocirs', 'DATA/TSDR'],
        "url_regex": [r'(HSK_DATA)|(UNCALIBR)'],
        "label": "D",
    },
	# spectral QUBE (notionally supported; selected a test case for regression testing)
    "cube": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tar.gz'], # contains: LBL, DAT (data file), and JPG (browse image)
        "url_must_contain": ['cocirs', 'DATA/CUBE'],
        "label": ('.tar.gz', '.LBL'),
    },
    # diagnostic info for raw interferograms; fixed-length
    # grouped with 'hsk' originally. now a separate product type because additional testing was needed
    "diag": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['DIAG', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/UNCALIBR'],
        "label": "D",
    },
    
# RMS node supplemental data set
# CIRS re-formated: simplified versions of variable-length files
    # calibrated and resampled spectra
    "spectra": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['SPEC', '.DAT'],
        "url_must_contain": ['DATA'],
        "url_regex": [r'(COCIRS_5xxx)|(COCIRS_6xxx)'],
        "label": "D",
    },
	# spectra prefixes; parameters describing the calibrated spectra
    "prefix": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['ISPM', '.TAB'],
        "url_must_contain": ['DATA'],
        "url_regex": [r'(COCIRS_5xxx)|(COCIRS_6xxx)'],
        "label": "D",
    },
		
# 	# interferometer voltages; variable-length (not supported)
#     "uncal_frv": {
#         "manifest": ATM_FILE,
#         "fn_must_contain": ['FRV', '.VAR'],
#         "url_must_contain": ['cocirs', 'DATA/TSDR/UNCALIBR'],
#         "label": "D",
#     },
#     # IFM records; variable-length (not supported)
#     "uncal_ifgm": {
#         "manifest": ATM_FILE,
#         "fn_must_contain": ['IFGM', '.VAR'],
#         "url_must_contain": ['cocirs', 'DATA/TSDR/UNCALIBR'],
#         "label": "D",
#     },
# 	# calibrated spectra; variable-length (not supported)
#     "cal_spectra": {
#         "manifest": ATM_FILE,
#         "fn_must_contain": ['ISPM', '.VAR'],
#         "url_must_contain": ['cocirs', 'DATA/TSDR/APODSPEC'],
#         "label": "D",
#     },
	
}
