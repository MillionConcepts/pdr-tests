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
SB_FILE = "tiny_sbnarchive"

file_information = {
    "REDR": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['GO-', '-MAG-', '-REDR-'],
        "label": "D",
    },
    # ancillary(?) table - raw engineering data
    "REDR_eng": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['GO-', '-MAG-', '-REDR-', 'DATA/ENG'],
        "label": "D",
    },
    "RDR_tab": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-', '-MAG-', '-RDR-'],
        "label": "D",
    },
    "RDR_dat": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['GO-', '-MAG-', '-RDR-'],
        "label": "D",
    },
    # Currently not supported due to incorrect format file, support not planned
    "SUMM": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['GO-', '-MAG-', '-SUMM-'],
        "label": "D",
        "support_np": True
    },
    
    # SBN's Ida and Gaspra specific subset of mag data
    "small_bodies": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['galileo/idagaspra', 'data/galileo_mag'],
        "label": "D",
    },

    # EDR officially unsupported.
    "EDR": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['GO-', '-MAG-', '-EDR-'],
        "label": "D",
        "support_np": True
    },
    # spice kernels
    "spice": {
        "manifest": PLASM_FILE,
        "fn_regex": [r'((BSP)|(TLS)|(TPC)|(TSC))$'],
        "url_must_contain": ['GO-', '-MAG-', '-RDR-', 'EXTRAS/SPICE'],
        "label": "D",
        "support_np": True
    },
    # (maybe) software files; no PDS labels
    "misc": {
        "manifest": PLASM_FILE,
        "fn_regex": [r'((mpsh)|(opt))$'],
        "url_must_contain": ['GO-J-MAG-3-RDR-MAGSPHERIC-SURVEY-V1.0',
                             'DATA/SURVEY'],
        "label": "A",
        "support_np": True
    },
}
