"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .csv file that contains urls, file sizes, etc., scraped directly
from the hosting institution for this product type. for some data sets, all
urls will be found in the same .csv file; for others, they may be split
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
GEO_FILE = Path(MANIFEST_DIR, "geomsl.parquet")

file_information = {
    "CCD_FRAME": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ecc.*"],
        "url_must_contain": ["msl-m-apxs-2-edr"],
        "label": "D",
    },
    "DIFFRACTION_SINGLE": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ed1.*"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "DIFFRACTION_SPLIT": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*eds.*"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "DIFFRACTION_ALL": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*eda.*"],
        "url_must_contain": ["msl-m-apxs-2-edr"],
        "label": "D",
    },
    "ENERGY_ALL": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*eea.*"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "ENERGY_SINGLE": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ee1.*"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "ENERGY_SPLIT": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ees.*"],
        "url_must_contain": ["msl-m-apxs-2-edr"],
        "label": "D",
    },
    "FILM": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*efm.*"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "HOUSEKEEPING": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ehk.*"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "TRANSMIT_RAW": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*etr.*"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D"
    }
}
