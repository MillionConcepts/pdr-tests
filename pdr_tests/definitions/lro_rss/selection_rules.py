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
MANIFEST_FILE = Path(MANIFEST_DIR, "geolro.parquet")

file_information = {
    # Laser Ranging full rate; text files
    "range_full": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.fr'],
        "url_must_contain": ['lro-l-rss-1-tracking-v1', 'data/range'],
        "label": 'D',
    },
    # Laser Ranging normal point; text files
    "range_norm": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.npt'],
        "url_must_contain": ['lro-l-rss-1-tracking-v1', 'data/range'],
        "label": 'D',
    },
    # Small Forces Files, parameters for thruster calibration; text files
    "sff": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.txt'],
        "url_must_contain": ['lro-l-rss-1-tracking-v1', 'data/sff'],
        "label": 'D',
    },
    # Tracking data; binary tables
    "trk": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.trk'],
        "url_must_contain": ['lro-l-rss-1-tracking-v1', 'data/trk'],
        "label": 'D',
    },
    # Weather information; ASCII tables
    "wea": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.wea'],
        "url_must_contain": ['lro-l-rss-1-tracking-v1', 'data/wea'],
        "label": 'D',
    },
}
