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
PPI_FILE = "plasm_full"

file_information = {
    
    # Derived Triton atmospheric profile
    "derived": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vg_2499/data'],
        "label": "D",
    },
    # a spice kernel; label has no pointer to the data file
    "spice": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tsp'],
        "url_must_contain": ['vg_2499/geometry'],
        "label": "D",
        "support_np": True
    },
    # Low-level RSS data from Saturn and Titan occultations. Mirrored at RMS
    # (support not planned; labels are missing pointers to the data files)
    "odr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.ODR'],
        "url_must_contain": ['VG', 'RSS-1-ROCC', '/DATA'],
        "label": "D",
        "support_np": True
    },
    # Geometry files at PPI
    "geom": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG', 'RSS-1-ROCC', '/GEOMETRY'],
        "label": "D",
    },
    # Support not planned
    # The SPK products are spice kernels. The DAT products have no pointers in 
    # the labels. The CRS tables have extra newline characters throughout that 
    # cause them to open incorrectly.
    "geom_unsupported": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((SPK)|(DAT)|(CRS))$'],
        "url_must_contain": ['VG', 'RSS-1-ROCC', '/GEOMETRY'],
        "label": "D",
        "support_np": True
    },
}

