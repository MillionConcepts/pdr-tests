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
MANIFEST_FILE = "geomgs"

file_information = {
    
    # derived thermal inertia maps; well-label 2-dimensional arrays
    "timap": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-tes-', '-timap-', '/data'],
        "label": "D",
    },
    # projected thermal inertia maps; well-label 2-dimensional arrays
    "special": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-tes-', '-special-'],
        "label": "D",
    },
    # Ancillary tables - It looks like there are 5 tables that are duplicated 
    # across all tsdr volumes.
    # .tab files in the data/mars directory are mirrored (and supported) at the 
    # ASU node's TES archive (their commented out GEO selection rules are below)
    "tsdr_ancillary": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mgs-m-tes-3-tsdr-v2'],
        "url_regex": [r'/data$'],
        "label": "D",
    },
    
    # Support not planned; missing PDS3 compliant labels
    # (These products are mirrored in the ASU Node's TES archive.)
    # raw interferogram data (.var); variable length table
    "tsdr_IFG_data": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['ifg', '.var'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
        "support_np": True
    },
    # raw and calibrated radiance data (.var); variable length table
    "tsdr_RAD_data": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['rad', '.var'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
        "support_np": True
    },
}

"""

# The following products are duplicates of the ASU Node's TES Standard Data Record

    # derived atmospheric data; well-labeled fixed length table
    "tsdr_ATM": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['atm', '.tab'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
    },
    # raw and calibrated bolometer data; well-labeled fixed length table
    "tsdr_BOL": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['bol', '.tab'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
    },
    # derived positional data; well-labeled fixed length table; IAU-1994 coords
    "tsdr_GEO": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['geo', '.tab'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
    },
    # interferogram metadata (.tab); well-labeled fixed length table
    "tsdr_IFG_tab": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['ifg', '.tab'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
    },
    # observation parameters; well-labeled fixed length table
    "tsdr_OBS": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['obs', '.tab'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
    },
    # raw positional data; well-labeled fixed length table
    "tsdr_POS": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['pos', '.tab'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
    },
    # raw and calibrated radiance metadata (.tab); well-labeled fixed length table
    "tsdr_RAD_tab": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['rad', '.tab'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
    },
    # auxiliary observation parameters; well-labeled fixed length table
    "tsdr_TLM": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['tlm', '.tab'],
        "url_must_contain": ['-tes-', '-tsdr-', '/mars'],
        "label": "A",
    },
"""
