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
GEO_FILE = "geomgs"
"""
# The MGS science sampler is mirrored at ATM and IMG
IMG_FILE = "img_usgs_mars-global-surveyor"
ATM_FILE = "atm"
"""

file_information = {
    "mager": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.gif'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/mager'],
        "label": "D",
    },
    "moc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.gif'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/moc'],
        "label": "D",
    },
    "mola_pedr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.b'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/mola/pedr'],
        "label": "A",
    },
    # one product opens wrong because of mistakes in the data file (AP00026V.TAB)
    "mola_pedr_asc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/mola/pedr'],
        "label": "D",
    },
    "rss_img": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/rss'],
        "label": "D",
    },
    "rss_sha": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.sha'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/rss'],
        "label": "D",
    },
    "tes_rad": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['r.tab'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/tes/radiance'],
        "label": "A",
    },
    "tes_temp": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.gif'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/tes/tempimg'],
        "label": "D",
    },
    "geometry": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/geometry'],
        "label": "D",
    },
}
"""
support planned, see the mgs_mola selection rules for details
    "mola_aedr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.b'],
        "url_must_contain": ['mgs/mgs-sampler/mgs_0001', '/mola/aedr'],
        "label": "A",
    },
"""
