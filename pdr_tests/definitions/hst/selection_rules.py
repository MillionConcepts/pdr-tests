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
GEO_FILE = "geomars"
RMS_FILE = "ringvolumes"
ATM_FILE = "atm"

file_information = {
    
    # Wide Field Planetary Camera 2 Observations of Mars
    # spectral cubes
    "mars_cube": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.cub'],
        "url_must_contain": ['hst-m-wfpc2-3-v1/hstm_0001/data'],
        "label": "D",
    },
    # FITS images
    "mars_image": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['hst-m-wfpc2-3-v1/hstm_0001/data'],
        "label": "D",
    },
    
    # HST WFPC2 astrometry of Saturn's moons, 1994-2002
    "sat_moons_94": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ASTROM_xxxx/ASTROM_0001/DATA/EASYDATA'],
        "label": "D",
    },
    # HST WFPC2 astrometry of Saturn's moons, 1996-2005
    "sat_moons_96": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ASTROM_xxxx/ASTROM_0101/DATA/EASYDATA'],
        "label": "D",
    },

    # HST WFPC2 observations of Jupiter during the comet Shoemaker-Levy 9 impact
    "jup_sl9_impact": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_regex": [r'sl9_000[56]/wfpc2/'],
        "label": "D",
    },
    
}
