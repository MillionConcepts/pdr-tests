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
    
    # SAM EDRs are safed, and according to GEO "the lowest-level SAM RDR
    # product is essentially equivalent to the raw data"
    "edr_safed": {
        "manifest": GEO_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ["msl-m-sam-2-edr-v1/mslsam_0xxx/data"],
        "label": "D",
        "support_np": True
    },
    
    # The RDRs can have multiple data files per label, so the selection rules
    # grab the label instead of the csv, tab, and/or txt file(s).
    
    # level 0 RDRs
    "l0_hk": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_hk_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level0"],
        "label": "D",
    },
    "l0_qms": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_qms_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level0"],
        "label": "D",
    },
    "l0_gc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_gc_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level0"],
        "label": "D",
    },
    "l0_tls": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_tls_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level0"],
        "label": "D",
    },
    # level 1a RDRs
    "l1a_hk": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_hk_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level1a"],
        "label": "D",
    },
    "l1a_qms": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_qms_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level1a"],
        "label": "D",
    },
    "l1a_gc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_gc_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level1a"],
        "label": "D",
    },
    "l1a_tls": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_tls_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level1a"],
        "label": "D",
    },
    # level 1b RDRs
    "l1b_qms": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_qms_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level1b"],
        "label": "D",
    },
    "l1b_gc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_gc_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level1b"],
        "label": "D",
    },
    # level 2 RDRs
    "l2_qms": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_qms_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level2"],
        "label": "D",
    },
    "l2_gc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_gc_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level2"],
        "label": "D",
    },
    "l2_tls": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_tls_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level2"],
        "label": "D",
    },
}
"""
These ancillary products are all just txt files:
    "l0_msg": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_msg_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level0"],
        "label": "D",
    },
    "l1a_msg": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_msg_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level1a"],
        "label": "D",
    },

The L1B TLS product type is described in samrdrl1b.cat, but wasn't present
in the archive.
    "l1b_tls": {
        "manifest": GEO_FILE,
        "fn_must_contain": ["_tls_", ".lbl"],
        "url_must_contain": ["mslsam_", "data", "level1b"],
        "label": "D",
    },

"""
