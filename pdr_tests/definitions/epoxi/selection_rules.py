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
    # HRI-IR raw spectra
    "hrii_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['/data'],
        "url_regex": [r'dif-[ecm]-hrii-2-epoxi'],
        "label": "D",
    },
    # HRI-IR calibrated spectra
    "hrii_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', 'hrii-3_4-epoxi', '/data'],
        "label": "D",
    },
    # HRI-VIS raw images
    "hriv_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['/data'],
        "url_regex": [r'dif-[ecmx]-hriv-2-epoxi'],
        "label": "D",
    },
    # HRI-VIS calibrated images
    "hriv_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '/data'],
        "url_regex": [r'(hriv-3-epoxi)|(hriv-3_4-epoxi)'],
        "label": "D",
    },
    # HRI-VIS photometry (data available in 2 formats: .tab and .fit)
    "hriv_photometry": {
        "manifest": SBN_FILE,
        "fn_regex": [r'(tab$)|(fit$)'],
        "url_must_contain": ['dif-', 'hriv-5-epoxi-exoplanets-phot', '/data'],
        "label": "D",
    },
    # HRI-VIS deconvolved images
    "hriv_deconvolved": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', 'hriv-5-epoxi-hartley2-deconv', '/data'],
        "label": "D",
    },
    # HRI-VIS stellar PSFs
    "hriv_psf": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', 'hriv-6-epoxi-stellar-psfs', '/data'],
        "label": "D",
    },
    # MRI-VIS raw images
    "mri_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['/data'],
        "url_regex": [r'dif-[ecm]-mri-2-epoxi'],
        "label": "D",
    },
    # MRI-VIS calibrated images
    "mri_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', 'mri-3_4-epoxi', '/data'],
        "label": "D",
    },
    # MRI-VIS photometry is PDS4
    
    # derived shape model
    # 1 model, 2 projections/file formats
    "shape": {
        "manifest": SBN_FILE,
        "fn_regex": [r'(wrl$)|(tab$)'],
        "url_must_contain": ['dif-', 'hriv_mri-5-hartley2-shape', '/data'],
        "label": "D",
    },
    # in-flight calibrations (HRI-IR, HRI-VIS, and MRI-VIS)
    "calibrations": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['dif-', '-2-epoxi-calibrations', '/data'],
        "label": "D",
    },
    # spacecraft instrument temperatures
    "temps": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['dif-', 'hrii_hriv_mri-6-epoxi-temps', '/data'],
        "label": "D",
    },
}
