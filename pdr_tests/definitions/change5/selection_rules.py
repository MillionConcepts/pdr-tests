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

GEO_FILE = "change5"

file_information = {
    # Landing Camera
    "LCAM_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE5-L_GRAS_LCAM-1-0388_SCI_N_20201201151036_20201201151036_0001_A.2AL"
        ],
        "label": "D",
    },
    # Lunar Mineralogical Spectrometer
    # have to make sure to have both the SCI file and
    # AUX data file
    "LMS_C_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE5-L_GRAS_LMS-C-C000_SCI_N_20201202165629_20201202170410_0019_A.2BL"
        ],
        "label": "D",
    },
    # Lunar Mineralogical Spectrometer (Mid-Infrared Channel)
    "LMS_M_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE5-L_GRAS_LMS-M-C000_SCI_N_20201202165629_20201202170410_0019_A.2BL"
        ],
        "label": "D",
    },
    "LMS_N_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE5-L_GRAS_LMS-N-C000_SCI_N_20201202165629_20201202170410_0019_A.2BL"
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
            "CE5-L_GRAS_LRPR-A_SCI_N_20201201215911_20201201221639_0001_A.01L"
        ],
        "label": "D",
        "support_np": True
    },
    "LRPR_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE5-L_GRAS_LRPR-A_SCI_N_20201130092304_20201130094032_0001_A.2BL"
        ],
        "label": "D",
        "support_np": True
    },
    # Panoramic Camera (Left)
    "PCAML_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE5-L_GRAS_PCAML-I-008_SCI_N_20201203054903_20201203054903_0004_A.2BL"
        ],
        "label": "D",
    },
    # Panoramic Camera (Right)
    "PCAMR_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE5-L_GRAS_PCAMR-I-008_SCI_N_20201203054903_20201203054903_0004_A.2BL"
        ],
        "label": "D",
    },
}
