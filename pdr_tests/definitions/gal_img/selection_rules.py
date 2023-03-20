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
IMG_FILE = Path(MANIFEST_DIR, "img_usgs_galileo_coverage.parquet")

file_information = {
    # boring VICAR-style .img files. they do have line prefix tables we
    # currently just successfully ignore. note that many are subframed by
    # zeroing parts of the arrays, which can look on casual inspection like
    # we didn't read part of the array,\ but is actually present as intended
    # in the file.
    "REDR": {
        "manifest": IMG_FILE,
        "fn_ends_with": ['.img'],
        "url_regex": [r'.*SSI/go_00\d[2-9]'],
        "label": (".img", ".lbl"),
        "force_lowercase_download": True
    },
    "cal_images": {
        "manifest": IMG_FILE,
        "fn_ends_with": ['.img'],
        "url_regex": [r'.*SSI/go_0001'],
        "label": (".img", ".lbl"),
        "force_lowercase_download": True
    },
    # they apparently think of them in a distinct way, so i'm organizing them
    # in a distinct way
    "cal_dat_images": {
        "manifest": IMG_FILE,
        "fn_ends_with": ['.dat'],
        "url_regex": [r'.*SSI/go_0001'],
        "label": (".dat", ".lbl"),
        "force_lowercase_download": True
    },
}
