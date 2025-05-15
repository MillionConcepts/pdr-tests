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

RMS_FILE = "ringvolumes"

file_information = {
	
    # occultation data - only on RMS node as far as I can tell
    
    # VIMS occultation data
    "vims": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['COVIMS_8xxx/COVIMS_8001/data'],
        "label": 'D',
    },
    "vims_old": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_regex": [r'COVIMS_8xxx_v(1|2.0)/COVIMS_8001/((data)|(EASYDATA))'],
        "label": 'D',
    },
    # UVIS occultation data
    "uvis": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['COUVIS_8xxx/COUVIS_8001/data'],
        "label": 'D',
    },
    "uvis_old": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_regex": [r'COUVIS_8xxx_v(1|2.[01])/COUVIS_8001/((data)|(DATA))'],
        "label": 'D',
    },
    # RSS occultation data
    "rss": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CORSS_8xxx/CORSS_8001/data'],
        "label": 'D',
    },
    "rss_old": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['CORSS_8xxx_v1/CORSS_8001/EASYDATA'],
        "label": 'D',
    },
}
