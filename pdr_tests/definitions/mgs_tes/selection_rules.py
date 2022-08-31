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
MANIFEST_FILE = Path(MANIFEST_DIR, "img_asu_themis_tes.parquet")

file_information = {
    
    # derived atmospheric data; well-labeled fixed length table
    "ATM": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/atm'],
        "label": "A",
    },
    # raw and calibrated bolometer data; well-labeled fixed length table
    "BOL": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/bol'],
        "label": "A",
    },
    # derived positional data; well-labeled fixed length table; IAU-1994 coords
    "GEO": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/geo'],
        "url_regex": [r'geo$'],
        "label": "A",
    },
    # derived positional data; well-labeled fixed length table; IAU-1994 AND IAU-2000 coords
    "GEO_2000": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/geo/geo00'],
        "label": "A",
    },
    # interferogram metadata (.tab); well-labeled fixed length table
    "IFG_tab": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/ifg'],
        "label": "A",
    },
    # observation parameters; well-labeled fixed length table
    "OBS": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/obs'],
        "label": "A",
    },
    # raw positional data; well-labeled fixed length table
    "POS": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/pos'],
        "label": "A",
    },
    # raw and calibrated radiance metadata (.tab); well-labeled fixed length table
    "RAD_tab": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/rad'],
        "label": "A",
    },
    # auxiliary observation parameters; well-labeled fixed length table
    "TLM": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mars_by_table/tlm'],
        "label": "A",
    },
}


"""
# Known unsupported product; labels unusually short

    # Percent concentraion tables; fixed length table
    "PCT": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['mars_by_table/pct'],
        "label": "A",
    },

# Known unsupported products; .var files missing PDS3 compliant labels
# Support not planned.

    # raw interferogram data (.var); variable length table
    "IFG_data": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.var'],
        "url_must_contain": ['mars_by_table/ifg'],
        "label": "A",
    },

    # raw and calibrated radiance data (.var); variable length table
    "RAD_data": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.var'],
        "url_must_contain": ['mars_by_table/rad'],
        "label": "A",
    },

"""
