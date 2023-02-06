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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
LRO_FILE = Path(MANIFEST_DIR, "geolro_coverage.parquet")

# the '/lro' on the end of the url_must_contain instructions is to exclude
# products in 'superseded' subdirectories
file_information = {
    # simple flat ascii tables including decoded telemetry
    # from a 1-hour period
    "edr": {
        "manifest": LRO_FILE,
        "fn_must_contain": ['edr.tab'],
        "url_must_contain": ['lro-l-dlre-2-edr-v1/lro'],
        "label": "D",
    },
    # ZIP-compressed flat ascii tables.
    "rdr": {
        "manifest": LRO_FILE,
        "fn_must_contain": ['rdr.zip'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro'],
        "label": "D",
    },


    # ends_with instructions are intended to ignore detached XML files for
    # ArcGIS in EXTRAS
    "gdr_l2_img": {
        "manifest": LRO_FILE,
        "fn_ends_with": ['.img'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'gdr_l2'],
        "label": "D",
    },
    "gdr_l2_jp2": {
        "manifest": LRO_FILE,
        "fn_ends_with": ['.jp2'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'gdr_l2'],
        "label": "D",
    },
    # L3 GDRs. also scaled 16-bit ("16-byte integers"). 5 'planes' / files /
    # products for each version of each L3 GDR, but all the same format.
    # again, both IMG and JP2 flavors.
    "gdr_l3_img": {
        "manifest": LRO_FILE,
        "fn_ends_with": ['.img'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'data', 'gdr_l3'],
        "label": "D",
    },
    "gdr_l3_jp2": {
        "manifest": LRO_FILE,
        "fn_ends_with": ['.jp2'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'data', 'gdr_l3'],
        "label": "D",
    },
    # L4 products: big flat ascii tables. 3 types.
    # don't know yet if I want to stick examples of each in.
    "l4": {
        "manifest": LRO_FILE,
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'data'],
        "fn_regex": ["(pcp|dlre_prp|global)_.*tab"],
        "label": "D",
    }
}
