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
SBN_FILE = "tiny_other"

file_information = {    
    # HRI-VIS raw navigation images
    "hriv_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-hriv-2-nav-9p-', '/data/'],
        "label": "D",
    },
    # HRI-VIS calibrated nav images
    "hriv_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-hriv-3-nav-9p-', '/data/'],
        "label": "D",
    },
    # MRI-VIS raw navigation images
    "mri_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-mri-2-nav-9p-', '/data/'],
        "label": "D",
    },
    # MRI-VIS calibrated nav images
    "mri_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-mri-3-nav-9p-', '/data/'],
        "label": "D",
    },
    # ITS-VIS raw navigation images
    "its_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dii-', '-its-2-nav-9p-', '/data/'],
        "label": "D",
    },
    # ITS-VIS calibrated nav images
    "its_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dii-', '-its-3-nav-9p-', '/data/'],
        "label": "D",
    },
    # radio science - orbit data files
    # (eop, ion, and tro products do not have archive compliant labels)
    "rss": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.odf'],
        "url_must_contain": ['dif-c-rss-1-9p-encounter', '/data'],
        "label": "D",
    },
    "rss_support_np": {
        "manifest": SBN_FILE,
        "fn_regex": [r'((eop)|(ion)|(tro))$'],
        "url_must_contain": ['dif-c-rss-1-9p-encounter', '/data'],
        "label": "D", # no data pointers in the labels
        "support_np": True
    },
    # spacecraft instrument temperatures
    "temps": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['dif-c-hrii_hriv_mri-6-temps', '/data'],
        "label": "D",
    },
    # additional temperature logs
    "templog": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-2-ground-', 'data/templog'],
        "url_regex": [r'(dif-cal)|(dii-cal)'],
        "label": "D",
    },
    # pre-launch testing
    "testing": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['-2-ground-', '/data'],
        "url_regex": [r'(dif-)|(dii-)'],
        "label": "D",
    },
}
