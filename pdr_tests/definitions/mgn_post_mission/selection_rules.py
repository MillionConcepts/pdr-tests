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
GEO_MANIFEST = "geomgn"
IMG_MANIFEST = "img_usgs_magellan"

file_information = {
	
	# "This archive contains a map of stereo-derived topography produced from the Magellan FMAPs."
    "topo": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['urn-nasa-pds-magellan_stereo_topography', 'data'],
        "label": ('.img', '.xml'),
    },
    
	# "This archive was produced by the U.S. Geological Survey after the Magellan mission 
	# ended. It contains full-resolution mosaicked images covering about 92% of the planet. 
	# Images were generated from the F-BIDR products."
    "fmap": {
        "manifest": IMG_MANIFEST,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mg_1'],
        "label": "A",
    },
    # browse versions
    "fmap_browse": {
        "manifest": IMG_MANIFEST,
        "fn_must_contain": ['.ibg'],
        "url_must_contain": ['mg_1'],
        "label": "A",
    },
    # gazetter - tables of named features on Venus 
    # (also spelled gazetteer in some of the documentation)
    # Support planned, low priority. Some tables open fine, others are 
    # double-spaced and open wrong. They're easier to test manually than with 
    # ix because all products share the gazetter.tab filename.
    # "gazetter": {
    #     "manifest": IMG_MANIFEST,
    #     "fn_must_contain": ['.tab'],
    #     "url_must_contain": ['mg_1', 'gazetter'],
    #     "label": "D",
    # },
    
}
