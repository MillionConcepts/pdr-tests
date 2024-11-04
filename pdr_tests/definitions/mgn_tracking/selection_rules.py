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
PPI_FILE = "plasm_full"

file_information = {
	
    # Archival Tracking Data Files (ATDF/TDF)
    "tdf": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.tdf'],
        "url_must_contain": ['mgn-v-rss-1-tracking'],
        "label": "D",
    },
	# weather data in tracking directory (TEXT objects)
	"weather": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.wea'],
        "url_must_contain": ['mgn-v-rss-1-tracking'],
        "label": "D",
    },
    # Original Data Records (ODRs)
	"odr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.ODR'],
        "url_must_contain": ['MGN-SS-RSS-1-ODR-OPENLOOP-SW-SCINT-V1.0/DATA'],
        "label": "D",
    },
    
    # Orbit Data Files (ODF)
    # Known Unsupported, eventual support planned (low priority)
    # from documentation: "similar data to the ATDF but in an edited and compressed format"
#     "odf": {
#         "manifest": GEO_MANIFEST,
#         "fn_must_contain": ['.odf'],
#         "url_must_contain": ['mgn-v-rss-1-tracking'],
#         "label": "D",
#     },
    
    # other unsupported tracking/telemetry products: 
    # AMD, ION, TRO (labels lack pointers to data files)
    "unsupported_telemetry": {
        "manifest": GEO_MANIFEST,
        "fn_regex": [r'(amd$)|(ion$)|(tro$)'],
        "url_must_contain": ['mgn-v-rss-1-tracking'],
        "label": "D",
        "support_np": True
    },
}
