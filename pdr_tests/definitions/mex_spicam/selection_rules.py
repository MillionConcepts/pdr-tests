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

GEO_FILE = "geomex"

file_information = {
    
    # IR level 0B data
    # The FREQUENCY_ARRAY pointer appears to be opening fine at first glance.
    # The RECORD_ARRAY pointer does not open: "UserWarning: Unable to load
    # RECORD_ARRAY: <class 'KeyError'>: 'DATA_TYPE'"
    # There is a nested array that may be the cause of the problem.
##    "ir_edr": {
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['.dat'],
##        "url_must_contain": ['mex','m-spi-2-iredr-raw', 'data'],
##        "label": "D",
##    },
    # IR level 1A data
    # The spicam_rdr_hdu_name() special case fixes the FITS HDU indexing.
    "ir_rdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['mex-m-spi-2-irrdr-cleaned', 'data'],
        "label": "D",
    },
    # UV level 0B data
    # The RECORD_ARRAY pointer does not open: "UserWarning: Unable to load
    # RECORD_ARRAY: <class 'KeyError'>: 'DATA_TYPE'"
    # There is a nested array that may be the cause of the problem.
##    "uv_edr": {
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['.dat'],
##        "url_must_contain": ['mex','m-spi-2-uvedr-raw', 'data'],
##        "label": "D",
##    },
    # UV level 1A data
    # The spicam_rdr_hdu_name() special case fixes the FITS HDU indexing.
    "uv_rdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['mex-m-spi-2-uvrdr-cleaned', 'data'],
        "label": "D",
    },
    
    # The IR and UV DDR datasets are archived at PSA but not GEO.
    # They are notionally supported.
}

SKIP_FILES = ["MEX_ORIENTATION_DESC.TXT", "DATA_QUALITY_ID_DESC.TXT",
              "SPICAM_UVMODE_DESC.TXT"]
