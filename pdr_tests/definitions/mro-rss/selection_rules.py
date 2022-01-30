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
    'odf': {'manifest': GEO_MRO_FILE,
            "fn_must_contain": ['.odf'],
            "url_must_contain": ['rss', '/odf'],  # this is probably unnecessary, but it's here anyway
            "label": "D"},
    'rsr': {'manifest': GEO_MRO_FILE,
            "fn_must_contain": ['.1a1'],
            "url_must_contain": ['rss', '/rsr'],
            "label": "D"},
    'tnf': {'manifest': GEO_MRO_FILE,
            'fn_must_contain': ['.tnf'],
            'url_must_contain': ['rss', '/tnf'],  # same thing here
            "label": "D"},
    'rsdmap': {'manifest': GEO_MRO_FILE,
               'fn_must_contain': ['.img'],
               'url_must_contain': ['rss', '/rsdmap'],
               "label": "D"},
    'shadr': {'manifest': GEO_MRO_FILE,
              'fn_must_contain': ['.tab'],
              'url_must_contain': ['rss', '/shadr'],
              "label": "D"},
    'shbdr': {'manifest': GEO_MRO_FILE,
              'fn_must_contain': ['.dat'],
              'url_must_contain': ['rss', '/shbdr'],
              "label": "D"},
}
