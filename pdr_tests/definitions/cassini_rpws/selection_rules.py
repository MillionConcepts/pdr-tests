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
PPI_FILE = Path(MANIFEST_DIR, "plasm.parquet")

file_information = {
	
	# RPWS Langmuir Probe continuous current data
	"cont_current": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CO-SS_S-RPWS-3-LPCNTCUR', 'DATA'],
        "label": "D",
	},
	# RPWS Langmuir Probe sweep voltage-current data
	"volt_current": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CO-SS_S-RPWS-3-LPUI', 'DATA'],
        "label": "D",
	},
	# RPWS Langmuir Probe Sweep data
	"sweep": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CO-SS_S-RPWS-5-LPSWEEP', 'DATA'],
        "label": "D",
	},
	# RPWS Langmuir Probe proxy electron density data
	"proxy": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CO-SS_S-RPWS-5-NEPROXY', 'DATA'],
        "label": "D",
	},
	# telemetry data -- out of scope
	# from documentation: reformatted telemetry packets are not fixed length and are not well-suited to description by PDS labeling standards
#     "refdr_telemetry": {
#         "manifest": PPI_FILE,
#         "fn_must_contain": ['.PKT'],
#         "url_must_contain": ['CO-V_E_J_S_SS-RPWS-2-REFDR-ALL', 'DATA', 'RPWS_RAW_COMPLETE'],
#         "label": "D",
# 	},
	# full resolution wideband standard data products
    "refdr_wbr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['CO-V_E_J_S_SS-RPWS-2-REFDR-WBRFULL', 'DATA', 'RPWS_WIDEBAND_FULL'],
        "label": "D",
	},
	# full resolution waveform standard data products
    "refdr_wfr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['CO-V_E_J_S_SS-RPWS-2-REFDR-WFRFULL', 'DATA', 'RPWS_WAVEFORM_FULL'],
        "label": "D",
	},
	# calibrated low rate full resolution standard data products
	"rdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['CO-V_E_J_S_SS-RPWS-3-RDR-LRFULL', 'DATA', 'RPWS_LOW_RATE_FULL'],
        "label": "D",
	},
	# reduced temporal and spectral resolution spectral data
	"summ": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CO-V_E_J_S_SS-RPWS-4-SUMM-KEY60S', 'DATA', 'KEY_PARAMS'],
        "label": "D",
	},
}
