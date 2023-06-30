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
    # EDR - raw images
    "raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_MSI_2_EDR_', '/data', '/raw'],
        "label": "D",
    },
    # EDR - iof
    "iof": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_MSI_3_EDR_', '/data', '/iof'],
        "label": "D",
    },
    # EDR - rad
    "rad": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['NEAR_A_MSI_3_EDR_', '/data', '/rad'],
        "label": "D",
    },
    # RDR filter bandpass info
    "filters": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['NEAR_MSI_6_RDR_INSTRUMENT_INFO_V1_0/data'],
        "label": "D",
    },
    # DIM products (basemaps for shape model)
    "dim": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['NEAR_A_MSI_5_DIM_EROS_ORBIT_V1_0/data'],
        "label": "A",
    },
    # Eros shape model
    "shape": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['NEAR_A_MSI_5_EROS_SHAPE_MODELS_V1_0/data'],
        "label": "D",
    },
}
