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

GEO_FILE = "chan2"

file_information = {
    "cha_erm_hkd": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_cha_erm_hkd_20190914153735792.csv"
        ],
        "label": "D",
    },
    "cha_erm_sci": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_cha_erm_sci_ops_20251214092436743.csv"
        ],
        "label": "D",
    },
    "cla_l1": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_cla_l1_20251208T152411790_20251208T152417274.fits"
        ],
        "label": "D",
    },
    "iir_nci": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_iir_nci_20250902T0211471130_d_img_d18.qub"
        ],
        "label": "D",
    },
    "iir_nri": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_iir_nri_20191202T0639493114_d_img_d18.qub"
        ],
        "label": "D",
    },
    # too big in memory but doesn't have errors
    # so don't dump if you can't handle it
    "ohr_ncp": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_ohr_ncp_20251109T1305444583_d_img_d18.img"
        ],
        "label": "D",
        "support_np": True
    },
    "ohr_nrp": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_ohr_nrp_20190906T1246532096_d_img_d18.img"
        ],
        "label": "D",
    },
    # these are too big
    "sar_nrxl": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_sar_nrxl_20251106t221014810_d_r0b_xx_cp_xx_d18.dat"
        ],
        "label": "D",
        "support_np": True
    },
    "tmc_nca": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_tmc_nca_20191015T1021251544_d_img_d18.img"
        ],
        "label": "D",
    },
    # image too big
    "tmc_ncn": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_tmc_ncn_20260127T1155357132_d_img_d18.img"
        ],
        "label": "D",
        "support_np": True
    },
    "xsm_lvl1": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_xsm_20190912_v1_level1.fits"
        ],
        "label": "D",
    },
    "xsm_lvl2": {
        "manifest": GEO_FILE,
        "fn_must_contain": [
            "ch2_xsm_20190912_v1_level2.lc"
        ],
        "label": "D",
    },
}
