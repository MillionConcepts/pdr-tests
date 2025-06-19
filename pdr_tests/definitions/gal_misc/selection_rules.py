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
PLASM_FILE = "plasm_full"
ATM_FILE = "atm"
SBN_FILE = "tiny_sbnarchive"

file_information = {
    # PHOTOPOLARIMETER RADIOMETER
    # R_EDR data prior to arrival at Jupiter
    "ppr_edr_early": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['/GO-', '-PPR-2-EDR-', '/DATA'],
        "label": "D",
    },
    # RDR data prior to arrival at Jupiter
    "ppr_rdr_early": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['/GO-', '-PPR-3-RDR-', '/DATA'],
        "label": "D",
    },
    # R_EDR data from Jupiter mission phase onwards
    "ppr_edr_late": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['gopr_500', '/r_edr'],
        "label": "D",
    },
    # RDR data from Jupiter mission phase onwards
    "ppr_rdr_late": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['gopr_500', '/rdr'],
        "label": "D",
    },

    # Positional Dataset
    # spacecraft trajectory; there are a handful of table formats used here
    # (multiple test cases are selected)
    "sc_traj": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "fn_regex": [r'(TRAJ)|(CRDS)'],
        "url_must_contain": ['/GO-', '-POS-6-', '/DATA'],
        "label": "D",
    },
    # spacecraft trajectory derived from spice kernels
    "sc_traj_derived": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['/GO-', '-POS-6-SUMM-', '/DATA'],
        "label": "D",
    },
    # rotor attitude
    "rotor_attitude": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['/GO-', '-POS-6-REDR-ROTOR', '/DATA'],
        "label": "D",
    },
    # spice kernels
    "spice": {
        "manifest": PLASM_FILE,
        "fn_regex": [r'((BSP)|(TLS)|(TPC)|(TSC))$'],
        "url_must_contain": ['GO-', '-POS-6-', 'EXTRAS/SPICE'],
        "label": "D",
        "support_np": True
    },

    # Miscellaneous Ida and Gaspra products at the Small Bodies Node
    # Light Curves (data is .dat, supporting products are .tab)
    "light_curves": {
        "manifest": SBN_FILE,
        "fn_regex": [r'(tab)|(dat)'],
        "url_must_contain": ['sbnig_0001/data/lightcurves'],
        "label": "D",
    },
    # Spectra
    "spectra": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sbnig_0001/data/spectra'],
        "label": "D",
    },

    # uplink archive (most files are .txt or .pdf)
    "uplink": {
        "manifest": PLASM_FILE,
        "fn_regex": [r'((tab)|(TAB))$'],
        "url_must_contain": ['GO-J_JSA_X_V_E_A_C-UPL-V1.0/DATA'],
        "label": "D", # incomplete labels
        "support_np": True
    },
    "uplink_other": {
        "manifest": PLASM_FILE,
        "fn_must_contain": ['.data'],
        "url_must_contain": ['GO-J_JSA_X_V_E_A_C-UPL-V1.0/DATA'],
        "label": "A", # no PDS label
        "support_np": True
    },
}
