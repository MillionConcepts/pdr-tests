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
SB_FILE = "tiny_new_horizons"

file_information = {
    # The raw/EDR products sometimes have a typo where the
    # EXTENSION_HK_0X096_HEADER pointer is replaced by a duplicate
    # EXTENSION_SSR_SH_HEADER pointer. A special case opens
    # EXTENSION_SSR_SH_HEADER_0 as the HK_0X096 header and leaves
    # EXTENSION_SSR_SH_HEADER_1 as the SSR_SH header.
        
    # post-launch raw and calibrated data
    "launch_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-rex-2-launch-v2.0/data'],
        "label": "D",
    },
    "launch_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-rex-3-launch-v1.0/data'],
        "label": "D",
    },
    # jupiter flyby raw and calibrated data
    "jupiter_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-j-rex-2-jupiter-v2.0/data'],
        "label": "D",
    },
    "jupiter_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-j-rex-3-jupiter-v1.0/data'],
        "label": "D",
    },
    # pluto cruise raw and calibrated data
    "cruise_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-rex-2-plutocruise-v2.0/data'],
        "label": "D",
    },
    "cruise_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-rex-3-plutocruise-v1.0/data'],
        "label": "D",
    },
    # pluto encounter raw and calibrated data
    "pluto_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-p-rex-2-pluto-v2.0/data'],
        "label": "D",
    },
    "pluto_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-p-rex-3-pluto-v1.0/data'],
        "label": "D",
    },
    
    # KEM Cruise 1 raw and calibrated data
    "kem_cruise_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-rex-2-kemcruise1-v2.0/data'],
        "label": "D",
    },
    "kem_cruise_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-x-rex-3-kemcruise1-v2.0/data'],
        "label": "D",
    },
    # arrokoth encounter raw and calibrated data
    "arrokoth_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-a-rex-2-kem1-v','.0/data'],
        "label": "D",
    },
    "arrokoth_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-a-rex-3-kem1-v','.0/data'],
        "label": "D",
    },
    # Uplink tuning profiles extracted from TNFs
    "tnf_uplink": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['nh-','-rex-','data/tnf'],
        "label": "D",
    },
    # TNF --> unsupported, support not planned (incomplete/non-compliant labels)
    "tnf_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tnf'],
        "url_must_contain": ['nh-','-rex-','data/tnf'],
        "label": "D",
        "support_np": True,
    },
}
