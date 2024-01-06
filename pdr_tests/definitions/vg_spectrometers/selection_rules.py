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
ATM_FILE = "atm"
RMS_FILE = "ringvolumes"

file_information = {
    
    # UVS spectra (RDRs) are converted to PDS4
    # UVS derived maps
    "uvs_maps": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['vg_2101/data'],
        "label": "D",
    },
    
    # IRIS derived maps
    "iris_maps": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['vg_2102/data'],
        "label": "D",
    },
##    # IRIS full-res observations; unsupported VAX tables
##    "iris_fullres": {
##        "manifest": ATM_FILE,
##        "fn_must_contain": ['.dat'],
##        "url_must_contain": ['/vg_2001/'],
##        "fn_regex": [r'^vg[12]_'],
##        "label": "D",
##    },
    # IRIS full-res expanded Jupiter/Saturn dataset 
    "iris_expanded_ascii": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VGIRIS_xxxx_peer_review', '/DATA'],
        "label": "D",
    },
    "iris_expanded_lsb": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['LSB.DAT'],
        "url_must_contain": ['VGIRIS_xxxx_peer_review', '/DATA'],
        "label": "D",
    },
    "iris_expanded_msb": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['MSB.DAT'],
        "url_must_contain": ['VGIRIS_xxxx_peer_review', '/DATA'],
        "label": "D",
    },
}

