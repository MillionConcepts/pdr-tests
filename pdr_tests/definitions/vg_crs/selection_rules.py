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
    
    # PDS4: Jupiter (VG1/VG2) and Saturn (VG1)
    
    # RDR (Neptune, VG2)
    "rdr": {
        "manifest": PPI_FILE,
        "fn_regex": ['(TAB)|(DAT)$'],
        "url_must_contain": ['VG2-N-CRS-3-RDR-D1-6SEC-V1.0/DATA'],
        "label": "D",
    },
    # SUMM D1/D2 (Saturn, VG2)
    "summ_saturn": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-S-CRS-4-SUMM-D1_D2-192SEC-V1.0/DATA'],
        "label": "D",
    },
    
    # The binary products are grouped by detector and the ascii products are
    # grouped by target. This is to avoid repeated filenames ending up in the
    # same index/folder during ix testing.
    
    # SUMM D1 (Binary products, Uranus and Neptune, VG2)
    "summ_d1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-', '-CRS-4-SUMM-D1-96SEC-V1.0/DATA'],
        "label": "D",
    },
    # SUMM D2 (Binary products, Uranus and Neptune, VG2)
    "summ_d2": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-', '-CRS-4-SUMM-D2-96SEC-V1.0/DATA'],
        "label": "D",
    },
    # SUMM Uranus (Ascii products, D1 and D2, VG2)
    "summ_uranus": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-CRS-4-SUMM-D', '-96SEC-V1.0/DATA'],
        "label": "D",
    },
    # SUMM Neptune (Ascii products, D1 and D2, VG2)
    "summ_neptune": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-N-CRS-4-SUMM-D', '-96SEC-V1.0/DATA'],
        "label": "D",
    },
    
    # Extras - support not planned
    "extras_splash": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((SPH)|(ABS)|(DAT)|(DES)|(HED))$'],
        "url_must_contain": ['VG2-S-CRS-4-SUMM-','/EXTRAS/SPLASH'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    "extras_cdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.cdr'],
        "url_must_contain": ['VG2-', '-CRS-', '/EXTRAS'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    # Spice kernels - support not planned
    "spice": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((TLS)|(TPC)|(TSP)|(TC))$'],
        "url_must_contain": ['VG2-', '-CRS-', '/EXTRAS/SPICE'],
        "label": "D",
        "support_np": True
    },
    # Ancillary - support not planned
    "ancil_csv": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['VG', '-CRS-', '/DATA'],
        "label": "A", # no PDS labels
        "support_np": True
    },
}

