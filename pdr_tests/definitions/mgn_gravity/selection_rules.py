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

GEO_MANIFEST = Path(MANIFEST_DIR, "geomgn.parquet")

file_information = {
	
	
    # Line of Sight Acceleration Profile Data Record
    "losapdr": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.001'],
        "url_must_contain": ['mgn-v-rss-5-losapdr-l2', 'data'],
        "label": "A",
    },
    
    # Spherical Harmonics Gravity ASCII Data Record (SHGADR) and
    # Spherical Harmonics Topography ASCII Data Record (SHTADR)
    "shadr": {
        "manifest": GEO_MANIFEST,
        "fn_regex": [r'^((sht)|(shg))(.*)(a0[12])'],
        "url_must_contain": ['mgn-v-rss-5-gravity-l2'],
        "label": "A",
    },
    # Spherical Harmonics Binary Data Record (SHBDR)
    "shbdr": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['shg', '.b01'],
        "url_must_contain": ['mgn-v-rss-5-gravity-l2', 'gravity'],
        "label": "D",
    },
    # grav anomalies, topo, and associated errors; derived from shadr/shbdr
    # ASCII array format
    "grav_topo_grid": {
        "manifest": GEO_MANIFEST,
        "fn_regex": [r'((grd)|(err))\.dat'],
        "url_must_contain": ['mgn-v-rss-5-gravity-l2'],
        "label": "D",
    },
    # images versions of grav_topo_grid
    "grav_topo_img": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mgn-v-rss-5-gravity-l2', 'images'],
        "label": "D",
    },
    # digital maps of grav anomalies and topography
    "grav_topo_map": {
        "manifest": GEO_MANIFEST,
        "fn_regex": [r'(geoid\.dat)|(bouguer)|(freeair)|(topo\.dat)'],
        "url_must_contain": ['mgn-v-rss-5-gravity-l2', ''],
        "label": "A",
    },
    
    
	
}
