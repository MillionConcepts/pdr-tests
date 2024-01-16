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
SB_FILE = "tiny_sbnarchive"


file_information = {

# Cosmic Dust Analyzer (CDA)
	# Area Table: sensitive area of detector and analyzer
    "cda_area": {
        "manifest": SB_FILE,
        "fn_must_contain": ['AREA', '.TAB'],
        "url_must_contain": ['COCDA', 'DATA'],
        "label": "D",
    },
    # Status History: config, tests, etc
    "cda_stat": {
        "manifest": SB_FILE,
        "fn_must_contain": ['STAT', '.TAB'],
        "url_must_contain": ['COCDA', 'DATA'],
        "label": "D",
    },
    # Event Table: spacecraft geometry info
    "cda_events": {
        "manifest": SB_FILE,
        "fn_must_contain": ['EVENTS', '.TAB'],
        "url_must_contain": ['COCDA', 'DATA'],
        "label": "D",
    },
    # Spectra Table: time-of-flight mass spectra peaks
    # (volumes COCDA_0002 and COCDA_0003 appear to be the only ones with real data as of 2/14/23)
    "cda_spectra": {
        "manifest": SB_FILE,
        "fn_must_contain": ['SPECTRA', '.TAB'],
        "url_must_contain": ['DATA'],
        "url_regex": [r'(COCDA_0002)|(COCDA_0003)'],
        "label": "D",
    },
    # Settings Table: voltages
    "cda_settings": {
        "manifest": SB_FILE,
        "fn_must_contain": ['SETTINGS', '.TAB'],
        "url_must_contain": ['COCDA', 'DATA'],
        "label": "D",
    },
    # Couter Table: impact counter time history
    "cda_counter": {
        "manifest": SB_FILE,
        "fn_must_contain": ['COUNTER', '.TAB'],
        "url_must_contain": ['COCDA', 'DATA'],
        "label": "D",
    },
    # individual mass spectra, ion signals, election signals (IID and CAT targets), and induced charge signals
    "cda_signals": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['COCDA', 'DATA', 'SIGNALS'],
        "label": "D",
    },
    
# High Rate Detector (HRD)
    # raw data; NASA level 0, CODMAC level 2
    "hrd_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['cohrd', 'data/raw'],
        "label": "D",
    },
    # processed/calibrated data; NASA level 1-A, CODMAC level 3
    "hrd_processed": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['cohrd', 'data/processed'],
        "label": "D",
    },
    # calibration files
    "hrd_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['cohrd', 'data/calibrate'],
        "label": "D",
    },
    # instrument on-off times
    "hrd_onoff": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['cohrd', 'data/onoff'],
        "label": "D",
    },
    # instrument pointing and spacecraft position
    "hrd_point": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['cohrd', 'data/pointing'],
        "label": "D",
    },
}
