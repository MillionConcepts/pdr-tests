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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
GEO_FILE = Path(MANIFEST_DIR, "geopremgn.parquet")

file_information = {
    # Earth-based Venus observations; Arecibo and Goldstone observatories
    "eb_venus": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['ven', '.img'],
        "url_must_contain": ['premgn/mg_1001/ebvenus'],
        "label": "D",
    },
    # Pioneer Venus orbiter observations; gravity and radar data
    "pi_venus_tab": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['ven', '.dat'],
        "url_must_contain": ['premgn/mg_1001/pvvenus'],
        "label": "D",
    },
##    "pi_venus_img": {  # unsupported; SAMPLE_TYPE = VAX_REAL
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['ven', '.img'],
##        "url_must_contain": ['premgn/mg_1001/pvvenus'],
##        "label": "D",
##    },
    # Earth observations from AIRSAR instrument (unsupported; SAMPLE_TYPE = VAX_REAL)
##    "airsar": {
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['eth', '.img'],
##        "url_must_contain": ['premgn/mg_1001/airsar'],
##        "label": "D",
##    },
    # Earth-based Mars observations
    "eb_mars_tab": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['mar', '.dat'],
        "url_must_contain": ['premgn/mg_1001/ebmars'],
        "label": "D",
    },
    "eb_mars_img": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['mar', '.img'],
        "url_must_contain": ['premgn/mg_1001/ebmars'],
        "label": "D",
    },
    # Earth-based Mercury observations
    "eb_merc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['mer', '.dat'],
        "url_must_contain": ['premgn/mg_1001/ebmerc'],
        "label": "D",
    },
    # Earth-based Lunar observations; Arecibo and Haystack observatories
    "eb_moon": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['lun', '.img'],
        "url_must_contain": ['premgn/mg_1001/ebmoon'],
        "label": "D",
    },
    # Viking orbiter Mars gravity observations
    "vi_mars": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['mar', '.dat'],
        "url_must_contain": ['premgn/mg_1001/vikgrav'],
        "label": "D",
    },
}
