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

    # PDS4: low rate spectrum analyzer, and raw waveform data (VG1/VG2)
    
    # Jupiter RDR, SUMM, and DDR (VG1/VG2)
    "jup_rdr_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['J-PWS-2-RDR-SA-4.0SEC', '/DATA'],
        "label": "D",
    },
    "jup_rdr_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['J-PWS-2-RDR-SA-4.0SEC', '/DATA'],
        "label": "D",
    },
    "jup_summ": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['J-PWS-4-SUMM-SA-48.0SEC', '/DATA'],
        "label": "D",
    },
    "jup_ddr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['VG', 'J-PWS-5-DDR', '/DATA'],
        "label": "D",
    },

    # Saturn RDR and SUMM (VG1/VG2)
    # filenames are repeated between VG1 and VG2 (manually tested the repeats)
    "sat_rdr_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['S-PWS-2-RDR-SA-4.0SEC', '/DATA'],
        "label": "D",
    },
    "sat_rdr_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['S-PWS-2-RDR-SA-4.0SEC', '/DATA'],
        "label": "D",
    },
    "sat_summ": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['S-PWS-4-SUMM-SA-48SEC', '/DATA'],
        "label": "D",
    },

    # Solar System SUMM and ancillary products (VG1/VG2)
    # filesnames are repeated so VG1 and VG2 are separated for testing
    "sys_summ_vg1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG1-J_S_SS-PWS-4-SUMM-SA1HOUR', '/DATA/HOUR1'],
        "label": "D",
    },
    "sys_summ_vg2": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-J_S_U_N_SS-PWS-4-SUMM-SA1HOUR', '/DATA/HOUR2'],
        "label": "D",
    },
    "sys_ancillary": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['SS-PWS-4-SUMM-SA1HOUR', '/DATA/ANCILLARY'],
        "label": "D",
    },

    # Uranus RDR and SUMM (all VG2)
    "ur_rdr_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-PWS-2-RDR-SA-4SEC', '/DATA'],
        "label": "D",
    },
    "ur_rdr_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-PWS-2-RDR-SA-4SEC', '/DATA'],
        "label": "D",
    },
    "ur_summ_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-PWS-4-SUMM-SA-48SEC', '/DATA'],
        "label": "D",
    },
    "ur_summ_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-PWS-4-SUMM-SA-48SEC', '/DATA'],
        "label": "D",
    },

    # Neptune RDR and SUMM (all VG2)
    "nep_rdr_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PWS-2-RDR-SA-4SEC', '/DATA'],
        "label": "D",
    },
    "nep_rdr_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-N-PWS-2-RDR-SA-4SEC', '/DATA'],
        "label": "D",
    },
    "nep_summ_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PWS-4-SUMM-SA-48SEC', '/DATA'],
        "label": "D",
    },
    "nep_summ_asc": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((TAB)|(BRO))$'],
        "url_must_contain": ['VG2-N-PWS-4-SUMM-SA-48SEC', '/DATA'],
        "label": "D",
    },

    # Extras - support not planned; no PDS labels
    # (also they're "not subject to PDS standards")
    "extras_splash": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.SPH'],
        "url_must_contain": ['VG', '-PWS-', '/EXTRAS/SPLASH'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    "extras_cdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.cdr'],
        "url_must_contain": ['VG', '-PWS-', '/EXTRAS'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    "extras_dos": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((CFG)|(HLP)|(OBJ)|(DSK)|(MAK)|(PRJ))$'],
        "url_must_contain": ['VG', '-PWS-', '/EXTRAS/DOS'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    "extras_ico": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.ICO'],
        "url_must_contain": ['VG', '-PWS-', '/EXTRAS'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    # Spice kernels - support not planned
    "spice": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((TLS)|(TPC)|(TSP))$'],
        "url_must_contain": ['VG', '-PWS-', '/EXTRAS/SPICE'],
        "label": "D",
        "support_np": True
    },
    # Ancillary tables 
    # Low priority for support; they're already easy to read CSV files
    # "UserWarning: Unable to load SPREADSHEET: <class 'pandas.errors.EmptyDataError'>: No columns to parse from file"
    "summ_filter": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['VG', '-PWS-4-SUMM-', '/DATA'],
        "label": "D",
        "support_np": True
    },
}

