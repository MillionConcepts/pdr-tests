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
    # Archived: Halley (primary target), Gz (practice target)
    #   - version 1.0 of the Halley products are not in tiny.parquet
    #   - some v1.0 product types open, many open wrong or not at all
    #   - most Gz product do not open (incomplete labels)
    # In-progress: version 2.0 of several Halley datasets
    
    # filter response curves (v2.0 of the dataset; v1.0 are .dat files)
    "curve": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['irfc', '.tab'],
        "url_must_contain": ['ihw-c-irfcurv-3-edr-halley', 'data'],
        "label": "D",
    },
    # filter parameter tables    
    "param_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-irftab-3-rdr-halley', 'data'],
        "label": "D",
    },
    # images
    "image_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['ihw-c-irimag-3-edr-gz', 'data'],
        "label": "D",
    },
    "image_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ihw-c-irimag-3-edr-halley', 'data'],
        "label": "D",
    },
    # photometry
    "photom_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-irphot-3-rdr-halley', 'data'],
        "label": "D",
    },
    "photom_halley_addenda": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ear-c-irphot-2-rdr-halley-addenda', 'data'],
        "label": "D",
    },
    # polarimetry
    "polar_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-irpol-3-rdr-halley', 'data'],
        "label": "D",
    },
    # spectra (v2.0 of the dataset; v1.0 are .dat files)
    "spec_halley": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-irspec-3-edr-halley', 'data'],
        "label": "D",
    },
    
    # Support not planned:
    # The Gz products have stub labels missing a lot of table format info
    "param_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-irftab-2-rdr-gz', 'data'],
        "label": "D",
        "support_np": True
    },
    "photom_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-irphot-2-rdr-gz', 'data'],
        "label": "D",
        "support_np": True
    },
    "polar_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-irpol-2-rdr-gz', 'data'],
        "label": "D",
        "support_np": True
    },
    "spec_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-irspec-3-edr-gz', 'data'],
        "label": "D",
        "support_np": True
    },
    "mag_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-irimag-3-edr-gz', 'data'],
        "label": "D",
        "support_np": True
    },
}
