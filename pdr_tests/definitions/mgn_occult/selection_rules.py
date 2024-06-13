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
ATM_MANIFEST = "atm"

file_information = {
	
	# "Magellan Radio Occultation Raw Data Archive"
    # Original Data Record (ODR) --> primary data type
    "odr": {
        "manifest": ATM_MANIFEST,
        "fn_must_contain": ['.odr'],
        "url_must_contain": ['mg_22', 'odr'],
        "label": "D",
    },
    # Tracking Data Files (TDFs) --> backup to ODRs, ancillary
    "tdf": {
        "manifest": ATM_MANIFEST,
        "fn_must_contain": ['.tdf'],
        "url_must_contain": ['mg_22', 'tdf'],
        "label": "D",
    },
    # "Magellan Venus Radio Occultation Atmospheric Profiles Data Set Archive"
    # derived products; 2 profiles (ABS and RTPD)
    "ddr": {
        "manifest": ATM_MANIFEST,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['mg_2401/data'],
        "label": "D",
    },

    # Spacecraft attitude info during radio occultation
    # (most other products in the geometry directories are spice kernels)
    "geometry": {
        "manifest": ATM_MANIFEST,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mg_22', 'geometry'],
        "label": "D",
    },
}
