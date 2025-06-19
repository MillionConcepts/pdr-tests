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
MANIFEST_FILE = "plasm_full"

file_information = {
        
    # MAG High-Resolution Premapping/Mapping Data
    "mag_high_res": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.STS'],
        "url_must_contain": ['MGS-M-MAG-3', 'MAPPING-HIGHRES', 'DATA'],
        "label": "D",
    },
    # MAG Data Archive; planetocentric coordinates
    "mag_pcc": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.STS'],
        "url_must_contain": ['MGS-M-MAG-3','FULLWORD-RES','DATA','PCENTRIC'],
        "label": "D",
    },
    # MAG Data Archive; sun-state coordinates
    "mag_ssc": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.STS'],
        "url_must_contain": ['MGS-M-MAG-3','FULLWORD-RES','DATA','SUNSTATE'],
        "label": "D",
    },
    
    # ER Data Archive; omni-directional flux
    "er_omni_flux": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.STS'],
        "url_must_contain": ['MGS-M-ER-3','OMNIDIR-FLUX','DATA'],
        "label": "D",
    },
    # ER Data Archive; angular flux
    "er_ang_flux": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.STS'],
        "url_must_contain": ['MGS-M-ER-4','ANGULAR-FLUX','DATA'],
        "label": "D",
    },
    # ER Map
    "er_map": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['MGS-M-ER-5-FIELD-MAP','DATA'],
        "label": "D",
    },

    # # Geometry products
    # "orbit_info": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['.TAB'],
    #     "url_must_contain": ['MGS-M-', '/GEOMETRY'],
    #     "label": "D",
    # },
    # "ancil_text": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['.KER'],
    #     "url_must_contain": ['MGS-M-', '/GEOMETRY'],
    #     "label": "D",
    # },
    # Spice kernels - support not planned
    "spice": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((TF)|(TPC)|(TI))$'],
        "url_must_contain": ['MGS-M-', '/GEOMETRY'],
        "label": "D",
        "support_np": True
    },
}
