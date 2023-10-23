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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
SB_FILE = Path(MANIFEST_DIR, "tiny.parquet")

file_information = {
    
    # post-launch raw and calibrated data
    "launch_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-alice-2-launch-v2.0/data'],
        "label": "D",
    },
    "launch_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-alice-3-launch-v2.0/data'],
       "label": "D",
   },
    # jupiter flyby raw and calibrated data
    "jupiter_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-j-alice-2-jupiter-v2.0/data'],
        "label": "D",
    },
    "jupiter_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-j-alice-3-jupiter-v2.0/data'],
       "label": "D",
   },
    # pluto cruise raw and calibrated data
    "cruise_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-alice-2-plutocruise-v2.0/data'],
        "label": "D",
    },
    "cruise_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-alice-3-plutocruise-v2.0/data'],
       "label": "D",
   },
    # pluto encounter raw and calibrated data
    "pluto_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-p-alice-2-pluto-v3.0/data'],
        "label": "D",
    },
    "pluto_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-p-alice-3-pluto-v3.0/data'],
       "label": "D",
   },
    
    # extended mission - cruise 1
    "kem_cruise_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-alice-2-kemcruise1-v2.0/data'],
        "label": "D",
    },
    "kem_cruise_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-alice-3-kemcruise1-v2.0/data'],
       "label": "D",
   },
    # extended mission - encounter 1, Arrokoth
    "arrokoth_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-a-alice-2-kem1-v4.0/data'],
        "label": "D",
    },
    "arrokoth_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-a-alice-3-kem1-v4.0/data'],
       "label": "D",
   },
}