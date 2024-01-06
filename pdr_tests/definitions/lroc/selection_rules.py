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
MANIFEST_FILE = "img_lroc"

file_information = {
    "NAC_CDR_if": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["M", ".IMG"],
        "url_must_contain": ["NAC"],
        "label": "A",
    },
    "NAC_CDR_rad": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["S", ".IMG"],
        "url_must_contain": ["NAC"],
        "label": "A",
    },
    "WAC_CDR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": [".IMG"],
        "url_must_contain": ["WAC"],
        "label": "A",
    },
    "NAC_EDR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": [".IMG"],
        "url_must_contain": ["NAC"],
        "label": "A",
    },
    "WAC_EDR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": [".IMG"],
        "url_must_contain": ["WAC"],
        "label": "A",
    },
    "NAC_DTM": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_DTM", ".TIF"],
        "url_must_contain": ["/DATA/"],
        "label": "D",
    },
    "NAC_PHO": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_PHO", ".IMG"],
        "label": "A",
    },
    "NAC_POLE": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_POLE", ".IMG"],
        "label": "A",
    },
    "NAC_POLE_PSR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_POLE_PSR", ".IMG"],
        "label": "A",
    },
    "NAC_ROI": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_ROI", ".IMG"],
        "label": "A",
    },
    "WAC_CSHADE": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_CSHADE", ".IMG"],
        "label": "A",
    },
    "WAC_EMP": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_EMP", ".IMG"],
        "label": "A",
    },
    "WAC_EMP_tl": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_EMP", ".TIF"],
        "url_must_contain": ["/DATA/"],
        "label": "D",
    },
    "WAC_HAPKE": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_HAPKE", ".IMG"],
        "label": "A",
    },
    "WAC_HAPKE_tl": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_HAPKE", ".TIF"],
        "url_must_contain": ["/DATA/"],
        "label": "D",
    },
    "WAC_HAPKE_PARAMMAP": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_HAPKEPARAMMAP", ".IMG"],
        "label": "A",
    },
    "WAC_GLD100": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_GLD100", ".IMG"],
        "label": "A",
    },
    "WAC_GLOBAL": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_GLOBAL", ".IMG"],
        "label": "A",
    },
    "WAC_MOVIE": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_MOVIE", ".IMG"],
        "label": "A",
    },
    "WAC_ORBITS": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_ORBITS", ".IMG"],
        "label": "A",
    },
    "WAC_POLE_ILL": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_POLE_ILL", ".IMG"],
        "label": "A",
    },
    "WAC_ROI": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_ROI", ".IMG"],
        "label": "A",
    },
    "WAC_TIO2": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_TIO2", ".IMG"],
        "label": "A",
    },
    "ANAGLYPH": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["ANAGLYPH", ".TIF"],
        "label": "D",
    },
}
