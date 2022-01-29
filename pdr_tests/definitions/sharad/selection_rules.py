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
GEO_MRO_FILE = Path(MANIFEST_DIR, "geomro.parquet")

file_information = {
    'EDR': {'manifest': GEO_MRO_FILE,
            "fn_must_contain": ['_s', '.dat'],
            "url_must_contain": ['sharad', '-edr-', '/data/'],
            "label": {"a_*.dat", "a.lbl"}},
    'RDR': {'manifest': GEO_MRO_FILE,
            "fn_must_contain": ['.dat'],
            "url_must_contain": ['sharad', '/data/', '-rdr-'],
            "label": "D"},
    'rgram': {'manifest': GEO_MRO_FILE,
              'fn_must_contain': ['.img'],
              'url_must_contain': ['sharad', '/rgram/'],
              "label": {"D"}},
    'geom': {'manifest': GEO_MRO_FILE,
             'fn_must_contain': ['.tab'],
             'url_must_contain': ['sharad', '/geom/'],
             "label": "D"},
}
