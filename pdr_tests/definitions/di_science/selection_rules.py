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
SBN_FILE = "tiny_other"

file_information = {
    # HRI-IR raw/calibration spectra - cruise & encounter phases
    "hrii_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-hrii-2-9p-', '/data/'],
        "label": "D",
    },
    # HRI-IR reduced/calibrated spectra
    "hrii_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-hrii-3_4-9p-', '/data/'],
        "label": "D",
    },
    # HRI-VIS raw/calibration images - cruise & encounter phases
    "hriv_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-hriv-2-9p-', '/data/'],
        "label": "D",
    },
    # HRI-VIS calibrated images
    "hriv_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-hriv-3_4-9p-', '/data/'],
        "label": "D",
    },
    # MRI-VIS raw/calibration images - cruise & encounter phases
    "mri_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-mri-2-9p-', '/data/'],
        "label": "D",
    },
    # MRI-VIS calibrated images
    "mri_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-mri-3_4-9p-', '/data/'],
        "label": "D",
    },
    # ITS-VIS raw/calibration images - cruise & encounter phases
    "its_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dii-', '-its-2-9p-', '/data/'],
        "label": "D",
    },
    # ITS-VIS calibrated images
    "its_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dii-', '-its-3_4-9p-', '/data/'],
        "label": "D",
    },
    # derived shape model; 2 versions in different projections
    "shape": {
        "manifest": SBN_FILE,
        "fn_regex": [r'(wrl$)|(tab$)'],
        "url_must_contain": ['dif-c-hriv_its_mri-5-tempel1-shape-', '/data'],
        "label": "D",
    },
    # photometry of MRI-VIS observations
    "photometry": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['dif-c-mri-5-tempel1-photometry', '/data'],
        "label": "D",
    },
    # derived surface temperature maps; most are images, there is 1 table
    "temp_maps": {
        "manifest": SBN_FILE,
        "fn_regex": [r'(fit$)|(tab$)'],
        "url_must_contain": ['dif-c-hrii-5-tempel1-surf-temp-maps', '/data'],
        "label": "D",
    },
    # IRAS images derived from sky survey atlas scans and pointed observations
    "iras_img_survey": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_iras-c-fpa-5-9p-images-v1.0/data/survey'],
        "label": "D",
    },
    "iras_img_pointed": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_iras-c-fpa-5-9p-images-v1.0/data/ao'],
        "label": "D",
    },
    # IRAS beam size tables for pointed images
    "iras_beamsize": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['di_iras-c-fpa-5-9p-images-v1.0/data'],
        "label": "D",
    },
    # IRAS photometry tables derived from reconstructed survey/pointed images
    "iras_photometry": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['di_iras-c-fpa-5-9p-phot-v1.0/data'],
        "label": "D",
    },

    # 9P/Tempel 1 approach/encounter movies
    # "UserWarning: The MOVIE pointer is not yet fully supported."
    # MPEG file format
    "movie": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.mpg'],
        "url_must_contain": ['di-c-hriv_its_mri-5-movie-coll', '/data'],
        "label": "D",
        "support_np": True
   },

    # Unsupported - no PDS labels
    # (Includes products from datasets that are otherwise covered by 
    # ptypes in di_nav)
    "notes": {
        "manifest": SBN_FILE,
        "url_must_contain": ['/NOTES'],
        "url_regex": [r'(dif-)|(dii-)|(di_iras)'],
        "label": "NA",
        "support_np": True
    },
    "code": {
        "manifest": SBN_FILE,
        "url_must_contain": ['/CODE'],
        "url_regex": [r'(dif-)|(dii-)'],
        "label": "NA",
        "support_np": True
    },
}
