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
    
    # LWP/LWR/SWP comets survey; extracted spectra
    "comet_extracted": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['iue-c','3-edr-iuecdb', '/data', '/ines'],
        "label": "D",
    },
    # LMX/SMX comets survey; raw spectra
    "comet_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['iue-c','3-edr-iuecdb', '/data', '/mx'],
        "label": "D",
    },
    # LSI/SSI comets survey; resampled images
    "comet_image": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['iue-c','3-edr-iuecdb', '/data', '/si'],
        "label": "D",
    },
    # LMX/SMX SL9; raw spectra
    "sl9_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['mx','.fit'],
        "url_must_contain": ['iue-j','3-edr-sl9', '/data/sl9'],
        "label": "D",
    },
    # LSI/SSI SL9; resampled images
    "sl9_image": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['si','.fit'],
        "url_must_contain": ['iue-j','3-edr-sl9', '/data/sl9'],
        "label": "D",
    },
}

