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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
ATM_FILE = Path(MANIFEST_DIR, "atm.parquet")

file_information = {
	
# Experiment data
    # Gravity experiment 
    "grav": {
        "manifest": ATM_FILE,
        "fn_regex": [r'\.[0-9][^0-9][0-9]'],
        "url_must_contain": ['cors_'],
        "url_regex": [r'((GR)|(gr)).*((RSR)|(rsr))'],
        "label": "D",
    },
    # Gravitational wave experiment
    "grav_wave": {
        "manifest": ATM_FILE,
        "fn_regex": [r'\.[0-9][^0-9][0-9]'],
        "url_must_contain": ['cors_'],
        "url_regex": [r'((GW)|(gw)).*((RSR)|(rsr))'],
        "label": "D",
    },
    # occultation experiment
    "occul": {
        "manifest": ATM_FILE,
        "fn_regex": [r'\.[0-9][^0-9][0-9]'],
        "url_must_contain": ['cors_'],
        "url_regex": [r'((OC)|(oc)).*((RSR)|(rsr))'],
        "label": "D",
    },
    # Solar Conjunction and Solar Characterization Experiments
	"solar": {
        "manifest": ATM_FILE,
        "fn_regex": [r'\.[0-9][^0-9][0-9]'],
        "url_must_contain": ['cors_'],
        "url_regex": [r'((SC)|(sc)).*((RSR)|(rsr))'],
        "label": "D",
    },
    # Bistatic Experiment
	"bist": {
        "manifest": ATM_FILE,
        "fn_regex": [r'\.[0-9][^0-9][0-9]'],
        "url_must_contain": ['cors_'],
        "url_regex": [r'((BI)|(bi)).*((RSR)|(rsr))'],
        "label": "D",
    },
    
# Misc logs, telemetry, monitoring, etc.
    # 158    Monitor File (0158-Monitor)
    "158": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.158'],
        "url_must_contain": ['cors_', '158'],
        "label": "D",
    },
    # 515    Monitor File (Mon-5-15)
    "515": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.515'],
        "url_must_contain": ['cors_', '515'],
        "label": "D",
    },
	# ODF    Orbit Data File
	"odf": {
        "manifest": ATM_FILE,
        "fn_regex": [r'(ODF$)|(odf$)'],
        "url_must_contain": ['cors_'],
        "url_regex": [r'(ODF)|(odf)'],
        "label": "D",
    },
	# TDF    Archival Tracking Data File
	"tdf": {
        "manifest": ATM_FILE,
        "fn_regex": [r'(TDF$)|(tdf$)'],
        "url_must_contain": ['cors_'],
        "url_regex": [r'(TDF)|(tdf)'],
        "label": "D",
    },
	# TLM    Telemetry File
	"tlm": {
        "manifest": ATM_FILE,
        "fn_regex": [r'(TLM$)|(tlm$)'],
        "url_must_contain": ['cors_'],
        "url_regex": [r'(TLM)|(tlm)'],
        "label": "D",
    },
    
# products with labels lacking pointer to 'data' file:
# 
# 	# LOG	log file 
# 	"log": {
#         "manifest": ATM_FILE,
#         "url_must_contain": ['cors_'],
#         "url_regex": [r'(/LOG)|(/log)'],
#         "label": "D",
#     },
# 	# PD1    Path Delay Data File from AWVR1
# 	"pd1": {
#         "manifest": ATM_FILE,
#         "fn_regex": [r'(.PD1)|(.pd1)'],
#         "url_must_contain": ['cors_'],
#         "url_regex": [r'(PD1)|(pd1)'],
#         "label": "D",
#     },
#     # PD2    Path Delay Data File from AWVR2
#     "pd2": {
#         "manifest": ATM_FILE,
#         "fn_regex": [r'(.PD2)|(.pd2)'],
#         "url_must_contain": ['cors_'],
#         "url_regex": [r'(PD2)|(pd2)'],
#         "label": "D",
#     },
#     # TNF
# 	"tnf": {
#         "manifest": ATM_FILE,
#         "fn_regex": [r'(.TNF)|(.tnf)'],
#         "url_must_contain": ['cors_'],
#         "url_regex": [r'(TNF)|(tnf)'],
#         "label": "D",
#     },
# 	# EOP    Earth Orientation Parameters File
# 	"eop": {
#         "manifest": ATM_FILE,
#         "fn_regex": [r'(.EOP)|(.eop)'],
#         "url_must_contain": ['cors_'],
#         "url_regex": [r'(EOP)|(eop)'],
#         "label": "D",
#     },
# 	# ION    Ionosphere Calibration File
# 	"ion": {
#         "manifest": ATM_FILE,
#         "fn_regex": [r'(.ION)|(.ion)'],
#         "url_must_contain": ['cors_'],
#         "url_regex": [r'(ION)|(ion)'],
#         "label": "D",
#     },
# 	# TRO    Troposphere Calibration File
# 	"tro": {
#         "manifest": ATM_FILE,
#         "fn_regex": [r'(.TRO)|(.tro)'],
#         "url_must_contain": ['cors_'],
#         "url_regex": [r'(TRO)|(tro)'],
#         "label": "D",
#     },
	
}
