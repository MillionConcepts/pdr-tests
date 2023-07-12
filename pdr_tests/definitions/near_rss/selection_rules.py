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
SBN_FILE = Path(MANIFEST_DIR, "tiny.parquet")


file_information = {
    # Eros and Mathilde ODF data
    "odf": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.'],
        "url_must_contain": ['NEAR_A_RSS_1_5', '/odf'],
        "label": "D",
    },
    # Eros gravity acceleration maps
    "grav_map": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['NEAR_A_RSS_5_EROS_GRAVITY_V1_0/erosgrav'],
        "label": "D",
    },
    # Eros spherical harmonic gravity model (ascii)
    "grav_asc": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.sha'],
        "url_must_contain": ['NEAR_A_RSS_5_EROS_GRAVITY_V1_0/erosgrav'],
        "label": "D",
    },
    # Eros spherical harmonic gravity model (binary)
    "grav_bin": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.shb'],
        "url_must_contain": ['NEAR_A_RSS_5_EROS_GRAVITY_V1_0/erosgrav'],
        "label": "D",
    },
    # table of Eros landmarks
    "landmark": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['NEAR_A_RSS_5_EROS_GRAVITY_V1_0/erosgrav'],
        "label": "D",
    },
}
