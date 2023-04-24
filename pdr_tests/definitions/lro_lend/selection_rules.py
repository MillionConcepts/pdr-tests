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

# shorthand variables for specific .parquet files
MANIFEST_FILE = Path(MANIFEST_DIR, "geolro.parquet")

file_information = {
    # Raw Neutron spectra data
    "edr_sci": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat', 'edr_sci'],
        "url_must_contain": ['lro-l-lend-2-edr-v1', 'data'],
        "label": 'D',
    },
    # Raw Housekeeping data
    "edr_hk": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat', 'edr_hk'],
        "url_must_contain": ['lro-l-lend-2-edr-v1', 'data'],
        "label": 'D',
    },
    # Calibrated Housekeeping data
    "rdr_chk": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat', 'rdr_chk'],
        "url_must_contain": ['lro-l-lend-2-edr-v1', 'data'],
        "label": 'D',
    },
    # Raw Neutron spectra with spatial data
    "rdr_rsci": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat', 'rdr_rsci'],
        "url_must_contain": ['lro-l-lend-2-edr-v1', 'data'],
        "label": 'D',
    },
    # Derived Neutron spectra data
    "rdr_dld": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat', 'rdr_dld'],
        "url_must_contain": ['lro-l-lend-2-edr-v1', 'data'],
        "label": 'D',
    },
    # Extended Derived Neutron spectra data
    "rdr_dlx": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat', 'rdr_dlx'],
        "url_must_contain": ['lro-l-lend-2-edr-v1', 'data'],
        "label": 'D',
    },
    # Averaged Neutron spectra data
    "rdr_ald": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat', 'rdr_ald'],
        "url_must_contain": ['lro-l-lend-2-edr-v1', 'data'],
        "label": 'D',
    },
    # Could not find any files for rdr_alf (Averaged Neutron flux data)
}
