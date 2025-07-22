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
RMS_FILE = "ringvolumes"

"""
Some ptypes have fixed-length and variable-length tables associated to each
product. There are no pointers to the variable-length tables/files.
Product types with .VAR files: frv, ifgm, ispm, and oispm
"""

file_information = {
    
    # APODSPEC
    # ISPM - calibrated, re-sampled (interpolated) spectral data
    "ispm": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['ISPM', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/APODSPEC'],
        "label": "D",
    },
    # HSK_DATA
    # HSK - raw housekeeping data
    "hsk": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['HSK', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/HSK_DATA'],
        "label": "D",
    },
    # NAV_DATA
    # GEO - spacecraft orientation data
    "geo": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['GEO', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/NAV_DATA'],
        "label": "D",
    },
    # POI - target body navigational data
    "poi": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['POI', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/NAV_DATA'],
        "label": "D",
    },
    # RIN - ring observations navigational data
    "rin": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['RIN', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/NAV_DATA'],
        "label": "D",
    },
    # TAR - target identification data
    "tar": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['TAR', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/NAV_DATA'],
        "label": "D",
    },
    # SUSPECT_SPECTRA
    # OISPM - calibrated, re-sampled spectral data of reduced quality
    "oispm": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['OISPM', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/SUSPECT_SPECTRA'],
        "label": "D",
    },
    # UNCALIB
    # DIAG - IFM diagnostic info
    "diag": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['DIAG', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/UNCALIBR'],
        "label": "D",
    },
    # FRV - IFM fringe voltages
    "frv": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['FRV', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/UNCALIBR'],
        "label": "D",
    },
    # IFGM - raw interferogram data
    "ifgm": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['IFGM', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/UNCALIBR'],
        "label": "D",
    },
    # IHSK - interpolated housekeeping data 
    "ihsk": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['IHSK', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/UNCALIBR'],
        "label": "D",
    },
    # OBS - observation parameters
    "obs": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['OBS', '.DAT'],
        "url_must_contain": ['cocirs', 'DATA/TSDR/UNCALIBR'],
        "label": "D",
    },
    # Tables in the EXTRAS directories
    "extras_tab": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['cocirs', 'EXTRAS'],
        "label": "D",
    },
    "extras_asc": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.ASC'],
        "url_must_contain": ['cocirs', 'EXTRAS'],
        "label": "D",
        "support_np": True # incomplete labels
    },
    
    # spectral QUBE (notionally supported; selected a test case for regression testing)
    "cube": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tar.gz'], # contains: LBL, DAT (data file), and JPG (browse image)
        "url_must_contain": ['cocirs', 'DATA/CUBE'],
        "label": ('.tar.gz', '.LBL'),
    },
    
    # RMS node supplemental data set
    # CIRS re-formated: simplified versions of variable-length files
    # APODSPEC - apodized, i.e. calibrated and resampled, spectra
    "rms_spec": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['DATA/APODSPEC'],
        "url_regex": [r'(COCIRS_5xxx)|(COCIRS_6xxx)'],
        "label": "D",
    },
    # GEODATA - position and viewing geometry of the planet and moons
    "rms_geo": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['DATA/GEO'],
        "url_regex": [r'(COCIRS_5xxx)|(COCIRS_6xxx)'],
        "label": "D",
    },
    # ISPMDATA - parameters describing each spectrum
    "rms_ispm": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['DATA/ISPMDATA'],
        "url_regex": [r'(COCIRS_5xxx)|(COCIRS_6xxx)'],
        "label": "D",
    },
    # POIDATA - pointing geometry on the planet or moon
    "rms_poi": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['DATA/POIDATA'],
        "url_regex": [r'(COCIRS_5xxx)|(COCIRS_6xxx)'],
        "label": "D",
    },
    # RINDATA - pointing geometry on the ring system
    "rms_rin": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['DATA/RINDATA'],
        "url_regex": [r'(COCIRS_5xxx)|(COCIRS_6xxx)'],
        "label": "D",
    },
    # TARDATA - listing of target bodies captured
    "rms_tar": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['DATA/TARDATA'],
        "url_regex": [r'(COCIRS_5xxx)|(COCIRS_6xxx)'],
        "label": "D",
    },
}
