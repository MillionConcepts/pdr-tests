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
    # L2 / raw data
    # orbiter data; binary tables
    "l2_orbit": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_o', '.dat'],
        "url_must_contain": ['ro_rl-', '-consert-2-', '/data'],
        "label": "D",
    },
    # lander data; binary tables
    "l2_land": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_l', '.dat'],
        "url_must_contain": ['ro_rl-', '-consert-2-', '/data'],
        "label": "D",
    },
    # ground bench data; binary tables
    "l2_bench": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_2', '.dat'],
        "url_must_contain": ['ro_rl-', '-consert-2-', '/data'],
        "label": "D",
    },
    # auxiliary AOCS data; ascii tables
    "l2_aux": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_a', '.tab'],
        "url_must_contain": ['ro_rl-', '-consert-2-', '/data'],
        "label": "D",
    },
    # auxiliary temperature data; ascii tables
    "l2_temp": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "fn_regex": [r'(cn_t)|(cn_x)'],
        "url_must_contain": ['ro_rl-', '-consert-2-', '/data'],
        "label": "D",
    },
    # auxiliary current data; ascii tables
    "l2_current": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "fn_regex": [r'(cn_c)|(cn_y)'],
        "url_must_contain": ['ro_rl-', '-consert-2-', '/data'],
        "label": "D",
    },

    # L3 / calibrated data
    # orbiter data; binary tables
    "l3_orbit": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_o', '.dat'],
        "url_must_contain": ['ro_rl-', '/data'],
        "url_regex": [r'(-consert-3-[a-eg-z])|(consert-3-fss-v1\.0)'],
        "label": "D",
    },
    # similar to above, but uses a different format file w/ the same filename
    "l3_orbit_fss": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_o', '.dat'],
        "url_must_contain": ['ro_rl-c-consert-3-fss-v1.1/data'],
        "label": "D",
    },
    # lander data; binary tables
    "l3_land": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_l', '.dat'],
        "url_must_contain": ['ro_rl-', '/data'],
        "url_regex": [r'(-consert-3-[a-eg-z])|(consert-3-fss-v1\.0)'],
        "label": "D",
    },
    # similar to above, but uses a different format file w/ the same filename
    "l3_land_fss": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_l', '.dat'],
        "url_must_contain": ['ro_rl-c-consert-3-fss-v1.1/data'],
        "label": "D",
    },
    # auxiliary AOCS data; ascii tables
    "l3_aux": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_a', '.tab'],
        "url_must_contain": ['ro_rl-', '-consert-3-', '/data'],
        "label": "D",
    },

    # L4 / resampled data
    # orbiter data; binary tables
    "l4_orbit": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_o', '.dat'],
        "url_must_contain": ['ro_rl-', '/data'],
        "url_regex": [r'-consert-4-[a-fh-z]',],
        "label": "D",
    },
    # similar to above, but uses a different format file w/ the same filename
    "l4_orbit_grnd": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_o', '.dat'],
        "url_must_contain": ['ro_rl-', '/data'],
        "url_regex": [r'-consert-4-grnd',],
        "label": "D",
    },
    # lander data; binary tables
    "l4_land": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_l', '.dat'],
        "url_must_contain": ['ro_rl-', '-consert-4-', '/data'],
        "label": "D",
    },
    # auxiliary AOCS data; ascii tables
    "l4_aux": {
        "manifest": SB_FILE,
        "fn_must_contain": ['cn_a', '.tab'],
        "url_must_contain": ['ro_rl-', '-consert-4-', '/data'],
        "label": "D",
    },

    # tables in the geometry directories
    "l3_geom": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ro_rl-', '-consert-3-', 'v1.1/geometry'],
        "label": "D",
    },
    "l4_geom": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ro_rl-', '-consert-4-', '/geometry'],
        "label": "D",
    },
}
