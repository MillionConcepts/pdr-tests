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
GEO_MESSENGER_FILE = Path(MANIFEST_DIR, "geomessenger.parquet")

file_information = {
    # standard data products; well-labeled fixed-length tables
    "uvvs_EDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['mascs-2-virs-edr-', '/uvvs'],
        "label": "D",
    },
    # standard data products; well-labeled fixed-length tables
    "virs_EDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['mascs-2-virs-edr-', '/virs'],
        "label": "D",
    },
    # housekeeping data for UVVS and VIRS; well-labeled fixed-length tables
    "hk_EDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['mascs-2-virs-edr-', '/hk'],
        "label": "D",
    },
    # calibrated data; well-labeled fixed-length tables
    "uvvs_CDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['mascs-3-virs-cdr-caldata-', '/cdr', '/uvvs'],
        "label": "D",
    },
    # calibrated data; well-labeled fixed-length tables
    "virs_CDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['mascs-3-virs-cdr-caldata-', '/cdr', '/virs'],
        "label": "D",
    },
    # derived data; well-labeled fixed-length tables
    "uvvs_DDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['mascs-3-virs-cdr-caldata-', '/ddr', '/uvvs'],
        "url_regex": [r'(uvvs_surf)|(uvvs_summ)|(uvvs_atmo)'],
        "label": "D",
    },
    # derived data; well-labeled fixed-length tables
    "virs_DDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['mascs-3-virs-cdr-caldata-', '/ddr', '/virs'],
        "label": "D",
    },
    # combined UVVS and VIRS derived data; well-labeled fixed-length tables
    "combo_DDR": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['mascs-3-virs-cdr-caldata-', '/ddr', '/uvvs_virs_combined'],
        "label": "D",
    },
    
    # There are multiple files per product/label for this product type.
    # It's easiest to select the label files here to avoid filename issues.
    # Don't be fooled by ix's download size estimate based on the labels only,
    # these are LARGE FILES (~1.8 GB each, but there are only 18 total).
    
    # derived analysis product; well-labeled 2-dimensional raster images
    "virs_DAP": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".lbl"],
        "url_must_contain": ['mascs-3-virs-cdr-caldata-', '/dap', '/virs'],
        "label": "D",
    },
}
