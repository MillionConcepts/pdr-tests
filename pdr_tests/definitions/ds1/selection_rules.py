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
    # ION PROPULSION SYSTEM DIAGNOSTIC SUBSYSTEM (IDS)
    # RDRs
    "ids_rdr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ds1-c-ids-3-rdr-borrelly-v1.0/data'],
        "label": "D",
    },
    # MINIATURE INTEGRATED CAMERA-SPECTROMETER (MICAS)
    # DLR and USGS DEMs
    "micas_dem": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['dem.tab'],
        "url_must_contain": ['ds1-c-micas-5-borrelly-dem-v1.0/data'],
        "label": "D",
    },
    # images used for DEM
    "micas_img": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ds1-c-micas-5-borrelly-dem-v1.0/data/images'],
        "label": "D",
    },
    # scale/matrix values used for USGS DEM
    "micas_mat": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ds1-c-micas-5-borrelly-dem-v1.0/data/matrices'],
        "label": "D",
    },

    # Safed Datasets:
    # DS1-C-MICAS-2-EDR-VISCCD-BORRELLY-V1.0
    # DS1-C-MICAS-3-RDR-VISCCD-BORRELLY-V1.0
    # DS1-C-PEPE-2-EDR-BORRELLY-V1.0
}
