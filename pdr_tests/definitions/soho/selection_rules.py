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
    # LASCO images
    "image": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['soho-c-lasco-4-cometimages-v1.0/data'],
        "label": "D",
    },
    # LASCO photometry
    "photom": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['soho-c-lasco-5-kreutzphotom-v1.0/data'],
        "label": "D",
    },

    # SBN's notes about the dataset
    "notes": {
        "manifest": SBN_FILE,
        "url_must_contain": ['soho-c-lasco-4-cometimages-v1.0/NOTES'],
        "label": "NA",
        "support_np": True,
    },
}

"""
    # SWAN derived data (PDS4)
    "swan": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['pds4-soho:swan_derived-v1.0/data'],
        "label": ('tab$','xml'),
    },
"""
