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

# variables naming specific parquet files in node_manifests
IMG_FILE = "img_jpl_msl_etc"

file_information = {
    
    # These selection rules are out-of-date. The dataset has been converted to 
    # PDS4 at IMG JPL, and the directory structure has changed!

    # A special case opens these with read_csv()
    "localizations": {
        "manifest": IMG_FILE,
        "fn_must_contain": [".csv"],
        "url_must_contain": ["MSLPLC_1XXX/DATA/LOCALIZATIONS"],
        "label": "D",
    },
    # 2 products: the DEM is 300 mb, the map is 1.2 gb
    "maps": {
        "manifest": IMG_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ["MSLPLC_1XXX/DATA/MAPS"],
        "label": "D",
    },
    
}

SKIP_FILES = ["DSMAP.CAT", "VICAR2.TXT", "ODL.TXT"]
