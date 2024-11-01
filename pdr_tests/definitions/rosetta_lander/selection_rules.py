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
SB_FILE = "tiny_rosetta"

file_information = {
    
# start APSX data products
    # each label is associated with multiple .tab data files
    "EDR_apxs": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.lbl'],
        "url_must_contain": ['-apxs-2-', '/data'],
        "label": "D",
    },
    
# start COSAC data products
    # for COSAC product types, one label can have multiple .tab data files
    "EDR_cosac": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.lbl'],
        "url_must_contain": ['-cosac-2-', '/data'],
        "label": "D",
    },
    "RDR_cosac": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.lbl'],
        "url_must_contain": ['-cosac-3-', '/data'],
        "label": "D",
    },

# start MUPUS data products
    "EDR_mupus": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-mupus-2-', '/data'],
        "label": "D",
    },
    "RDR_mupus": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-mupus-3-', '/data'],
        "label": "D",
    },

# start MODULUS/Ptolemy data products
    "EDR_ptolemy": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-ptolemy-2-', '/data'],
        "label": "D",
    },
    "RDR_ptolemy": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-ptolemy-3-', '/data'],
        "label": "D",
    },
    "DDR_ptolemy": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-ptolemy-5-', '/data'],
        "label": "D",
    },

# start ROLIS data products
    "EDR_rolis": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['-rolis-2-', '/data'],
        "label": "D",
    },
    "RDR_rolis": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['-rolis-3-', '/data'],
        "label": "D",
    },

# start ROMAP data products
    # each product has 1 label and multiple .tab files
    "EDR_romap": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.lbl'],
        "url_must_contain": ['-romap-2-', '/data'],
        "label": "D",
    },
    "RDR_romap": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.lbl'],
        "url_must_contain": ['-romap-3-', '/data'],
        "label": "D",
    },
    "DDR_romap": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-romap-5-', '/data'],
        "label": "D",
    },

# start SD2 data products
    # RECORD_TYPE and PRODUCT_TYPE are UND (undefined) in the EDR labels
    "EDR_sd2": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-sd2-3-', '/data/raw'],
        "label": "D",
        "support_np": True
    },
    "RDR_sd2": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-sd2-3-', '/data/calibrated'],
        "label": "D",
    },

# start SESAME data products
    # may want to break this down into smaller groups: some products have 1 label per multiple data files, some are 1-to-1
    "EDR_sesame": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.lbl'],
        "url_must_contain": ['-sesame-2-', '/data'],
        "label": "D",
    },
    "RDR_sesame": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.lbl'],
        "url_must_contain": ['-sesame-3-', '/data'],
        "label": "D",
    },

}


