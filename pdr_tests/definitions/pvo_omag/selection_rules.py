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
PPI_FILE = "plasm_full"

file_information = {    
    # SCCOORDS HIRES original binary files
    "sc_hires_bi": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD'],
        "url_must_contain": ['PVO-V-OMAG-3--SCCOORDS-HIRES',
                             'DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
##    # SCCOORDS HIRES ascii version
##    # manifest is out of date and ix can't find these files
##    "sc_hires_asc": {
##        "manifest": PPI_FILE,
##        "fn_must_contain": ['.TAB'],
##        "url_must_contain": ['PVO-V-OMAG-3--SCCOORDS-HIRES',
##                             'DATA/ASCII'],
##        "label": "D",
##    },
    # P-SENSOR HIRES original binary files
    "ps_hires_bi": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD'],
        "url_must_contain": ['PVO-V-OMAG-3-P-SENSOR-HIRES',
                             'DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
    # P-SENSOR HIRES ascii version 
    "ps_hires_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['PVO-V-OMAG-3-P-SENSOR-HIRES',
                             'DATA/ASCII'],
        "label": "D",
    },
    # SCCOORDS 24 second averages original binary files
    "sc_24s_bi": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD'],
        "url_must_contain": ['PVO-V-OMAG-4--SCCOORDS-24SEC',
                             'DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
##    # SCCOORDS 24 second averages ascii version
##    # manifest is out of date and ix can't find these files
##    "sc_24s_asc": {
##        "manifest": PPI_FILE,
##        "fn_must_contain": ['.TAB'],
##        "url_must_contain": ['PVO-V-OMAG-4--SCCOORDS-24SEC',
##                             'DATA/ASCII'],
##        "label": "D",
##    },
    # P-SENSOR 24 second averages original binary files
    "ps_24s_bi": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD'],
        "url_must_contain": ['PVO-V-OMAG-4-P-SENSOR-24SEC',
                             'DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
    # P-SENSOR 24 second averages ascii version 
    "ps_24s_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['PVO-V-OMAG-4-P-SENSOR-24SEC',
                             'DATA/ASCII'],
        "label": "D",
    },
    
}
