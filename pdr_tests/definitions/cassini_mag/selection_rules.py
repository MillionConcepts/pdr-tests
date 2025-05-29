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
PPI_FILE = "plasm_full"

file_information = {
	
	# raw consolidated data (VHM, FGM)
    "redr_sci": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD', '_SD'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-2-REDR-RAW-DATA', 'DATA', 'MRDCD'],
        "label": "D",
    },
    # housekeeping data
    "redr_hk": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD'],
        "fn_regex": [r'(_HK)|(_SH)'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-2-REDR-RAW-DATA', 'DATA', 'MRDCD'],
        "label": "D",
    },
    # spacecraft attitude data
	"redr_att": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD', 'CHATT'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-2-REDR-RAW-DATA', 'DATA', 'SCDCD'],
        "label": "D",
    },
    # channelized data with user-selected channels
	"redr_usr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD', 'CHUSR'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-2-REDR-RAW-DATA', 'DATA', 'SCDCD'],
        "label": "D",
    },
    	
	# calibrated scalar helium magnetometer science data
	"shm_sci": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD', '_SDSHM'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-3-RDR-CALIB-SHM', 'DATA'],
        "label": "D",
    },
    # scalar helium magnetometer housekeeping data
    "shm_hk": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD', '_HKSHM'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-3-RDR-CALIB-SHM', 'DATA'],
        "label": "D",
    },
        
	# processed/calibrated magnetic field data (full resolution)
	"rdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-3-RDR-FULL-RES', 'DATA'],
        "label": "D",
    },
    # processed/calibrated magnetic field data (second averages)
	"summ_sec": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-4-SUMM-1SECAVG', 'DATA'],
        "label": "D",
    },
    # processed/calibrated magnetic field data (minute averages)
    "summ_min": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-4-SUMM-1MINAVG', 'DATA'],
        "label": "D",
    },
    # spice kernels
    "summ_spice": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.MK'],
        "url_must_contain": ['CO-E_SW_J_S-MAG-4-SUMM-1MINAVG', 'GEOMETRY'],
        "label": "D",
        "support_np": True
    },
    
}

# Useful acronym and filename explanations from the dataset's documentation:
	
	# MRDCD = MAG raw consolidated data (VHM, FGM) and calibrated data (SHM)
	# _SD = science data
	# FGM = fluxgate magnetometer (raw)
	# VHM = vector helium mag (raw)
	# SHM = scalar helium mag (calibrated)
	# _HK = housekeeping
	# _SH = housekeeping
	# CON = configuration image data (housekeeping)
	# ANA = analog housekeeping
	# ERR = error counter
	# CMD = command validation info
	
	# SCDCD = spacecraft consolidated data
	# CH = channelized
	# ATT = attitude info
	# USR = user-selected channels
