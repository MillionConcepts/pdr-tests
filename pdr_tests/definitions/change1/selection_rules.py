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

GEO_FILE = "change1"

file_information = {

    # CCD Camera
    # image and labels open correctly
    "CCD_LVL3": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["CE1_BMYK_CCD_F001_21N171W_A.03"],
        "label": "A"
    },
    # no label?
    "CCD_B_LVL1": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["CE1_BMYK_CCD-B_SCI_N_20071223175846_20071223200554_0537_A.0"],
        "label": "A",
    },
    # Gamma Ray Spectrometer
    # table has wacky spacing that needs more sorting out to load without
    # splitting col values apart
    "GRS_LVL3": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["CE1_BMYK_GRS-A_20071128234222_20080206003829_256-1038_3_A.03"],
        "label": "A",
        "support_np": True,
    },
    # GRS science files
    "GRS_SCI_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
                "CE1_BMYK_GRS-A_SCI_P_20080721212255_20080721233010_2925_B.2C"
        ],
        "label": "A",
        },
    "GRS_SCI_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
                "CE1_BMYK_GRS-A_SCI_P_20081225203511_20081225223350_4719_B.01"
        ],
        "label": "A",
        },
    # High Energy Particle Detector, Science Files
    "HPD_SCI_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_HPD_SCI_P_20071126123804_20071126144547_0229_B.01"
        ],
        "label": "A",
        },
    # Interference Imaging
    # Line pre/suffixes not aligned with array element size are not supported.
    "IIM_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_IIM_SCI_N_20080606112139_20080606132849_2411_A.01"
        ],
        "label": "A",
        "support_np": True
    },
    "IIM_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_IIM_SCI_N_20080518220500_20080519001244_2201_A.2A"
        ],
        "label": "A",
    },
    # Laser Altimeter
    "LAM_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_LAM_SCI_P_20071223175846_20071223200554_0537_B.01"
        ],
        "label": "A",
    },
    "LAM_LVL2A": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_LAM_SCI_P_20090112155429_20090112175309_4935_B.2A"
        ],
        "label": "A",
    },
    "LAM_LVL2B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_LAM_SCI_P_20071130014613_20071130035352_0269_B.2B"
        ],
        "label": "A",
    },
    # Microwave Radiometer
    # Engineering / DN file?
    "MRM_DN_LVL03": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_MRM_20071204032632_20071231112657_0315_A_19_DN.03"
        ],
        "label": "A",
    },
    # low frequency channel
    "MRM_L_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_MRM-L_SCI_P_20090107230854_20090108010736_4878_B.01"
        ],
        "label": "A",
    },
    # thermal channel
    "MRM_T_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_MRM-T_SCI_P_20090107230854_20090108010736_4878_B.01"
        ],
        "label": "A",
    },
    # Solar Wind Ion Detector A & B
    "SWID_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_SWIDA_SCI_P_20080610233008_20080611013752_2462_A.01"
        ],
        "label": "A",
    },
    "SWID_LVL3B": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_SWIDA_SCI_P_20071127074729_20071127095510_0238_A_1.3B"
        ],
        "label": "A",
    },
    # X-Ray Spectrometer
    # LC1
    "XRS_L1_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_XRS-L1_SCI_P_20080117030352_20080117051103_0813_B.01"
        ],
        "label": "A",
    },
    # Scatter Component
    "XRS_SC_LVL01": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_XRS-SC_SCI_P_20080117030352_20080117051103_0813_B.01"
        ],
        "label": "A",
    },
    # Solar Excitation
    "XRS_SE_LVL2C": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "CE1_BMYK_XRS-SE_SCI_P_20071127224124_20071128004908_0245_B.2C"
        ],
        "label": "A",
    },
}
