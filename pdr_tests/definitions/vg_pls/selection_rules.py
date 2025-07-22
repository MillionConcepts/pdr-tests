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

# variables naming specific parquet files in node_manifests
PPI_FILE = "plasm_full"

file_information = {

    # PDS4: VG1 Jupiter, Saturn, and Solar System; VG2 Jupiter
    
    # VG2 Saturn
    "sat_ascii": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-S-PLS-5-SUMM', '/DATA'],
        "label": "D",
    },

    # VG2 Uranus
    "ur_elefit": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-PLS-5-RDR-ELEFIT', '/DATA'],
        "label": "D",
    },
    "ur_ionfit": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-PLS-5-RDR-IONFIT', '/DATA'],
        "label": "D",
    },
    "ur_elebr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-PLS-5-SUMM-ELEBR', '/DATA'],
        "label": "D",
    },
    "ur_ionbr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-PLS-5-SUMM-IONBR', '/DATA'],
        "label": "D",
    },
    # ascii versions of the 4 product types above
    "ur_ascii": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-PLS-5', '/DATA'],
        "label": "D",
    },
    
    # VG2 Neptune
    "nep_pro_sphere": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PLS-5-RDR-2PROMAGSPH', '/DATA'],
        "label": "D",
    },
    "nep_wind": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PLS-5-RDR-IONINBNDWIND', '/DATA'],
        "label": "D",
    },
    "nep_l_mode": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PLS-5-RDR-IONLMODE', '/DATA'],
        "label": "D",
    },
    "nep_ion_sphere": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PLS-5-RDR-IONMAGSPHERE', '/DATA'],
        "label": "D",
    },
    "nep_m_mode": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PLS-5-RDR-IONMMODE', '/DATA'],
        "label": "D",
    },
    # ascii versions of the 6 product types above
    "nep_ascii": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-N-PLS-5-RDR', '/DATA'],
        "label": "D",
    },
    
    # VG2 Solar System
    # fine resolution plasma data
    "sys_fine_res": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-SS-PLS-3-RDR-FINE-RES', '/DATA'],
        "label": "D",
    },
    # plasam daily averages
    "sys_1day_avg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-SS-PLS-4-SUMM-1DAY-AVG', '/DATA'],
        "label": "D",
    },
    # plasma hourly averages
    "sys_1hr_avg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-SS-PLS-4-SUMM-1HR-AVG', '/DATA'],
        "label": "D",
    },

    # Support not planned; missing pointers in the labels.
    # Adding pointers manually leads to an error: "UserWarning: Unable to load
    # TIME_SERIES: 'utf-8' codec can't decode byte 0xc6 in position 1: invalid
    # continuation byte"
    "nep_ele_sphere": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PLS-5-RDR-ELEMAGSPHERE', '/DATA'],
        "label": "D",
        "support_np": True
    },

    # Extras - support not planned
    "extras_splash": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((SPH)|(ABS)|(DAT)|(DES)|(HED))$'],
        "url_must_contain": ['VG2-', '-PLS-', '/EXTRAS/SPLASH'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    "extras_cdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.cdr'],
        "url_must_contain": ['VG2-', '-PLS-', '/EXTRAS'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    "extras_dlc": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((ABS)|(DES)|(HED))$'],
        "url_must_contain": ['VG', '-PLS-', '/EXTRAS/DLC'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    # The .DAT products do have labels and are supported
    "extras_dlc_dat": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG', '-PLS-', '/EXTRAS/DLC'],
        "label": "D",
    },
    # Spice kernels - support not planned
    "spice": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((TLS)|(TPC)|(TSP)|(TC)|(ASC))$'],
        "url_must_contain": ['VG2-', '-PLS-', '/EXTRAS/SPICE'],
        "label": "D",
        "support_np": True
    },
}

