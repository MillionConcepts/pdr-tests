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
SBN_FILE = "tiny"

file_information = {
    
    # Safed: Crommelin products (practice target)
    # Archived: Halley (primary target), GZ (practice target)
    #   - version 1.0 of the Halley products are not in tiny.parquet
    # In-progress: version 2.0 of several Halley datasets
    
    # flux
    "flux_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-ppflx-3-rdr-halley', 'data'],
        "label": "D",
    },
    # magnitude
    "mag_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-ppmag-3-rdr-halley', 'data'],
        "label": "D",
    },
    # polarimetry
    "pol_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-ppol-3-rdr-halley', 'data'],
        "label": "D",
    },
    # polarimetry - stokes parameter
    "stokes": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-ppstoke-3-rdr', 'data'],
        "label": "D",
    },
    
}

"""
# Unsupported GZ products; incomplete PDS3 labels do not fully define the 
# tables' formats.

    "flux_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-ppflx-3-rdr-gz', 'data'],
        "label": "D",
    },
    "mag_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-ppmag-3-rdr-gz', 'data'],
        "label": "D",
    },
    "pol_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-ppol-3-rdr-gz', 'data'],
        "label": "D",
    },
"""
