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

GEO_FILE = "change3"

file_information = {
    "EUVC_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_EUVC-1-043_SCI_N_20140221072325_20140221072325_0070_C.2B"
        ],
        "label": "A",
    },
    # Lunar Camera
    "LCAM_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_LCAM-4531_SCI_N_20131214131240_20131214131240_0001_A.2A"
        ],
        "label": "A",
    },
    # Lunar Penetrating Radar
    # Big tables! crash my computer
    # also all the data types are bit strings?
    "LPR1_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_LPR-1_SCI_N_20131220141301_20131220181800_0003_A.2A"
        ],
        "label": "A",
        "support_np": True,
    },
    # all the data types are bit strings?
    "LPR2B_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_LPR-2B_SCI_N_20131215171001_20131220141300_0002_A.2A"
        ],
        "label": "A",
        "support_np": True,
    },
    # Panoramic Cameras
    "PCAML_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_PCAML-C-035_SCI_N_20140112134924_20140112134924_0007_A.2A"
        ],
        "label": "A",
    },
    "PCAMR_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_PCAMR-C-037_SCI_N_20140112135113_20140112135113_0007_A.2A"
        ],
        "label": "A",
    },
    # Moon-Based Ultraviolet Telescope
    "MUVT_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_MUVT-F-0102_SCI_N_20150111211028_20150111211028_0394_B.2A"
        ],
        "label": "A",
    },
    # Particle-Induced X-Ray Spectrometer
    "PIXS_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_PIXS-C_SCI_N_20140112193801_20140114213300_0008_A.2A"
        ],
        "label": "A",
    },
    # Terrain Camera
    "TCAM_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_TCAM-I-214_SCI_P_20131223184802_20131223184802_0010_A.2A"
        ],
        "label": "A",
    },
    "TCAM_SCI_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_TCAM-I-078_SCI_P_20131224175512_20131224175512_0011_A.2B"
                          ],
        "label": "A",
    },
    # Visible and Near-Infrared Imaging Spectrometer
    "VNIS_CC_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_VNIS-CC_SCI_N_20131223023539_20131223023539_0005_A.2A"
        ],
        "label": "A",
    },
    # no valid PDS label attached, it's all binary
    "VNIS_CD_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_VNIS-CD_SCI_N_20131223021010_20131223021010_0005_A.2A"
        ],
        "label": "A",
        "support_np": True
    },
    "VNIS_SC_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_VNIS-SC_SCI_N_20131223023737_20131223023737_0005_A.2A"
        ],
        "label": "A",
    },
    "VNIS_SD_SCI_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE3_BMYK_VNIS-SD_SCI_N_20131223021320_20131223021320_0005_A.2A"
        ],
        "label": "A",
    },

}
