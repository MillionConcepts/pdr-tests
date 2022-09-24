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
    
    # spacecraft engineering data; well-labeled fixed-length tables
    "ech": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['csv', '.ech'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },
    # engineering channels summary data; well-labeled fixed-length tables
    "ecs": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.ecs'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },
    # engineering telemetry data as function of time; well-labeled fixed-length tables
    "ect": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.ect'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },
    # filtered body rates; well-labeled fixed-length tables
    "fbr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.fbr'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },
    # DSN monitor data; well-labeled fixed-length tables
    "mch": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['csv', '.mch'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },
    # DSN monitor data as function of time; well-labeled fixed-length tables
    "mct": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.mct'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },
    # radio science receiver standard format data units; well-labeled fixed-length tables
    "rsr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.rsr'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },

    
}

"""

    # orbit data files; fixed-length tables
    # problem tables: 1B start dates are weird, 3B are nonsense after the first row, final table (7B or 8B) should be all 0 but sometimes has random values in first couple rows.
    "odf": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.odf'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },
    # original data records; fixed-length tables
    # does not open
    "odr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.odr'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },
    # tracking data file; fixed-length tables
    # an error is introduced several columns (18?) into table TDF5 and propagates through the rest of the table
    "tdf": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tdf'],
        "url_regex": [r'-rss-1-cru-|-rss-1-moi-|-rss-1-map-|-rss-1-ext-'],
        "label": "D",
    },

"""
