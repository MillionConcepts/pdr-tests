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

file_information = {
    
    # Safed: Crommelin products (practice target)
    # Archived: Halley (primary target), GZ (practice target)
    # There are several radio science NDR datasets; they are null-data headers
    # for products that have not been digitized.
    
    # Continuum image
    "continuum": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-rscn-3-edr-halley-v1.0/data'],
        "label": "D",
    },
    # Occultation
    "occult_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['ihw-c-rsoc-3-edr-halley-v1.0/data'],
        "label": "D",
    },
    # OH polarization spectra
    "oh_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-rsoh-3-edr-halley-v1.0/data'],
        "label": "D",
    },
    # Radar polarization spectra
    "radar": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-rsrdr-3-edr-halley-v1.0/data'],
        "label": "D",
    },
    # Spectral Line
    "spectral_line": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-rssl-3-edr-halley-v1.0/data'],
        "label": "D",
    },
    # UV Visibility
    # UserWarning: Unable to load SPECTRUM: 'float' object has no attribute 'replace'
##    "visibility": {
##        "manifest": SBN_FILE,
##        "fn_must_contain": ['.dat'],
##        "url_must_contain": ['ihw-c-rsuv-2-edr-halley-v1.0/data'],
##        "label": "D",
##    },

    # Support not planned:
    # The GZ products have incomplete PDS3 labels. Their pointers are also
    # formatted weird when there are multiple image pointers in one label.
    "occult_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['ihw-c-rsoc-3-edr-gz-v1.0/data'],
        "label": "D",
        "support_np": True
    },
    "oh_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-rsoh-3-edr-gz-v1.0/data'],
        "label": "D",
        "support_np": True
    },
}
