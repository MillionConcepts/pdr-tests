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

# shorthand variables for specific .csv files
ATM_FILE = "atm"

file_information = {
    
    # There are pds4 labels available for Galileo UVS and EUV products at the
    # ATM node. The XDR and DAT versions of the products open incorrectly
    # from their pds3 labels, and some do not open at all because of a missing
    # format file. Below are selection rules for the pds3 versions.
    
##    # EUV data in .DAT file format
##    "euv_dat": {
##        "manifest": ATM_FILE,
##        "fn_must_contain": ['.DAT'],
##        "url_must_contain": ['gouv_00', '/euv/DAT'],
##        "label": "D",
##    },
##    # EUV data in .XDR file format
##    "euv_xdr": {
##        "manifest": ATM_FILE,
##        "fn_must_contain": ['.XDR'],
##        "url_must_contain": ['gouv_00', '/euv/XDR'],
##        "label": "D",
##    },
##    # The UVS products often call for a format file that is missing from the
##    # archive (RTS_SUMMATION.FMT).
##    # UVS data in .DAT file format
##    "uvs_dat": {
##        "manifest": ATM_FILE,
##        "fn_must_contain": ['.DAT'],
##        "url_must_contain": ['gouv_00', '/uvs/DAT'],
##        "label": "D",
##    },
##    # UVS data in .XDR file format
##    "uvs_xdr": {
##        "manifest": ATM_FILE,
##        "fn_must_contain": ['.XDR'],
##        "url_must_contain": ['gouv_00', '/uvs/XDR'],
##        "label": "D",
##    },
}
