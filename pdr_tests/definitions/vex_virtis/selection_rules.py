"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .parquet file that contains urls, file sizes, etc., scraped
directly from the hosting institution for this product type. for some data
sets, all urls will be found in the same .parquet file; for others, they may
be split between nodes or scraping sessions.

fn_must_contain: a list of strings that must be in the file name (not counting
directories, domains, etc.) to differentiate it from the other types in the
manifest file

url_must_contain: an optional additional list of strings that must be in the
url (counting the entire url) to differentiate this from other types in the
manifest file. useful for specifying directories.

label: "A" if the labels for this product type are attached; "D" if the labels
are detached.
"""

# All orbit directories are split in three subdirectories:
# RAW			contains all raw data files from the three channels
# CALIBRATED 		contains all calibrated files from the three channels
#  (including H calibrated darks)
# GEOMETRY 		contains all geometry files for the three channels
#
#
# File names are coded on 9.3 format as follows:
# V<channel + transfer mode><orbit number>_<sub-session number>.<ext>
# or
# VFxxxx_nn.EEE
#
# where:
# V is a literal "V" character
# F is the channel/transfer mode identifier (one alpha character):
#  H: H image transfer mode (backup observation mode)
#  S: H single spectrum transfer mode (including dark current files in nominal
#  mode)
#  T: H "64-spectra frame" transfer mode (nominal mode)
#  I: M-IR data
#  V: M-Vis data
# xxxx is the orbit number coded on exactly 4 digits (same as in directory
#  string)
# nn is the subsession ID (ID of file produced by this channel during this
#  orbit)
# EEE is the extension identifying the type and level of data (three alpha
#  characters):
#  QUB: raw data
#  GEO: geometry files
#  CAL: calibrated data
#  DRK: calibrated dark currents for H

# variables naming specific parquet files in node_manifests
PSA = "img_esa_ve"

file_information = {
    # Visible Infra Red Thermal Imaging Spectrometer

    # Raw / EDR
    "RAW": {
        "manifest": PSA,
        "fn_must_contain": ['.QUB'],
        "url_must_contain": ['VIRTIS', 'RAW'],
        "label": "A",
    },
    # Calibrated / RDR
    # bytes per pixel is .5, not allowed
    "CALIBRATED": {
        "manifest": PSA,
        "fn_must_contain": ['.CAL'],
        "url_must_contain": ['VIRTIS', 'CALIBRATED'],
        "label": "A",
        "support_np": True
    },
    # Calibrated / RDR
    # bytes per pixel is .5, not allowed
    "CALIBRATED_DARK": {
        "manifest": PSA,
        "fn_must_contain": ['.DRK'],
        "url_must_contain": ['VIRTIS', 'CALIBRATED'],
        "label": "A",
        "support_np": True
    },
    # Geometry File / EDR type
    # array wrong size compared to label
    "GEOM": {
        "manifest": PSA,
        "fn_must_contain": ['.GEO'],
        "url_must_contain": ['VIRTIS', 'GEO'],
        "label": "A",
        "support_np": True
    },
}

