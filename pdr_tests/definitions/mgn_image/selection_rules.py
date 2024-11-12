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
	
    # Compressed-Resolution Basic Image Data Record
    "c-bidr": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['IM', '.DAT'], # image data products only
        "url_must_contain": ['mgn-v-rdrs-5-c-bidr-v1'],
        "label": "D",
    },
    # Mosaic Image Data Record
    # full resolution
    "f-midr": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mgn-v-rdrs-5-midr-full-res-v1'],
        "url_regex": [r'mg_..../f'],
        "label": "D",
    },
    # compressed
    "c-midr": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mgn-v-rdrs-5-midr-full-res-v1'],
        "url_regex": [r'mg_..../c'],
        "label": "D",
    },
    # each MIDR volume/subdirectory has frame, geometry, and histogram tables
    "midr_tables": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mgn-v-rdrs-5-midr-full-res-v1'],
        "label": "D",
    },
    
    # Full-Resolution Basic Image Data Record --> no pointers, not archive compliant
    "f-bidr": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": [''],
        "url_must_contain": ['mgn-v-rdrs-5-bidr-full-res-v1'],
        "label": "D",
        "support_np": True
    },
	# ancillary tables; known unsupported 
    # labels do not define number of columns for tables, headers are being sent to read_table()
    "c-bidr_tables": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.DAT'],
        "fn_regex": [r'^[A-HJ-Z]'],
        "url_must_contain": ['mgn-v-rdrs-5-c-bidr-v1'],
        "label": "D",
        "support_np": True
    },

    # Support not planned - SAR EDRs are safed
    "sar_edr_safed": {
        "manifest": IMG_MANIFEST,
        "fn_must_contain": ['EDR'],
        "url_must_contain": ['edr/MGN_', '/EDR'],
        "label": "A",
        "support_np": True
    },
}
