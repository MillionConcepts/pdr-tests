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
SB_FILE = "tiny_rosetta"

file_information = {
    
    # images; well-labeled 2-D arrays
    "EDR": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['holdings/ro-', '-navcam-2-', '/data'],
        "label": "D",
    },
    # images; well-labeled 2-D arrays
    # each data product includes two .img files and one .lbl
    # filenames ending in 'c.img' are the main images, those ending in 'q.img' are quality flag images
    "RDR": {
        "manifest": SB_FILE,
        "fn_must_contain": ['c.img'],
        "url_must_contain": ['holdings/ro-', '-navcam-3-', '/data'],
        "label": "D",
    },
    # These are the quality flag images mentioned above. They are fully 
    # supported, but the RDR ptype alone leaves them marked as 'uncovered' in 
    # the coverage analysis pipeline. This RDR_quality_flag ptype is here to 
    # make sure they are counted as covered.
    # The "ix_skip" flag ensures they are skipped on all ix calls that do not 
    # specifically pass this ptype.
    "RDR_quality_flag": {
        "manifest": SB_FILE,
        "fn_must_contain": ['q.img'],
        "url_must_contain": ['holdings/ro-', '-navcam-3-', '/data'],
        "label": "A", # shares labels with RDR ptype above
        "ix_skip": True
    },
    # FITS versions of IMG data 
    "EDR_fits": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['holdings/ro-', '-navcam-2-', '/extras'],
        "label": "D",
    },
    "RDR_fits": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['holdings/ro-', '-navcam-3-', '/extras'],
        "label": "D",
    },
}


