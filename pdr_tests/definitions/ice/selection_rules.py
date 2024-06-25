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
SBN_FILE = "tiny_other"
PPI_FILE = "plasm_full"

file_information = {
    # Energetic Particle Anisotropy Spectrometer
    "epas": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ice-c-epas-3-rdr-giacobin-zin-v1.0/data'],
        "label": "D",
    },
    # Vector Helium Magnetometer
    "mag": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ice-c-mag-3-rdr-giacobin-zin-v1.0/data'],
        "label": "D",
    },
    # Plasma Wave Spectrum Analyzer
    # magnetic-field data
    "plawav_msp": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ice-c-plawav-3-rdr-msp-giacobin-zin-v1.0/data'],
        "label": "D",
    },
    # electric-field data
    "plawav_esp": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ice-c-plawav-3-rdr-esp-giacobin-zin-v1.0/data'],
        "label": "D",
    },
    # Radio Mapping of Solar Wind Disturbances
    "radwav": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ice-c-radwav-3-rdr-giacobin-zin-v1.0/data'],
        "label": "D",
    },
    # Solar Wind Plasma
    "swp": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ice-c-swplas-3-rdr-giacobin-zin-v1.0/data'],
        "label": "D",
    },
    # Ultralow-energy charge analyzer
    "uleca": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ice-c-uleca-3-rdr-giacobini-zin-v1.0/data'],
        "label": "D",
    },

    # Ephemeris data
    # (There are only 3 unique products, but it looks like 18 because each 
    # volume has a copy.)
    "ephem_tab": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ICE-', 'DATA', 'EPHEM'],
        "label": "D",
    },
    "ephem_tbl": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TBL'],
        "url_must_contain": ['ICE-', 'DATA', 'EPHEM'],
        "label": "D",
    },
}

"""
    # Ion Composition Instrument
    # The data products are just text files
    "ici": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.txt'],
        "url_must_contain": ['ice-c-ici-3-rdr-giacobini-zin-v1.0/data'],
        "label": "D",
    },
"""

