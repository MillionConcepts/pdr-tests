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

GEO_FILE = "change2"

file_information = {
    "CCD_GEO_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_CCD-B02_GEO_N_20101126083608_20101126103405_0601_A.2C"
        ],
        "label": "A",
    },
    "CCD_SCI_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_CCD-F10_SCI_N_20101126083608_20101126103405_0601_A.2C"
        ],
        "label": "A",
    },
    # Gamma-Ray Spectrometer
    "GRS_SCI_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_GRS-A_SCI_P_20101015085002_20101015104805_0088_A.2C"
        ],
        "label": "A",
    },
    # Laser Altimeter
    "LAM_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_LAM_SCI_P_20101015164224_20101015184030_0092_A.2B"
        ],
        "label": "A",
    },
    # Microwave Radiometer
    "MRM_L_SCI_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_MRM-L_SCI_P_20110511034542_20110511054334_2626_A.2C"
        ],
        "label": "A",
    },
    # Solar Wind Ion Detector
    "SWID_A_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_SWIDA_SCI_P_20110205022956_20110205042747_1464_A.2B"
        ],
        "label": "A",
    },
    "SWID_B_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_SWIDB_SCI_P_20110207132550_20110207152342_1494_A.2B"
        ],
        "label": "A",
    },
    # X Ray Spectrometer
    "XRS_LLE1_SCI_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_XRS-LLE1_SCI_P_20110212052303_20110212072055_1551_A.2C"
        ],
        "label": "A",
    },
    "XRS_SE_SCI_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE2_BMYK_XRS-SE_SCI_P_20110212052303_20110212072055_1551_A.2C"
        ],
        "label": "A",
    },
}
