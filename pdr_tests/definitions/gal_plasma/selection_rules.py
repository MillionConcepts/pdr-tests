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
    # Plasma Analyzer (PLS)
    # EDRs are not supported (non-compliant PDS3 labels, PDS4 not available).
    # Calibrated/derived Jupiter products have PDS4 versions available.
    # Pre-Jupiter data is PDS3: Earth/Venus/Ida/Gaspra encounters
    "pls_pre_jupiter": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-', '-PLS-4-SUMM', '/DATA'],
        "url_regex": [r'(-GET-)|(-IET-)|(-EARTH)|(-VET-)'],
        "label": "D",
    },
    # support not planned - PLS EDRs are raw telemetry data
    "pls_edr_unsupported": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.PKT'],
        "url_must_contain": ['GO-J-PLS-2-EDR-RAW-TELEM-PACKETS-V1.0/DATA'],
        "label": "D",
        "support_np": True
    },
    
    
    # PLasma Wave Receiver (PWS)
    # EDRs - Wideband Waveform Data (1, 10, and 80 kHz)
    # TEXT and TIME_SERIES pointers consistently fail to open, TABLE sometimes
    # fails due to typos in labels.
##    "pws_edr": {
##        "manifest": PLASM_FILE,
##        "fn_must_contain": ['.DAT'],
##        "url_must_contain": ['/GO-', '-PWS-2-EDR-', '/DATA'],
##        "url_regex": [r'(WFRM-)|(WAVEFORM-)'],
##        "label": "D",
##    },
    # REDR - PRS and RTS spectrum analyzer data; ascii version
    "pws_redr_asc": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-J-PWS-2-REDR-', '-SA-FULL-V1.0/DATA/'],
        "label": "D",
    },
    # REDR - LRS and RTS spectrum analyzer data; binary version
    # Currently unsupported; error is potentially related to bit columns
##    "pws_redr_bi": {
##        "manifest": PLASM_FILE,
##        "fn_must_contain": ['.DAT'],
##        "url_must_contain": ['GO-J-PWS-2-REDR-', '-SA-FULL-V1.0/DATA/'],
##        "label": "D",
##    },
    # REFDR - LRS data from Gaspra, Ida, and Venus
    # Currently unsupported; error is potentially related to bit columns
##    "pws_refdr": {
##        "manifest": PLASM_FILE,
##        "fn_must_contain": ['.DAT'],
##        "url_must_contain": ['/GO-', '-PWS-2-REFDR-', '/DATA'],
##        "label": "D",
##    },
    # SUMM - The pre-Jupiter products undercount their row_bytes; a special 
    # case fixes this. (Two of the test cases represent these products.)
    "pws_summ": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['/GO-', '-PWS-4-SUMM-', '60S-V1.0/DATA'],
        "label": "D",
    },
    # DDR - Test case reads these with pd.read_csv()
    "pws_ddr": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['GO-J-PWS-5-DDR-PLASMA-DENSITY-FULL-V1.0/DATA'],
        "label": "D",
    },
}
