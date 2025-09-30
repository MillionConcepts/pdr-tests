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
    "EDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ['crism', "/edr/"],
        "label": "D",
    },
    # These tables are part of the EDR ptype above and are fully supported; 
    # the EDR product labels have pointers to .img and .tab files. 
    # This EDR_additional_files ptype is to make sure the .tab files are 
    # counted correctly in the coverage analysis pipeline. 
    # The "ix_skip" flag ensures they are skipped on all ix calls that do not 
    # specifically pass this ptype.
    "EDR_additional_files": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['crism', "/edr/"],
        "label": "A", # shares labels with EDR ptype above
        "ix_skip": True
    },
    "CDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ['crism', "/cdr/"],
        "label": "D",
    },
    "DDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['crism', '/ddr/'],
        "label": "D",
    },
    "LDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['crism', '/ldr/'],
        "label": "D",
    },
    "TRDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ['crism', "/trdr/"],
        "label": "D",
    },
    # These tables are part of the TRDR ptype above and are fully supported; 
    # the TRDR product labels have pointers to .img and .tab files. 
    # This TRDR_additional_files ptype is to make sure the .tab files are 
    # counted correctly in the coverage analysis pipeline. 
    # The "ix_skip" flag ensures they are skipped on all ix calls that do not 
    # specifically pass this ptype.
    "TRDR_additional_files": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['crism', "/trdr/"],
        "label": "A", # shares labels with EDR ptype above
        "ix_skip": True
    },
    "MRDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ['crism', '/mrdr/'],
        "label": "D",
    },
    "TER": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": [".img"],
        "url_must_contain": ['crism', "/ter/"],
        "label": "D",
    },
    "MTRDR": {
        "manifest": GEO_MRO_FILE,
        "fn_must_contain": ['.img'],
        'url_must_contain': ['crism', '/mtrdr'],
        "label": "D",
    },
    'speclib': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['.tab'],
        'url_must_contain': ['crism', 'speclib-v1'],
        'label': "A",
    },
    'typespec': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['.tab'],
        'url_must_contain': ['crism', 'typespec-v1'],
        'label': 'D',
    },
    
    # These appear to be ancillary tables
    'ancil_cdr': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['.tab'],
        'url_must_contain': ['crism', 'cdr'],
        'label': 'D',
    },
    'ancil_rdr': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['.tab'],
        'url_must_contain': ['crism-4-rdr', 'ter'],
        'label': 'D',
    },
    'ancil_mrdr': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['.tab'],
        'url_must_contain': ['crism-5-rdr', 'mrdr'],
        'url_regex': [r'mrocr_3[12]'],
        'label': 'D',
    },
    # Products in the extras directories
    'extras_cdr': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['cdr', '.tab'],
        'url_must_contain': ['crism-2-edr', '/extras/'],
        'label': 'D',
    },
    'extras_obs': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['obs', '.tab'],
        'url_must_contain': ['crism-2-edr', '/extras/'],
        'label': 'D',
    },
    'extras_csv': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['.csv'],
        'url_must_contain': ['crism-2-edr', '/extras/'],
        'label': 'D',
        "support_np": True # These are text files using the DOCUMENT pointer
    },
    'extras_xls': {
        'manifest': GEO_MRO_FILE,
        'fn_must_contain': ['.xls'],
        'url_must_contain': ['crism-4-rdr', '/extras/'],
        'label': 'A', # no PDS label
        "support_np": True
    },
}
