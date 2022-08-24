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
THEMIS_FILE = Path(MANIFEST_DIR, "img_asu_themis_tes.parquet")

file_information = {
    
    "BTR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtib'],
        "label": "A",
    },
    "ABR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtvb'],
        "label": "A",
    },    
    "PBT_v1": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTGEO_v1/', 'odtip'],
        "label": "A",
    },
    "PBT_v2": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTGEO_v2/', 'odtip'],
        "label": "A",
    },
    "ALB_v2": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTGEO_v2/', 'odtva'],
        "label": "A",
    }, 
}

"""
These QUBE and CUBE products can be revisited once they are supported:

    "ir_EDR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.QUB'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtie'],
        "label": (".fmt", ".FMT"),
    },
    "ir_RDR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.QUB'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtir'],
        "label": "A",
    },
    "vis_EDR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.QUB'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtve'],
        "label": "A",
    },
    "vis_RDR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.QUB'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtvrs'],
        "label": "A",
    },
    "ir_GEO_v1": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.CUB.gz'],
        "url_must_contain": ['/ODTGEO_v1/', 'odtig'],
        "label": "D",
    },
    "vis_GEO_v1": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.CUB'],
        "url_must_contain": ['/ODTGEO_v1/', 'odtvg'],
        "label": "D",
    },
    "ir_GEO_v2": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.CUB.gz'],
        "url_must_contain": ['/ODTGEO_v2/', 'odtig'],
        "label": "D",
    },
    "vis_GEO_v2": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.CUB'],
        "url_must_contain": ['/ODTGEO_v2/', 'odtvg'],
        "label": "D",
    },

"""
