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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
RMS_FILE = Path(MANIFEST_DIR, "ringvolumes.parquet")

file_information = {
    # Hubble Space Telescope (HST) - raw and calibrated images, and
    # engineering data
    # These are still running into FITS issues.
##    "hst_raw_img": {
##        "manifest": RMS_FILE,
##        "fn_must_contain": ['.FITS'],
##        "url_must_contain": ['RAWIMAGE'],
##        "url_regex": [r'RPX_xxxx/RPX_000./199'],
##        "label": "D",
##    },
##    "hst_raw_mask": {
##        "manifest": RMS_FILE,
##        "fn_must_contain": ['.FITS'],
##        "url_must_contain": ['RAWMASK'],
##        "url_regex": [r'RPX_xxxx/RPX_000./199'],
##        "label": "D",
##    },
##    "hst_cal_img": {
##        "manifest": RMS_FILE,
##        "fn_must_contain": ['.FITS'],
##        "url_must_contain": ['CALIMAGE'],
##        "url_regex": [r'RPX_xxxx/RPX_000./199'],
##        "label": "D",
##    },
##    "hst_cal_mask": {
##        "manifest": RMS_FILE,
##        "fn_must_contain": ['.FITS'],
##        "url_must_contain": ['CALMASK'],
##        "url_regex": [r'RPX_xxxx/RPX_000./199'],
##        "label": "D",
##    },
##    "hst_eng_data": {
##        "manifest": RMS_FILE,
##        "fn_must_contain": ['.FITS'],
##        "url_must_contain": ['ENGDATA'],
##        "url_regex": [r'RPX_xxxx/RPX_000./199'],
##        "label": "D",
##    },
##    "hst_eng_mask": {
##        "manifest": RMS_FILE,
##        "fn_must_contain": ['.FITS'],
##        "url_must_contain": ['ENGMASK'],
##        "url_regex": [r'RPX_xxxx/RPX_000./199'],
##        "label": "D",
##    },
    # William Herschel Telescope (WHT) - images and spectra
    "wht_cal_img": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0101/DATA', 'IMAGES/CALIMAGE'],
        "label": "D",
    },
    "wht_raw_img": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0101/DATA', 'IMAGES/RAWIMAGE'],
        "label": "D",
    },
    "wht_raw_isis": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0101/DATA', 'SPECTRA/RAWISIS'],
        "label": "D",
    },
    "wht_cal_isis": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0101/DATA', 'SPECTRA/CALISIS'],
        "label": "D",
    },
    "wht_easy_isis": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['RPX_xxxx/RPX_0101/DATA', 'SPECTRA/EASYISIS'],
        "label": "D",
    },
    "wht_raw_api": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0101/DATA', 'SPECTRA/RAWAPI'],
        "label": "D",
    },
    # NASA Infra Red Telescope Facility (IRTF) - Saturn system and sky images
    "irtf_calibrated": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['_CAL.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0201/DATA'],
        "label": "D",
    },
    "irtf_calsky": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['_CALSKY.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0201/DATA'],
        "label": "D",
    },
    "irtf_raw": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['_RAW.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0201/DATA'],
        "label": "D",
    },
    "irtf_rawsky": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['_RAWSKY.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0201/DATA'],
        "label": "D",
    },
    # Canada France Hawaii Telescope (CFHT) - images
    "cfht_raw": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['_RAW.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0301/DATA'],
        "label": "D",
    },
    "cfht_processed": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['_PROC.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0301/DATA'],
        "label": "D",
    },
    # Wisconsin-Indiana-Yale-NOAO Telescope (WIYN) - images
    "wiyn_raw": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['_RAW.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0401/DATA'],
        "label": "D",
    },
    "wiyn_processed": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['_PROC.IMG'],
        "url_must_contain": ['RPX_xxxx/RPX_0401/DATA'],
        "label": "D",
    },
}
