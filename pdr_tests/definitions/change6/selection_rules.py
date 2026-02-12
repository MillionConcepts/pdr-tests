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
# For all Chang'e missions, this is referencing a "fake" manifest with one
# example file for each dtype, just so I can run ix.
# For Chang'e files, it's not possible to scrape the website & download them
# the way we do with the PDS.

GEO_FILE = "change6"

file_information = {
    # LCAM
    "LCAM_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE6-L_GRAS_LCAM-1-0632_SCI_N_20240601222715_20240601222715_0001_A.2AL"
        ],
        "label": "D",
    },
    # Lunar Regolith Penetrating Radar
    # these have a field_format that is None, doesn't work with pds4_tools
    # table structure. so I would have to modify pds4_tools a bit or parse
    # the xml label for the table structure myself. or modify the xml file?
    "LRPR_A_SCI_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE6-L_GRAS_LRPR-A_SCI_N_20240530131533_20240530133300_0001_A.01L"
        ],
        "label": "D",
        "support_np": True
    },
    # Lunar Mineralogical Spectrometer (Mid-Infrared Channel)
    "LMS_M_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE6-L_GRAS_LMS-M-D000_SCI_N_20240603141409_20240603142143_0023_A.2BL"
        ],
        "label": "D",
    },
    # Lunar Mineralogical Spectrometer
    # must have both SCI and AUX files 
    "LMS_C_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE6-L_GRAS_LMS-C-D000_SCI_N_20240603141409_20240603142143_0023_A.2BL"
        ],
        "label": "D",
    },
    "LMS_N_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE6-L_GRAS_LMS-N-D000_SCI_N_20240603141409_20240603142143_0023_A.2BL"
        ],
        "label": "D",
    },
    "LMS_S_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE6-L_GRAS_LMS-S-D000_SCI_N_20240603141409_20240603142143_0023_A.2BL"
        ],
        "label": "D",
    },
    "PCAML_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE6-L_GRAS_PCAML-I-118_SCI_N_20240603134930_20240603134930_0004_A.2BL"
        ],
        "label": "D",
    },
}
