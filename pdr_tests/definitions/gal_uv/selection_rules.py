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
ATM_FILE = Path(MANIFEST_DIR, "atm.parquet")

file_information = {
    # EUV data in .DAT file format
    "euv_dat": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['gouv_00', '/euv/DAT'],
        "label": "D",
    },
    # EUV data in .XDR file format. (1-2 products have the wrong product_id in
    # their labels, they use the .DAT file extension by mistake)
    "euv_xdr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.XDR'],
        "url_must_contain": ['gouv_00', '/euv/XDR'],
        "label": "D",
    },
    # The UVS products often call for a format file that is missing from the
    # archive (RTS_SUMMATION.FMT). The next 2 product types are a subset that
    # appear to never use the missing file. The "missing_fmt" product types
    # below are a subset of products that often reference the missing file.
    "uvs_dat": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['_UPB_', '.DAT'],
        "url_must_contain": ['gouv_00', '/uvs/DAT'],
        "label": "D",
    },
    # 1-2 XDR products have the wrong product_id in their labels, they use the
    # .DAT file extension by mistake
    "uvs_xdr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['_UPB_', '.XDR'],
        "url_must_contain": ['gouv_00', '/uvs/XDR'],
        "label": "D",
    },

    # TODO: these appear to have pds4 labels, test an example; it should be fine that the fmt doesn't exist
##    # Only some of these use the missing format file, but they are intermixed
##    # with products that use format files that are available
##    "uvs_dat_missing_fmt": {
##        "manifest": ATM_FILE,
##        "fn_must_contain": ['_URT_','.DAT'],
##        "url_must_contain": ['gouv_00', '/uvs/DAT'],
##        "label": "D",
##    },
##    # It seems like all of these use the missing format file
##    "uvs_xdr_missing_fmt": {
##        "manifest": ATM_FILE,
##        "fn_must_contain": ['_URT_', '.XDR'],
##        "url_must_contain": ['gouv_00', '/uvs/XDR'],
##        "label": "D",
##    },
}
