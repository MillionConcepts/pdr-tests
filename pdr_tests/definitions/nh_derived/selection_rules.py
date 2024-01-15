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
    # Pluto surface composition maps:
    "absorp": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['nh-p_psa-leisa_mvic-5-comp-v1.0/data', 'absorp'],
        "label": "D",
    },
    "color_fit": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-p_psa-leisa_mvic-5-comp-v1.0/data', 'color'],
        "label": "D",
    },
    "color_img": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['nh-p_psa-leisa_mvic-5-comp-v1.0/data', 'color'],
        "label": "D",
    },
    "mosaic": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['nh-p_psa-leisa_mvic-5-comp-v1.0/data', 'mosaic'],
        "label": "D",
    },
    "spectral": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-p_psa-leisa_mvic-5-comp-v1.0/data', 'spec'],
        "label": "D",
    },
    
    # Pluto and Charon geology and geophysical maps:
    "geo_maps": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['nh-p_psa-lorri_mvic-5-geophys-v1.0/data'],
        "label": "D",
    },
    
    # Pluto atmospheric data:
    # v2.0 is the most recent version of the dataset, but is not included in
    # tiny.parquet yet. star_occ is missing from v1.0, but other products look
    # largely unchanged between versions.
    "alice_occ": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['nh-p_psa-lorri_alice_rex-5-atmos-', '/data', 'aliceocc'],
        "label": "D",
    },
    "atmos_comp": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['nh-p_psa-lorri_alice_rex-5-atmos-', '/data', 'atmoscomp'],
        "label": "D",
    },
    "haze": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['nh-p_psa-lorri_alice_rex-5-atmos-', '/data', 'haze'],
        "label": "D",
    },
    "rex_atmos": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['nh-p_psa-lorri_alice_rex-5-atmos-', '/data', 'rexatmos'],
        "label": "D",
    },
##    "star_occ": {
##        "manifest": SB_FILE,
##        "fn_must_contain": ['.fit'],
##        "url_must_contain": ['nh-p_psa-lorri_alice_rex-5-atmos-v2.0/data', 'starocc'],
##        "label": "D",
##    },
    "therm_scan": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['nh-p_psa-lorri_alice_rex-5-atmos-', '/data', 'thermscan'],
        "label": "D",
    },
    
}
