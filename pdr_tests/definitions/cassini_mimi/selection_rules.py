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
	
	# uncalibrated data from CHEMS sensor
    "edr_chems": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['CO-E_J_S_SW-MIMI-2-CHEMS-UNCALIB', 'DATA'],
        "label": "D",
	},
	# uncalibrated data from INCA sensor
    "edr_inca": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['CO-E_J_S_SW-MIMI-2-INCA-UNCALIB', 'DATA'],
        "label": "D",
	},
	# uncalibrated data from LEMMS sensor
    "edr_lemms": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['CO-E_J_S_SW-MIMI-2-LEMMS-UNCALIB', 'DATA'],
        "label": "D",
	},
	
	# calibrated CHEMS data
    "rdr_chems_avg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['CO-S-MIMI-4-CHEMS-CALIB', 'DATA/CMAVG0'],
        "label": "D",
	},
    "rdr_chems_pha": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['CO-S-MIMI-4-CHEMS-CALIB', 'DATA/CPAVG0'],
        "label": "D",
	},
    "rdr_chems_fullres": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['CO-S-MIMI-4-CHEMS-CALIB', 'DATA/CMFULL0'],
        "label": "D",
	},
	
	# calibrated INCA data
    "rdr_inca": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['CO-S-MIMI-4-INCA-CALIB', 'DATA/I'],
        "label": "D",
	},

	# calibrated LEMMS data
    "rdr_lemms_avg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV', 'AVG'],
        "url_must_contain": ['CO-S-MIMI-4-LEMMS-CALIB', 'DATA/L'],
        "label": "D",
	},
	"rdr_lemms_fullres": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.csv', 'FULL'],
        "url_must_contain": ['CO-S-MIMI-4-LEMMS-CALIB', 'DATA/L'],
        "label": "D",
	},

    # ancillary products
    "edr_geom": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['CO-E_J_S_SW-MIMI-2-', 'GEOMETRY'],
        "label": "D",
    },
    # Most products do not open, others open wrong. Needs more testing
    # "rdr_ancil": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.CSV'],
    #     "url_must_contain": ['CO-S-MIMI-4-', 'DATA/ANCILLARY'],
    #     "label": "D",
    # },
    "spice": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TM'],
        "url_must_contain": ['DATA/ANCILLARY/KERNELS'],
        "url_regex": [r'(CO-E_J_S_SW-MIMI-2-)|(CO-S-MIMI-4-)'],
        "label": "D",
        "support_np": True
    },
	
}
