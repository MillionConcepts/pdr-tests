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

# variables naming specific parquet files in node_manifests
PPI_FILE = "esa_smart1"

file_information = {
    # AMIE: Advanced Moon Micro-imager Experiment
    "AMIE_EDR_EEP_V1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.IMG', 'AMI'],
        "url_must_contain": ['AMIE/S1-L-X-AMIE-2-EDR-EEP-V1.0', 'DATA'],
        "label": "A",
    },
    "AMIE_EDR_EEP_V1.1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.IMG', 'AMI'],
        "url_must_contain": ['AMIE/S1-L-X-AMIE-2-EDR-EEP-V1.1', 'DATA'],
        "label": "A",
    },
    "AMIE_EDR_EP_V1.0": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.IMG', 'AMI'],
        "url_must_contain": ['AMIE/S1-L-X-AMIE-2-EDR-EP-V1.0', 'DATA'],
        "label": "A",
    },
    "AMIE_EDR_EP_V1.1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.IMG', 'AMI'],
        "url_must_contain": ['AMIE/S1-L-X-AMIE-2-EDR-EP-V1.1', 'DATA'],
        "label": "A",
    },
    "AMIE_EDR_LP_V1.0": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.IMG', 'AMI'],
        "url_must_contain": ['AMIE/S1-L-X-AMIE-2-EDR-LP-V1.0', 'DATA'],
        "label": "A",
    },
    "AMIE_EDR_LP_V1.1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.IMG', 'AMI'],
        "url_must_contain": ['AMIE/S1-L-X-AMIE-2-EDR-LP-V1.1', 'DATA'],
        "label": "A",
    },
    "AMIE_RDR_EEP_V1.0": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.IMG', 'AMI'],
        "url_must_contain": ['AMIE/S1-L-X-AMIE-3-RDR-EEP-V1.0', 'DATA'],
        "label": "A",
    },
    "AMIE_RDR_EEP_V1.1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.IMG', 'AMI'],
        "url_must_contain": ['AMIE/S1-L-X-AMIE-3-RDR-EEP-V1.1', 'DATA'],
        "label": "A",
    },
    # not in manifest?
    # "AMIE_RDR_EP_V1.0": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.IMG', 'AMI'],
    #     "url_must_contain": ['AMIE/S1-L-X-AMIE-3-RDR-EP-V1.0', 'DATA'],
    #     "label": "A",
    # },
    # "AMIE_RDR_EP_V1.1": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.IMG', 'AMI'],
    #     "url_must_contain": ['AMIE/S1-L-X-AMIE-3-RDR-EP-V1.1', 'DATA'],
    #     "label": "A",
    # },
    # "AMIE_RDR_LP_V1.0": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.IMG', 'AMI'],
    #     "url_must_contain": ['AMIE/S1-L-X-AMIE-3-RDR-LP-V1.0', 'DATA'],
    #     "label": "A",
    # },
    # "AMIE_RDR_LP_V1.1": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.IMG', 'AMI'],
    #     "url_must_contain": ['AMIE/S1-L-X-AMIE-3-RDR-LP-V1.1', 'DATA'],
    #     "label": "A",
    # },
    # D-CIXS: Demonstraction of a Compact X-ray Spectrometer
    "DCIXS_EDR_EP": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB', 'DCIXS'],
        "url_must_contain": ['S1-L-DCIXS-2-EDR-EP-V1.0', 'DATA'],
        "label": "D",
    },
    "DCIXS_EDR_LP": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB', 'DCIXS'],
        "url_must_contain": ['S1-L-DCIXS-2-EDR-LP-V1.0', 'DATA'],
        "label": "D",
    },
    "DCIXS_EDR_EEP": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB', 'DCIXS'],
        "url_must_contain": ['S1-X-DCIXS-2-EDR-EEP-V1.0', 'DATA'],
        "label": "D",
    },
    # SIR2: Smart-1 Infrared Spectrometer
    "SIR2_EDR_EEP": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FIT', 'SIR'],
        "url_must_contain": ['S1-L-X-SIR-2-EDR-EEP-V1.0', 'DATA'],
        "label": "D",
    },
    "SIR2_EDR_EP": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FIT', 'SIR'],
        "url_must_contain": ['S1-L-X-SIR-2-EDR-EP-V1.0', 'DATA'],
        "label": "D",
    },
    "SIR2_EDR_LP": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FIT', 'SIR'],
        "url_must_contain": ['S1-L-X-SIR-2-EDR-LP-V1.0', 'DATA'],
        "label": "D",
    },
    # SPEDE: Spacecraft Potential, Electron and Dust Experiment
    "SPEDE_EDR_BKGRPLASMA": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-2-EDR-BKGRPLASMA-V1.0', 'DATA'],
        "label": "A",
    },
    "SPEDE_EDR_MONITORING": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-2-EDR-', 'EP-MONITORING-V1.', 'DATA'],
        "label": "A",
    },
    "SPEDE_EDR_LEOP_CAL": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-2-EDR-LEOP-CALIBRATION', 'DATA'],
        "label": "A",
    },
    "SPEDE_EDR_SW": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-2-EDR-SOLAR-WIND', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_BKGRPLASMA_EF": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['EF_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-BKGRPLASMA', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_BKGRPLASMA_PD_40": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['PD_40_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-BKGRPLASMA', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_BKGRPLASMA_HK": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['HK_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-BKGRPLASMA', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_EP_MONITOR_EF": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['EF_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-EP-MONITORING-', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_EP_MONITOR_PD_40": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['PD_40_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-EP-MONITORING-', 'DATA'],
        "label": "A",
    },
    # there is a monitoring1 and monitoring2 folder
    "SPEDE_REFDR_EP_MONITOR_HK": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['HK_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-EP-MONITORING', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_LEOP_CAL_EF": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['EF_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-LEOP-CALIBRATION', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_LEOP_CAL_PD_40": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['PD_40_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-LEOP-CALIBRATION', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_LEOP_CAL_HK": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['HK_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-LEOP-CALIBRATION', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_SW_EF": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['EF_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-SOLAR-WIND', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_SW_PD_40": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['PD_40_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-SOLAR-WIND', 'DATA'],
        "label": "A",
    },
    "SPEDE_REFDR_SW_HK": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['HK_CAL.TAB', 'SP'],
        "url_must_contain": ['S1-X-SPEDE-4-REFDR-SOLAR-WIND', 'DATA'],
        "label": "A",
    },
    # not in manifest?
    # XSM: x-ray solar monitor
    # "XSM_EDR_EEP": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.DAT'],
    #     "url_must_contain": ['S1-X-XSM-2-EDR-EEP-', 'DATA'],
    #     "label": "D",
    # },
    # "XSM_EDR_EP": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.DAT'],
    #     "url_must_contain": ['S1-X-XSM-2-EDR-EP-', 'DATA'],
    #     "label": "D",
    # },
    # "XSM_EDR_LP": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.DAT'],
    #     "url_must_contain": ['S1-X-XSM-2-EDR-LP-', 'DATA'],
    #     "label": "D",
    # },

}
