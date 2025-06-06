"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .parquet file that contains urls, file sizes, etc., scraped
directly from the hosting institution for this product type. for some data
sets, all urls will be found in the same .parquet file; for others, they may
be split between nodes or scraping sessions.

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
IMG_FILE = "img_jpl_mer_mosaic"

file_information = {
    # hazcam mosaics
    "haz": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mer','om_0xxx/data/hazcam'],
        "label": "A",
    },
    # microscopic imager mosaics / anaglyphs
    "mi": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'^.{21}[lrmn]'],
        "url_must_contain": ['mer','om_0xxx/data/mi'],
        "label": "A",
    },
    "mi_anaglyph": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'^.{21}[a]'],
        "url_must_contain": ['mer','om_0xxx/data/mi'],
        "label": "A",
    },
    # navcam mosaics / anaglyphs
    "nav": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'^.{21}[lrmn]'],
        "url_must_contain": ['mer','om_0xxx/data/navcam'],
        "label": "A",
    },
    "nav_anaglyph": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'^.{21}[a]'],
        "url_must_contain": ['mer','om_0xxx/data/navcam'],
        "label": "A",
    },
    # pancam mosaics / anaglyphs
    "pan": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'^.{21}[lrmn]'],
        "url_must_contain": ['mer','om_0xxx/data/pancam'],
        "label": "A",
    },
    "pan_anaglyph": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'^.{21}[a]'],
        "url_must_contain": ['mer','om_0xxx/data/pancam'],
        "label": "A",
    },

    # Support not planned:
    # List of images used in the mosaic products
    "image_list": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.lis'],
        "url_must_contain": ['mer','om_0xxx/data/'],
        "label": "NA",
        "support_np": True
    },
    # Pointing correction files for some mosaics
    "pointing_correction": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.nav'],
        "url_must_contain": ['mer','om_0xxx/data/'],
        "label": "NA",
        "support_np": True
    },
}

# irrelevant
SKIP_FILES = ["VICAR2.TXT", "GEOMETRIC_CM.TXT"]
