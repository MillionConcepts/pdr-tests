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
GEO_FILE = "geomsl"

file_information = {
    # EDRs
    # standby/housekeeping data
    "est": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat', 'est'],
        "url_must_contain": ['msl-m-dan-2-edr', 'data'],
        "label": "D",
    },
    # passive neutron data
    "epa": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat', 'epa'],
        "url_must_contain": ['msl-m-dan-2-edr', 'data'],
        "label": "D",
    },
    # active neutron data
    "eac": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat', 'eac'],
        "url_must_contain": ['msl-m-dan-2-edr', 'data'],
        "label": "D",
    },
    # RDRs - new products have pds4 labels, older products are pds3 only
    # derived engineering data
    "ren": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat', 'ren'],
        "url_must_contain": ['msl-m-dan-3_4-rdr', 'data'],
        "label": "D",
    },
    # derived passive data
    "rpa": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat', 'rpa'],
        "url_must_contain": ['msl-m-dan-3_4-rdr', 'data'],
        "label": "D",
    },
    # derived active data
    "rac": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat', 'rac'],
        "url_must_contain": ['msl-m-dan-3_4-rdr', 'data'],
        "label": "D",
    },
    # averaged passive data
    "rap": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat', 'rap'],
        "url_must_contain": ['msl-m-dan-3_4-rdr', 'data'],
        "label": "D",
    },
    # averaged active data
    # These tables are probably opening correctly, but they are formatted
    # differently enough from the other RDRs that it is hard to tell. Several
    # columns (e.g. time) have the same values for every row, but those columns
    # in the averaged passive products have unqiue values down the rows.
    # (Could not find a pds4 example of this ptype for comparison.)
    "raa": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat', 'raa'],
        "url_must_contain": ['msl-m-dan-3_4-rdr', 'data'],
        "label": "D",
    },
}
