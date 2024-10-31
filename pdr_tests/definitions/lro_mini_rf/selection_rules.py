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
MANIFEST_FILE = "geolro"

file_information = {
    # Bistatic Radar EDRs
    "bsr_edr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['data/edr'],
        "url_regex": [r'(lromrf_2xxx)|(lromrf_3xxx)'],
        "label": 'D',
    },
    # Bistatic Radar RDRs
    "bsr_rdr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['data/rdr'],
        "url_regex": [r'(lromrf_2xxx)|(lromrf_3xxx)'],
        "label": 'D',
    },
    # Bistatic Radar DDRs
    "bsr_ddr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['data/ddr'],
        "url_regex": [r'(lromrf_2xxx)|(lromrf_3xxx)'],
        "label": 'D',
    },
    # Mini-RF Global Mosaic
    "mosaic": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['lro-l-mrflro-5-global-mosaic-v1', 'data'],
        "label": 'D',
    },
    # SAR Level 1; Calibrated Data Record
    "cdr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['lro-l-mrflro-4-cdr-v1', 'data', 'level1'],
        "label": 'D',
    },
    # SAR Level 2; Map-Projected Calibrated
    "projected": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['lro-l-mrflro-4-cdr-v1', 'data', 'level2'],
        "label": 'D',
    },
    # SAR Polar Mosaics
    "polar_mosaic": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['lro-l-mrflro-4-cdr-v1', 'data', 'mosaics'],
        "label": 'D',
    },
    # SAR housekeeping data
    "housekeeping": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['lro-l-mrflro-4-cdr-v1', 'data', 'housekeeping'],
        "label": 'D',
    },

    # SAR Raw Packetized Data Records; raw binary telemetry
    # Support not planned --> The parameter files (.txt) open, but there are 
    # no pointers to the data files (.dat).
    "raw": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'(dat$)|(DAT$)'],
        "url_must_contain": ['lro-l-mrflro-4-cdr-v1', 'data', 'raw'],
        "label": 'D',
        "support_np": True
    },
}
