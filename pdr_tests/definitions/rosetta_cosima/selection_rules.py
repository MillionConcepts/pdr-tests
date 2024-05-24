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
    # image data
    "image": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "D",
    },
    # grain list
    "grain": {
        "manifest": SB_FILE,
        "fn_must_contain": ['gr__.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    # housekeeping
    "hk": {
        "manifest": SB_FILE,
        "fn_must_contain": ['hk.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    # history product
    "history": {
        "manifest": SB_FILE,
        "fn_must_contain": ['hist.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    # named positions (Several products are just the attached label and an 
    # empty table. They fail to open, which is expected.)
    "position": {
        "manifest": SB_FILE,
        "fn_must_contain": ['position.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    # spectrum
    "spectrum": {
        "manifest": SB_FILE,
        "fn_must_contain": ['sp_','.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    # peak list
    "peak": {
        "manifest": SB_FILE,
        "fn_must_contain": ['pk_','.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    # scan data
    "scan": {
        "manifest": SB_FILE,
        "fn_must_contain": ['scan.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    # heating data
    "heat": {
        "manifest": SB_FILE,
        "fn_must_contain": ['heat.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    # cleaning data
    "clean": {
        "manifest": SB_FILE,
        "fn_must_contain": ['clea.tab'],
        "url_must_contain": ['ro-c-cosima-3-v6.0/data'],
        "label": "A",
    },
    
    # ground calibration data (similar to above ptypes, but with different 
    # format files)
    "ground_image": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ro-cal-cosima-3-v3.0/data'],
        "label": "D",
    },
    "ground_grain": {
        "manifest": SB_FILE,
        "fn_must_contain": ['gr__.tab'],
        "url_must_contain": ['ro-cal-cosima-3-v3.0/data'],
        "label": "A",
    },
    "ground_hk": {
        "manifest": SB_FILE,
        "fn_must_contain": ['hk.tab'],
        "url_must_contain": ['ro-cal-cosima-3-v3.0/data'],
        "label": "A",
    },
    "ground_history": {
        "manifest": SB_FILE,
        "fn_must_contain": ['hist.tab'],
        "url_must_contain": ['ro-cal-cosima-3-v3.0/data'],
        "label": "A",
    },
    "ground_spectrum": {
        "manifest": SB_FILE,
        "fn_must_contain": ['sp_','.tab'],
        "url_must_contain": ['ro-cal-cosima-3-v3.0/data'],
        "label": "A",
    },
    "ground_peak": {
        "manifest": SB_FILE,
        "fn_must_contain": ['pk_','.tab'],
        "url_must_contain": ['ro-cal-cosima-3-v3.0/data'],
        "label": "A",
    },
    "ground_scan": {
        "manifest": SB_FILE,
        "fn_must_contain": ['scan.tab'],
        "url_must_contain": ['ro-cal-cosima-3-v3.0/data'],
        "label": "A",
    },
    "ground_heat": {
        "manifest": SB_FILE,
        "fn_must_contain": ['heat.tab'],
        "url_must_contain": ['ro-cal-cosima-3-v3.0/data'],
        "label": "A",
    },
}


