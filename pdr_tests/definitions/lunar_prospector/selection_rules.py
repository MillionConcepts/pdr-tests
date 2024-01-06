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
GEO_FILE = "geolunar"
PPI_FILE = "plasm_full"

file_information = {
    # Line of Sight Acceleration Profile Data Record 
    "losapdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.los'],
        "url_must_contain": ['lp-l-rss-5-los-v1'],
        "url_regex": [r'(nominal)|(extended)'],
        "label": "D",
    },
    # Electron Reflectometer (ER) high resolution data
    "er_rdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-3-RDR-HIGHRESFLUX-V1.0', 'ER_HI_TS'],
        "label": "D",
    },
    # ER low resolution data
    "er_summ": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-4-SUMM-OMNIDIRELEFLUX-V1.0', 'ER_LO_TS'],
        "label": "D",
    },
    # ER omni-directional 3-D electron flux data
    "er_3d": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-3-RDR-3DELEFLUX-80SEC-V1.0', 'ER_3D'],
        "label": "D",
    },
    # ER level 2 data
    "er_lvl2": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-4-ELECTRON-DATA-V1.0/DATA'],
        "label": "D",
    },
    # Magnetometer (MAG) 
    "mag_summ": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-4-SUMM-LUNARCRDS-5SEC-V1.0/DATA/MAG'],
        "label": "D",
    },
    # MAG level 2 data
    "mag_lvl2": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-4-LUNAR-FIELD-TS-V1.0/DATA'],
        "label": "D",
    },
    # MAG level 3 data: Regional Field Maps
    "mag_lvl3": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-5-LUNAR-FIELD-BINS-V1.0/DATA'],
        "label": "D",
    },
    # MAG level 4 data: Large-Scale Vector Field Maps
    "mag_lvl4": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-5-SURFACE-FIELD-MAP-V1.0/DATA'],
        "label": "D",
    },
    # level 0 data: spacecraft attitude
    "attitude": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ENG-6-ATTITUDE-V1.0/DATA/ATTITUDE'],
        "label": "D",
    },
    # level 0 data: spacecraft trajectory 
    "trajectory": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-6-TRAJECTORY-V1.0/DATA'],
        "label": "D",
    },
    # level 0 data: commands sent to the spacecraft
    "command": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ENG-6-COMMAND-V1.0/DATA/COMMAND'],
        "label": "D",
    },
}
