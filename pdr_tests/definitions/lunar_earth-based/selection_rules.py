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

# shorthand variables for specific .parquet files
MANIFEST_FILE = Path(MANIFEST_DIR, "geolunar.parquet")

file_information = {
    # Lunar Spectroscopy
    "spectra": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mk88-l-120cvf-3-rdr-120color-v1/', 'data'],
        "label": "D",
    },
    # 70 cm Lunar Radar
    "70cm_l1": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['arcb_nrao-l-rtls_gbt-4_5-70cm-v1', 'data/level1'],
        "label": "D",
    },
    "70cm_l2": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['arcb_nrao-l-rtls_gbt-4_5-70cm-v1', 'data/level2'],
        "label": "D",
    },
    # 12.6 cm (S-band) Lunar Radar
    "s-band": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['arcb_nrao-l-rtls_gbt-5-12.6cm-v1', 'data'],
        "label": "D",
    },
    # Midcourse Space Experiment (MSX) - infrared images in cube format
    # ENVI_HEADER does not open
    # data.show("QUBE") fails; things go wrong at line 82 in browsify.py
    # QUBE products open fine and look great during manual testing.
##    "msx": {
##        "manifest": MANIFEST_FILE,
##        "fn_must_contain": ['.qub'],
##        "url_must_contain": ['msx-l-spirit3-2_4-v1/msx_9001/data'],
##        "label": "D",
##    },
}
