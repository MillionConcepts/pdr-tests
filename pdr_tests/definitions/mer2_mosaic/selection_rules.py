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
from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
IMG_FILE = Path(MANIFEST_DIR, "img_jpl_mer_coverage.parquet")

file_information = {
    # hazcam mosaics
    "haz": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mer2om_0xxx/data/hazcam'],
        "label": "A",
    },
    # microscopic imager mosaics
    "mi": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mer2om_0xxx/data/mi'],
        "label": "A",
    },
    # navcam mosaics / anaglyphs
    "nav": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'.{21}[lrmn]'],
        "url_must_contain": ['mer2om_0xxx/data/navcam'],
        "label": "A",
    },
    "nav_anaglyph": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'.{21}[a]'],
        "url_must_contain": ['mer2om_0xxx/data/navcam'],
        "label": "A",
    },
    # pancam mosaics / anaglyphs
    "pan": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'.{21}[lrmn]'],
        "url_must_contain": ['mer2om_0xxx/data/pancam'],
        "label": "A",
    },
    "pan_anaglyph": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'.{21}[a]'],
        "url_must_contain": ['mer2om_0xxx/data/pancam'],
        "label": "A",
    },
}

# irrelevant
SKIP_FILES = ["VICAR2.TXT", "GEOMETRIC_CM.TXT"]