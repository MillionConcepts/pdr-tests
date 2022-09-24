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
MANIFEST_FILE = Path(MANIFEST_DIR, "geomgs.parquet")

file_information = {
    
    # May be missing product types due to the many unique file extensions and an archive layout that makes finding them difficult.
    
    # ionospheric electron density profile; fix-length tables
    # header tables have data table appended as additional rows
    "eds": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.eds'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # mix of gravitational acceleration and geoid images; well-labeled 2-dimensional arrays (images)
    "img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex" : [r'ggm|gom'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # line of sight acceleration profile; fix-length tables
    # header tables have data table appended as additional rows
    "los": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.los'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # occultation measurements; well-labeled fix-length tables
    "ocs": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.ocs'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # spherical harmonic model of gravity field; well-labeled fix-length tables
    "sha": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.sha'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # spherical harmonic model of gravity field; well-labeled fix-length tables
    "shb": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.shb'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # viewing geometry for BSR; well-labeled 2-dimensional arrays (images)
    "srg": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.srg'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # power vs frequency and time near MGS radio occultation; well-labeled 2-dimensional arrays (images)
    "sri": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.sri'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # radio occultation surface echos; well-labeled fix-length tables
    # header tables have data table appended as additional rows
    "srt": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.srt'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # atmospheric temperature-pressure profile; fixed-length tables
    # header tables have data table appended as additional rows
    "tps": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tps'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    # power spectra from BSR; well-labeled fix-length tables
    "spc": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.spc'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },
    
}

"""

    # same as img but these have a typo in their labels: SAMPLE_TYPE                = "IEEE REAL"
    "img_typo": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex" : [r'jgm|jgd|jod'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },

    # Adobe PostScript files; out of scope
    "bro": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.ps1'],
        "url_must_contain": ['-rss-5-sdp-'],
        "label": "D",
    },

"""
