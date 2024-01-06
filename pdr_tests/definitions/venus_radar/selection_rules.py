"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .parquet file that contains urls, file sizes, etc., scraped
directly from the hosting institution for this product type. for some data
sets, all urls will be found in the same .parquet file; for others, they may
be split between nodes or scraping sessions.

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
GEO_FILE = "geovenus"

file_information = {
    # Earth-Based Radar Observations of Venus
    # Uncalibrated, Delay-Doppler Images (PDS3)
    "edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['arcb_nrao-v-rtls_gbt-3-delaydoppler-v1/vrm_90xx/data'],
        "label": "D",
    },
    # Calibrated, Multi-Look Maps (PDS4)
    "maps": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['urn-nasa-pds-venus_radar_level2/data'],
        "label": ('.img','.xml'),
    },
}
