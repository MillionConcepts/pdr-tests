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

# Venus Express Radio Science (VRA, VeRa)
# level 2 are calibrated data after further processing
# level 1b are processed from level 1a into an ASCII file
# level 1a are raw tracking data
# - DATA
#      |     |
#      |     |- LEVEL1A
#      |            |- CLOSED_LOOP
#      |                 |-IFMS    IFMS closed-loop data files(Level 1a)
#      |                 |-DSN     DSN closed-loop data files (Level 1a)
#      |            |- OPEN_LOOP
#      |                 |-IFMS    IFMS open-loop data files  (Level 1a)
#      |                 |-DSN     DSN open-loop data files   (Level 1a)
#      |     |- LEVEL1b
#      |            |- CLOSED_LOOP
#      |                 |-IFMS    IFMS closed-loop data files(Level 1b)
#      |                 |-DSN     DSN closed-loop data files (Level 1b)
#      |            |- OPEN_LOOP
#      |                 |-IFMS    IFMS open-loop data files  (Level 1b)
#      |                 |-DSN     DSN open-loop data files   (Level 1b)
#      |     |- LEVEL02
#      |            |- CLOSED_LOOP
#      |                 |-IFMS    IFMS closed-loop data files (Level 2)
#      |                 |-DSN     DSN closed-loop data files  (Level 2)
#      |            |- OPEN_LOOP
#      |                 |-IFMS    IFMS open-loop data files   (Level 2)
#      |                 |-DSN     DSN open-loop data files    (Level 2)

# DSN = Deep Space Network
# IFMS = Intermediate Frequency Modulation System used by ESA ground station
# New Norcia

# variables naming specific parquet files in node_manifests
PSA = "img_esa_ve"

file_information = {
    # Level 1A Closed Loop IFMS  (RDR) (or UDR?)
    # checked
    "LV1A_CL_IFMS_AG2": {
        "manifest": PSA,
        "fn_must_contain": ['.RAW', '_AG2_'],
        "url_must_contain": ['VRA','LEVEL1A', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    "LV1A_CL_IFMS_AG1": {
        "manifest": PSA,
        "fn_must_contain": ['.RAW', '_AG1_'],
        "url_must_contain": ['VRA', 'LEVEL1A', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    "LV1A_CL_IFMS_D1X": {
        "manifest": PSA,
        "fn_must_contain": ['.RAW', '_D1X_'],
        "url_must_contain": ['VRA', 'LEVEL1A', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    "LV1A_CL_IFMS_D2X": {
        "manifest": PSA,
        "fn_must_contain": ['.RAW', '_D2X_'],
        "url_must_contain": ['VRA', 'LEVEL1A', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    "LV1A_CL_IFMS_D2S": {
        "manifest": PSA,
        "fn_must_contain": ['.RAW', '_D2S_'],
        "url_must_contain": ['VRA', 'LEVEL1A', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    # Level 2 Closed Loop DSN  (RDR)
    # checked
    "LV2_CL_DSN_DPX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_DPX_'],
        "url_must_contain": ['VRA','LEVEL02', 'CLOSED_LOOP', 'DSN'],
        "label": "D",
    },
    "LV2_CL_DSN_DPS": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_DPS_'],
        "url_must_contain": ['VRA', 'LEVEL02', 'CLOSED_LOOP', 'DSN'],
        "label": "D",
    },
    # Level 1B Closed Loop DSN (EDR)
    # subtypes of DPS, DPX, RMP
    # ramp table
    "LV1B_CL_DSN_RMP": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_RMP_'],
        "url_must_contain": ['VRA', 'LEVEL1B', 'CLOSED_LOOP', 'DSN'],
        "label": "D",
    },
    # doppler s band
    "LV1B_CL_DSN_DPS": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_DPS_'],
        "url_must_contain": ['VRA', 'LEVEL1B', 'CLOSED_LOOP', 'DSN'],
        "label": "D",
    },
    # doppler x band
    "LV1B_CL_DSN_DPX": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_DPX_'],
        "url_must_contain": ['VRA', 'LEVEL1B', 'CLOSED_LOOP', 'DSN'],
        "label": "D",
    },
    # Level 1B Closed Loop IFMS (EDR)
    # gain table
    "LV1B_CL_IFMS_AG1": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_AG1_'],
        "url_must_contain": ['VRA', 'LEVEL1B', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    # gain table
    "LV1B_CL_IFMS_AG2": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_AG2_'],
        "url_must_contain": ['VRA', 'LEVEL1B', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    # doppler table
    "LV1B_CL_IFMS_D1X": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_D1X_'],
        "url_must_contain": ['VRA', 'LEVEL1B', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    # doppler table
    "LV1B_CL_IFMS_D2X": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_D2X_'],
        "url_must_contain": ['VRA', 'LEVEL1B', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    # doppler table
    "LV1B_CL_IFMS_D2S": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_D2S_'],
        "url_must_contain": ['VRA', 'LEVEL1B', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    # # Level 1A Closed Loop DSN (UDR)
    # subtypes of ODF, TNF
    # checked
    "LV1A_CL_DSN_ODF": {
        "manifest": PSA,
        "fn_must_contain": ['.DAT', '_ODF_'],
        "url_must_contain": ['VRA','LEVEL1A', 'CLOSED_LOOP', 'DSN'],
        "label": "D",
    },
    "LV1A_CL_DSN_TNF": {
        "manifest": PSA,
        "fn_must_contain": ['.DAT', '_TNF_'],
        "url_must_contain": ['VRA', 'LEVEL1A', 'CLOSED_LOOP', 'DSN'],
        "label": "D",
    },
    # Level 2
    # doppler tables
    "LV2_CL_IFMS_D1X": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_D1X_'],
        "url_must_contain": ['VRA','LEVEL02', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    "LV2_CL_IFMS_D2S": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_D2S_'],
        "url_must_contain": ['VRA', 'LEVEL02', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    "LV2_CL_IFMS_D2X": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_D2X_'],
        "url_must_contain": ['VRA', 'LEVEL02', 'CLOSED_LOOP', 'IFMS'],
        "label": "D",
    },
    # Open Loop DSN (UDR)
    # subtypes of ODF, TNF
    # these are all "_RSR_" I believe
    "LV1A_OL_DSN": {
        "manifest": PSA,
        "fn_must_contain": ['.DAT', '_RSR_'],
        "url_must_contain": ['VRA', 'LEVEL1A', 'OPEN_LOOP', 'DSN'],
        "label": "D",
    },

}
