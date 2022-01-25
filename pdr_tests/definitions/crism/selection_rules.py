"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .csv file that contains urls, file sizes, etc., scraped directly
from the hosting institution for this product type. for some data sets, all
urls will be found in the same .csv file; for others, they may be split
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
GEO_MRO_FILE = Path(MANIFEST_DIR, "MRO_FILE_size_corrected.csv")

file_information = {
    "EDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ["/edr/"],
        "label": "D",
    },
    "CDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ["/cdr/"],
        "label": "D",
    },
    "DDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['/ddr/'],
        "label": "D",
    },
    "LDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['/ldr/'],
        "label": "D",
    },
    "TRDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ["/trdr/"],
        "label": "D",
    },
    "MRDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ['/mrdr/'],
        "label": "D",
    },
    "TER": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ["/ter/"],
        "label": "D",
    },
    "MTRDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": ['.img'],
        'url_must_contain': ['/mtrdr'],
        "label": "D",
    },
    'speclib': {'database': GEO_MRO_FILE,
                'fn_must_contain': ['.tab'],
                'url_must_contain': ['speclib-v1'],
                'label': "A"},
    'typespec': {'database': GEO_MRO_FILE,
                 'fn_must_contain': ['.tab'],
                 'url_must_contain': ['typespec-v1'],
                 'label': 'D'},
}
