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

# At Chang'e 4 they switched to PDS4 labels, detached with a variety of
# endings.

GEO_FILE = "change4"

file_information = {
    "ASAN_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_ASAN-SCI_SCI_N_20250729024000_20250729042000_0357_B.2BL"
        ],
        "label": "D",
    },
    # Landing Camera
    "LCAM_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_LCAM-1-5357_SCI_N_20190103022914_20190103022914_0001_A.2AL"
        ],
        "label": "D",
    },
    # Low-Frequency Radio Spectrometer (Transfer Relay)
    # this file is way too big for me to load
    "LFRS_TR_SCI_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_LFRS-TR_SCI_P_20210510013000_20210510140000_0167_B.2CL"
        ],
        "label": "D",
        "support_np": True
    },
    "LND_DPSL_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_LND-DPSL_SCI_P_20231009013000_20231020073000_0060_B.2AL"
        ],
        "label": "D",
    },
    "LND_ThN_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_LND-ThN_SCI_P_20231009013000_20231020073000_0060_B.2AL"
        ],
        "label": "D",
    },
    # Lunar Lander Neutron Dosimetry
    "LND_TID_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_LND-TID_SCI_P_20240305011500_20240316080000_0065_B.2AL"
        ],
        "label": "D",
    },
    # Lunar Penetrating Radar
    # these tables have a shape problem I haven't figured out
    "LPR1_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_LPR-1_SCI_N_20250224012500_20250303054500_0346_A.2BL"
        ],
        "label": "D",
        "support_np": True
    },
    "LPR2A_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_LPR-2A_SCI_N_20250224012500_20250303054500_0346_A.2BL"
        ],
        "label": "D",
        "support_np": True
    },
    "LPR2B_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_LPR-2B_SCI_N_20190104004000_20190109213900_0001_A.2BL"
        ],
        "label": "D",
        "support_np": True
    },
    # Panoramic Camera
    "PCAML_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_PCAML-Q-055_SCI_N_20250304065925_20250304065925_0347_B.2BL"
        ],
        "label": "D",
    },
    "PCAMR_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_PCAMR-Q-041_SCI_N_20250304063452_20250304063452_0347_B.2BL"
        ],
        "label": "D",
    },
    # Terrain Camera
    "TCAM_SCI_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_TCAM-I-069_SCI_N_20190111190323_20190111190323_0009_A.2CL"
        ],
        "label": "D",
    },
    # Visible and Near-Infrared Imaging Spectrometer
    "VNIS_SD_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_VNIS-SD_SCI_N_20250729024000_20250729042000_0357_B.2BL"
        ],
        "label": "D",
    },
    # The pd FWF or csv table reader can't handle things that aren't UTF-8.
    "VNIS_VD_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE4_GRAS_VNIS-VD_SCI_N_20250722010000_20250722023500_0356_B.2BL"
        ],
        "label": "D",
        "support_np": True
    },
}


