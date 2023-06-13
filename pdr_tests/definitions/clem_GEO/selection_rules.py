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
MANIFEST_FILE = Path(MANIFEST_DIR, "geolunar.parquet")

file_information = {
    
    # thermal images; RDRs
    "lwir": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['clem1-l-lwir-3-rdr', '/data'],
        "label": "A",
    },
    # 'safed' data in the archive. It opens fine but isn't a priority for maintained support.
    "lidar": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['clem1-l-lidar-3-topo', '/data'],
        "label": "D",
    },
    # topography derived from lidar
    "topo_tab": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['clem1-gravity-topo', '/topo'],
        "label": "D",
    },
    # topography derived from lidar
    "topo_dat": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['clem1-gravity-topo', '/topo'],
        "label": "D",
    },
    # gravitational anomalies derived from radio science data
    "grav_tab": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['clem1-gravity-topo', '/gravity'],
        "label": "D",
    },
    # gravitational anomalies derived from radio science data
    "grav_dat": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['clem1-gravity-topo', '/gravity'],
        "label": "D",
    },
    # image versions of topo_dat and grav_dat
    "grav_topo_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['clem1-gravity-topo', '/images'],
        "label": "D",
    },
#     # RSS level 1 BSR products have non-compliant labels (missing pointers; support not planned)
#     "bsr_edr": {
#         "manifest": MANIFEST_FILE,
#         "fn_must_contain": ['.lbl'],
#         "url_must_contain": ['clem1-l-rss-1-bsr', '/geometry'],
#         "label": "D",
#     },
    # bistatic radar observations; pointers to data files are formatted unusually
    "bsr_rdr_data": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['clem1-l-rss-5-bsr', '/data'],
        "label": "D",
    },
    # bistatic radar observations; observing geometry data
    "bsr_rdr_geo": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['clem1-l-rss-5-bsr', '/geometry'],
        "label": "D",
    },
    # bistatic radar observations; image version of bsr_rdr_data
    "bsr_rdr_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['clem1-l-rss-5-bsr', '/img'],
        "label": "D",
    },
    
}
