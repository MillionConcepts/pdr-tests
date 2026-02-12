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

# For all ISRO missions, this is referencing a "fake" manifest with one
# example file for each dtype, just so I can run ix.
# For ISRO files, it's not possible to scrape the website & download them
# the way we do with the PDS.

GEO_FILE = "chan3"

file_information = {
    "apx_hk_lvl1": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_apx_obs20_mob34_20230831_v1_level1.hk"
        ],
        "label": "D",
    },
    "apx_lvl1": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_apx_obs20_mob34_20230831_lunobs_v1_level1.fits"
        ],
        "label": "D",
    },
    "cht_cal": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_cht_cal_20230831T01_745726827_v1.csv"
        ],
        "label": "D",
    },
    "cht_raw": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_cht_raw_20230829T00_876027888_v1.csv"
        ],
        "label": "D",
    },
    "ils_nop_accln": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_ils_nop_calib_20230828t001500008_d_accln.csv"
        ],
        "label": "D",
    },
    "ils_nop_rawcount": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_ils_nop_raw_20230831t000000000_d_rawcount.csv"
        ],
        "label": "D",
    },
    "lib_l0": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_lib_034_20230831T051804_00_l0.csv"
        ],
        "label": "D",
    },
    "lib_l0_0_1": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_lib_034_20230831T051804_00_l0_0_1.csv"
        ],
        "label": "D",
    },
    "lib_l0_0_3": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_lib_034_20230831T051804_00_l0_0_3.csv"
        ],
        "label": "D",
    },
    "lib_l0_1_2": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_lib_034_20230831T051804_00_l0_1_2.csv"
        ],
        "label": "D",
    },
    "lib_l1_1_5": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_lib_034_20230831T051804_05_l1_1_5.csv"
        ],
        "label": "D",
    },
    "lim_nc3": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_lim_nc3_20230904T2156569920_d_img_d32_1_160.jpg"
        ],
        "label": "D",
    },
    "nav_nrr": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_nav_nrr_20230902T0859039663_d_img_nno_047.png"
        ],
        "label": "D",
    },
    "rim_nc1": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_rim_nc1_20230902T0205274346_d_img_gnh_2_0.jpg"
        ],
        "label": "D",
    },
    "rlp_erA_ops": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_rlp_erA_ops_20230730T040828040.csv"
        ],
        "label": "D",
    },
    "rlp_erA_sci": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_rlp_erA_sci_20230730T040828040.csv"
        ],
        "label": "D",
    },
    "rlp_lr_ops": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_rlp_lr_ops_20230812T040525760.csv"
        ],
        "label": "D",
    },
    "rlp_lr_sci": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_rlp_lr_sci_20230812T040525760.csv"
        ],
        "label": "D",
    },
    "rlp_nrB_ops": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_rlp_nrB_ops_20230824T131435752.csv"
        ],
        "label": "D",
    },
    "rlp_nrB_sci": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch3_rlp_nrB_sci_20230824T223156464.csv"
        ],
        "label": "D",
    },
}
