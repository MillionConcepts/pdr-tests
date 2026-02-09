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

"""
Chandrayaan-1 X-Ray Spectrometer (C1XS)
Data products have the following naming convention:

<instr-name>_<mission-phase><data-type><instr-dtype>_Rnnnnn.<extension>

Where:
C1XS            = instrument identifier
<mission-phase> = N (Normal Phase Operations)
<data-type>     = PDS data type (E)
<instr-dtype>   = Instrument data type abbreviation (see below)
Rnnnnn          = is the spacecraft orbit number
<extension>     = extension, TAB for the data products, LBL for the detached
                  label file.

Instrument data types:
HKD   Housekeeping Data
001   C1XS Time Tagged Events (not used)
002   C1XS Low Count Spectrum (not used)
XSM   XSM Spectral Data
006   C1XS Compressed Low Count Spectrum (not used)
CAX   C1XS Auxiliary Data
XAX   XSM Auxilliary Data
CZD   Auxiliary Data Detector Means
TTS   Time Tagged, single pixel data
TT3   Time Tagged, 3 pixel data
HRS   High resolution spectra

Examples:
C1XS_NEHKD_R00218.TAB
C1XS_NEHKD_R00218.LBL

There is an EDR folder and an REFDR folder. There is also a folder of data from
during "NOP".


"""

# variables naming specific parquet files in node_manifests
ESA_FILE = "img_esa_chan"

file_information = {
    "C1XS_HKD_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["HKD"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "EDR"],
        "label": "D"
    },
    "C1XS_XSM_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["XSM"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "EDR"],
        "label": "D"
    },
    "C1XS_CAX_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["CAX"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "EDR"],
        "label": "D"
    },
    "C1XS_XAX_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["XAX"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "EDR"],
        "label": "D"
    },
    "C1XS_CZD_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["CZD"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "EDR"],
        "label": "D"
    },
    "C1XS_TTS_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["TTS"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "EDR"],
        "label": "D"
    },
    "C1XS_TT3_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["TT3"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "EDR"],
        "label": "D"
    },
    "C1XS_HRS_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["HRS"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "EDR"],
        "label": "D"
    },
    #  CCS = CIXS calibrated spectrum
    "C1XS_CCS_REFDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["NECCS"],
        "url_must_contain": ["CHANDRAYAAN-1", "C1XS", "REFDR"],
        "label": "D"
    },
    "SARA_SWIM_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["SWIM"],
        "url_must_contain": ["CHANDRAYAAN-1", "-SWIM-", "SARA"],
        "label": "D",
        "support_np": True,
    },
    # SARA CENA also has .DAT files, but they are not mentioned in the labels
    # nor do they have labels of their own?
    "SARA_CENA_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".TAB"],
        "fn_must_contain": ["CENA"],
        "url_must_contain": ["CHANDRAYAAN-1", "-CENA-", "SARA"],
        "label": "D",
        "support_np": True,
    },
    # science spectral data AND housekeeping for SIR2, EDR
    "SIR2_SPECTRAL_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".FIT"],
        "fn_must_contain": ["_SC_"],
        "url_must_contain": ["CHANDRAYAAN-1", "SIR2"],
        "label": "D"
    },
    # housekeeping only for SIR2, EDR
    "SIR2_HOUSEKEEPING_EDR": {
        "manifest": ESA_FILE,
        "fn_ends_with": [".FIT"],
        "fn_must_contain": ["_HK_"],
        "url_must_contain": ["CHANDRAYAAN-1", "SIR2"],
        "label": "D"
    },
}
