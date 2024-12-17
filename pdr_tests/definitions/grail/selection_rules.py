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
MANIFEST_FILE = "geograil"

file_information = {
# Raw Radio Science Data
    # Biased Open Loop File
    "rss_bof": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.bof'],
        "url_must_contain": ['grail-l-rss-2-edr-v1/grail_0201/bof'],
        "label": "D",
    },
    # Orbit Data File
    "rss_odf": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.odf'],
        "url_must_contain": ['grail-l-rss-2-edr-v1/grail_0201/odf'],
        "label": "D",
    },
    # Open Loop File
    "rss_olf": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['olf'],
        "url_must_contain": ['grail-l-rss-2-edr-v1/grail_0201/olf'],
        "label": "D",
    },
    # Radio Science Receiver
    "rss_rsr": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'[1-9][ab][1-9]$'],
        "url_must_contain": ['grail-l-rss-2-edr-v1/grail_0201/rsr'],
        "label": "D",
    },
    # Support not planned - BTM, TDM, TNF, XRF, and ancillary products
    "rss_unsupported": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((btm)|(tdm)|(tnf)|(xfr)|(eop)|(ion)|(tro)|(wea))$'],
        "url_must_contain": ['grail-l-rss-2-edr-v1/grail_0201/'],
        "url_regex": [r'(btm)|(tdm)|(tnf)|(xfr)|(ancillary)'],
        "label": "D",
        "support_np": True
    },
# Derived Lunar Gravitational Field Data; level 2 (PDS3 and PDS4)
    # Spherical Harmonics ASCII Data Records
    "lgrs_shadr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['grail-l-lgrs-5-rdr-v1/grail_1001/shadr'],
        "label": "D",
    },
    # Spherical Harmonics Binary Data Records
    "lgrs_shbdr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['grail-l-lgrs-5-rdr-v1/grail_1001/shbdr'],
        "label": "D",
    },
    # Radio Science Digital Map Products
    "lgrs_rsdmap": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['grail-l-lgrs-5-rdr-v1/grail_1001/rsdmap'],
        "label": "D",
    },
    # Ascii tables in the extras directory that are missing PDS labels
    "extras": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'(tab)|(asc)$'],
        "url_must_contain": ['grail-l-lgrs-5-rdr-v1/grail_1001/extras'],
        "label": "A",
        "support_np": True
    },
    # Spice kernels (I think the coverage manifest pipeline auto excludes 'spk' 
    # files at this point, so this ptype may be unnecessary)
    "spk": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.spk'],
        "url_must_contain": ['grail-l-lgrs-5-rdr-v1/grail_1001/spk'],
        "label": "D",
        "support_np": True
    },

    # Lunar Gravity Ranging System raw data; level 0
    # Unsupported: no pointers to data file, no table formatting given
    "lgrs_edr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.asc'],
        "url_must_contain": ['grail-l-lgrs-2-edr-v1/grail_0001', 'level_0'],
        "label": "D",
        "support_np": True
    },
    # calibrated/resampled LGRS data; level 1A/1B 
    # Unsupported: no pointers to data file, no table formatting given
    "lgrs_cdr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.asc'],
        "url_must_contain": ['grail-l-lgrs-3-cdr-v1/grail_0101/level_1'],
        "label": "D",
        "support_np": True
    },
}
