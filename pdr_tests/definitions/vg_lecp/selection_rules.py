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
    
    # VG1 - RDR far encounter (Jupiter, Saturn)
    "vg1_rdr_far": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['VG1-', 'LECP-3-RDR-FAR-ENC-400MSEC', '/DATA'],
        "label": "D",
    },
    # VG2 - RDR far encounter (Jupiter, Saturn, Uranus, Neptune)
    "vg2_rdr_far": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['VG2-', 'LECP-3-RDR-FAR-ENC-400MSEC', '/DATA'],
        "label": "D",
    },
    # VG1 - RDR near encounter (Jupiter)
    "vg1_rdr_near": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['VG1-', 'LECP-3-RDR-NEAR-ENC-400MSEC', '/DATA'],
        "label": "D",
    },
    # VG2 - RDR near encounter (Saturn)
    "vg2_rdr_near": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['VG2-', 'LECP-3-RDR-NEAR-ENC-400MSEC', '/DATA'],
        "label": "D",
    },
    
    # Jupiter RDR step
    "j_rdr_step": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['J-LECP-3-RDR-STEP', '/DATA'],
        "label": "D",
    },
    # Jupiter SUMM average
    "j_summ_average": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['J-LECP-4-SUMM-AVERAGE-15MIN', '/DATA'],
        "label": "D",
    },
    # Jupiter SUMM sector
    # The VG1 products open correctly with a special case. The VG2 product 
    # does not open because of typos in the data file's END_TIME column.
    "j_summ_sector_vg1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG1-J-LECP-4-SUMM-SECTOR-15MIN', '/DATA'],
        "label": "D",
    },
##    "j_summ_sector_vg2": {
##        "manifest": PPI_FILE,
##        "fn_must_contain": ['.TAB'],
##        "url_must_contain": ['VG2-J-LECP-4-SUMM-SECTOR-15MIN', '/DATA'],
##        "label": "D",
##    },
    
    # Saturn RDR step
    "s_rdr_step": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['S-LECP-3-', 'STEP', '/DATA'],
        "label": "D",
    },
    # Saturn SUMM average (ix testing missed the VG2 product because of repeated
    # filenames between VG1 and VG2. It was manually tested instead.)
    "s_summ_average": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['S-LECP-4-SUMM-AVERAGE-15MIN', '/DATA'],
        "label": "D",
    },
    # Saturn SUMM sector
    # VG1 does not open because of typos in the data file's END_TIME column.
    # VG2 opens fine.
##    "s_summ_sector_vg1": {
##        "manifest": PPI_FILE,
##        "fn_must_contain": ['.TAB'],
##        "url_must_contain": ['VG1-S-LECP-4-SUMM-SECTOR-15MIN', '/DATA'],
##        "label": "D",
##    },
    "s_summ_sector_vg2": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-S-LECP-4-SUMM-SECTOR-15MIN', '/DATA'],
        "label": "D",
    },
    
    # Uranus RDR step 6.4min
    "u_rdr_step": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['U-LECP-3-STEP-6.4MIN', '/DATA'],
        "label": "D",
    },
    # Uranus RDR step 12.8min (formatted differently from LECP-3-RDR-STEP)
    "u_rdr_step_12.8": {
        "manifest": PPI_FILE,
        "fn_regex": [r'(TAB)|(DAT)$'], # ascii and binary versions available
        "url_must_contain": ['U-LECP-4-RDR-STEP-12.8MIN', '/DATA'],
        "label": "D",
    },
    # Uranus RDR sector
    "u_rdr_sector": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'], # only the ascii versions are supported
        "url_must_contain": ['U-LECP-4-RDR-SECTOR-15MIN', '/DATA'],
        "label": "D",
    },
    # Uranus SUMM average
    "u_summ_average": {
        "manifest": PPI_FILE,
        "fn_regex": [r'(TAB)|(DAT)$'], # ascii and binary versions available
        "url_must_contain": ['U-LECP-4-SUMM-AVERAGE-15MIN', '/DATA'],
        "label": "D",
    },
    # Uranus SUMM scan
    "u_summ_scan": {
        "manifest": PPI_FILE,
        "fn_regex": [r'(TAB)|(DAT)$'], # ascii and binary versions available
        "url_must_contain": ['U-LECP-4-SUMM-SCAN-24SEC', '/DATA'],
        "label": "D",
    },
    
    # Neptune RDR step
    "n_rdr_step": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['N-LECP-3-RDR-STEP', '/DATA'],
        "label": "D",
    },
    # Neptune RDR step 12.8min (formatted differently from LECP-3-RDR-STEP)
    "n_rdr_step_12.8": {
        "manifest": PPI_FILE,
        "fn_regex": [r'(TAB)|(DAT)$'], # ascii and binary versions available
        "url_must_contain": ['N-LECP-4-RDR-STEP-12.8MIN', '/DATA'],
        "label": "D",
    },
    # Neptune SUMM scan
    "n_summ_scan": {
        "manifest": PPI_FILE,
        "fn_regex": [r'(TAB)|(DAT)$'], # ascii and binary versions available
        "url_must_contain": ['N-LECP-4-SUMM-SCAN-24SEC', '/DATA'],
        "label": "D",
    },
    
}

