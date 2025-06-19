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
    
    # PDS4: VG1 jupiter and saturn
    # Safed: cruise phase (VG1/VG2)
    
    # spacecraft position data near jupiter in RTN and S3 coordinates
    "jupiter": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-J-POS-6-SUMM', '/DATA'],
        "label": "D",
    },
    # spacecraft position data near saturn in RTN and L1 coordinates
    "saturn": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-S-POS-4-SUMM', '/DATA'],
        "label": "D",
    },
    # spacecraft position data near uranus in RTN and U1 coordinates
    "uranus": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-POS-5-SUMM', '/DATA'],
        "label": "D",
    },
    # spacecraft position data near neptune in RTN and NLS coordinates
    "neptune": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-N-POS-5-SUMM', '/DATA'],
        "label": "D",
    },
    
    # "original binary" versions of the uranus and neptune products
    "ur_hg_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-POS-5-SUMM-HGCOORDS-48SEC-V1.0',
                             '/DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
    "ur_u1_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-POS-5-SUMM-U1COORDS-48SEC-V1.0',
                             '/DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
    "nep_hg_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-POS-5-SUMM-HGCOORDS-48SEC-V1.0',
                             '/DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
    "nep_nls_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-POS-5-SUMM-NLSCOORDS-12SEC-V1.0',
                             '/DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
    
    # Safed datasets:
    # VG1 and VG2 cruise phase position/trajectory data
    "cruise": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG','-SS-POS-6-1DAY-V1.0/DATA'],
        "label": "D",
    },

    # Extras - support not planned
    "extras_splash": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((SPH)|(ABS)|(DAT)|(DES)|(HED))$'],
        "url_must_contain": ['VG2-', '-POS-', '/EXTRAS/SPLASH'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    "extras_cdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.cdr'],
        "url_must_contain": ['VG2-', '-POS-', '/EXTRAS'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    # Spice kernels - support not planned
    "spice": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((TLS)|(TPC)|(TSP)|(TC))$'],
        "url_must_contain": ['VG2-', '-POS-', '/EXTRAS/SPICE'],
        "label": "D",
        "support_np": True
    },
    # Ancillary - support not planned
    "ancil_csv": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['VG', '-POS-', '/DATA'],
        "label": "A", # no PDS labels
        "support_np": True
    },
}

