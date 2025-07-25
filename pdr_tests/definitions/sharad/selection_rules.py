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
GEO_MRO_FILE = "geomro_full"

file_information = {
    'EDR': {'manifest': GEO_MRO_FILE,
            "fn_must_contain": ['_s.dat'],
            "url_must_contain": ['sharad', '-edr-', '/data/'],
            "label": ("_s.dat", ".lbl"),
            "regex": True},
    # The way the EDR rules are written leaves the AUXILIARY_DATA_TABLE and 
    # label files marked as uncovered in the coverage analysis pipeline. This 
    # ptype explicitly includes them so the coverage metrics are correct. 
    # The "ix_skip" flag ensures they are skipped on all ix calls that do not 
    # specifically pass this ptype.
    'EDR_additional_files': {'manifest': GEO_MRO_FILE,
            "fn_regex": [r'((lbl)|(LBL)|(_a.dat))$'],
            "url_must_contain": ['sharad', '-edr-', '/data/'],
            "label": "A", # not actually attached labels, but don't want to double count them when counting coverage 
            "ix_skip": True},
    'RDR': {'manifest': GEO_MRO_FILE,
            "fn_regex": ['(dat$)|(DAT$)'],
            "url_must_contain": ['sharad', '/data/', '-rdr-'],
            "label": "D"},
    'rgram': {'manifest': GEO_MRO_FILE,
              'fn_must_contain': ['.img'],
              'url_must_contain': ['sharad', '/rgram/'],
              "label": "D"},
    'geom': {'manifest': GEO_MRO_FILE,
             'fn_must_contain': ['.tab'],
             'url_must_contain': ['sharad', '/geom/'],
             "label": "D"},
}
