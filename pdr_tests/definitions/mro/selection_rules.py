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
ATM_FILE = "atm"
IMG_FILE = "img_usgs_mars-reconnaissance-orbiter"
IMG_HIRISE_FILE = "img_hirise"

file_information = {
    # HiRISE EDR
    "hirise_edr": {
        "manifest": IMG_HIRISE_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/EDR/'],
        "label": "A",
    },
    # HiRISE RDR
    "hirise_rdr": {
        "manifest": IMG_HIRISE_FILE,
        "fn_must_contain": ['.JP2'],
        "url_must_contain": ['PDS/RDR/'],
        "label": "D",
    },
    # HiRISE DTM
    # Most DTM images are JP2 with detached labels, some products also have an 
    # IMG version with attached labels.
    "hirise_dtm": {
        "manifest": IMG_HIRISE_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/DTM/'],
        "label": "A",
    },
    "hirise_dtm_jp2": {
        "manifest": IMG_HIRISE_FILE,
        "fn_must_contain": ['.JP2'],
        "url_must_contain": ['PDS/DTM/'],
        "label": "D",
    },
    # CTX EDR
    "ctx_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['CTX/mrox_', '/data'],
        "label": "A",
    },
    # MARCI EDR
    "marci_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['MARCI/mrom_', '/data'],
        "label": "A",
    },
    # MCS EDR
    "mcs_edr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['EDR.TAB'],
        "url_must_contain": ['MROM_0', '/DATA'],
        "label": "D",
    },
    # MCS RDR
    "mcs_rdr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['RDR.TAB'],
        "url_must_contain": ['MROM_1', '/DATA'],
        "label": "D",
    },
    # Format issues, alerting node
    # MCS DDR
    "mcs_ddr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['DDR.TAB'],
        "url_must_contain": ['MROM_2', '/DATA'],
        "label": "D",
        "support_np": True
    },
}

SKIP_FILES = ["JP2INFO.TXT", "DSMAP.CAT"]
