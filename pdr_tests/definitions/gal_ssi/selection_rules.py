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
IMG_FILE = Path(MANIFEST_DIR, "img_usgs.parquet")
SB_FILE = Path(MANIFEST_DIR, "tiny.parquet")

file_information = {
    # Calibration product types:
    "blemish": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Galileo/SSI/go_0001', 'blemish'],
        "label": "D",
    },
    "dark": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['Galileo/SSI/go_0001', 'dark'],
        "label": "D",
    },
    "shutter": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Galileo/SSI/go_0001', 'shutter'],
        "label": "D",
    },
    "slope": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['Galileo/SSI/go_0001', 'slope'],
        "label": "D",
    },
    # REDR data
    # Image pointer opened fine manually. TELEMETRY_TABLE pointer fails with:
    # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'.
    # LINE_PREFIX_TABLE also not yet supported.
##    "redr": {
##        "manifest": IMG_FILE,
##        "fn_must_contain": ['.img'],
##        "url_must_contain": ['Galileo/SSI'],
##        "url_regex": [r'\/[cC][0-9]{6}'],
##        "label": "D",
##    },
    
    # The SB Node has Ida and Gaspra subsets of SSI data in different formats
    # (.fit and .qub), so they are included here.
    "gaspra": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['galileo/idagaspra', 'data/galileo_ssi/gaspra'],
        "label": "D",
    },
    "ida": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['galileo/idagaspra', 'data/galileo_ssi/ida'],
        "label": "D",
    },
    "sb_cal_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['galileo/derived', '_SSI_', 'data/fits'],
        "label": "D",
    },
    "sb_cube": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.qub'],
        "url_must_contain": ['galileo/derived', '_SSI_', 'data/qube'],
        "label": "D",
    },
}
