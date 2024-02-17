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
MANIFEST_FILE = "img_usgs"

file_information = {
    
    # Lunar Orbiter Image Recovery Project (LOIRP)
    # (These are large files (600+ mb). A handful of the larger files have been
    # manually tested; products <=200 mb have been tested with ix.)
    # medium-resolution image frames
    "med_res": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['M.IMG'],
        "url_must_contain": ['LO_1001/DATA'],
        "label": 'D',
    },
    # high-resolution image frames
    "high_res": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'H[123]\.IMG$'],
        "url_must_contain": ['LO_1001/DATA'],
        "label": 'D',
    },
    
    # Older versions of the LO3/4/5 datasets
    # primary products
    "lo_primary": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['primary'],
        "url_regex": [r'LO[345]_0001/constructed_frames'],
        "label": 'A',
    },
    # cosmetic versions
    "lo_cosmetic": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['cosmetic'],
        "url_regex": [r'LO[345]_0001/constructed_frames'],
        "label": 'A',
    },
}
