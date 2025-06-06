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
ATM_FILE = "atm"

file_information = {
    'odf': {'manifest': GEO_MRO_FILE,
            "fn_must_contain": ['.odf'],
            "url_must_contain": ['rss', '/odf'],
            "label": "D"},
    'rsr': {'manifest': GEO_MRO_FILE,
            "url_must_contain": ['rss', '/rsr'],
            "fn_regex": [r'\..*[^lbl]'],
            "label": "D"},
    'rsdmap': {'manifest': GEO_MRO_FILE,
               'fn_must_contain': ['.img'],
               'url_must_contain': ['rss', '/rsdmap'],
               "label": "D"},
    'shadr': {'manifest': GEO_MRO_FILE,
              'fn_must_contain': ['.tab'],
              'url_must_contain': ['rss', '/shadr'],
              "label": "D"},
    'shbdr': {'manifest': GEO_MRO_FILE,
              'fn_must_contain': ['.dat'],
              'url_must_contain': ['rss', '/shbdr'],
              "label": "D"},
    'sha_clone': {'manifest': GEO_MRO_FILE,
              'fn_must_contain': ['.tab'],
              'url_must_contain': ['rss-5', '/extras/clones'],
              "label": "D"},
    # temperature-pressure profiles
    'tps': {'manifest': ATM_FILE,
              'fn_must_contain': ['.TPS'],
              'url_must_contain': ['data/mrors_2001/tps'],
              "label": "D"},
        
    # Unsupported; support planned, low priority
    # The FILE_HEADER pointer opens, but the rest do not. Most pointer names do 
    # not match the object names, they're missing "FREQUENCY_" from the pointer 
    # names
#     'dlf': {'manifest': GEO_MRO_FILE,
#             'fn_must_contain': ['.dlf'],
#             'url_must_contain': ['rss','/ancillary/'],
#             "label": "D",},
    # Support not planned
    'tnf': {'manifest': GEO_MRO_FILE,
            'fn_must_contain': ['.tnf'],
            'url_must_contain': ['rss', '/tnf'],
            "label": "D",
            "support_np": True},
    'ancil': {'manifest': GEO_MRO_FILE,
            'fn_regex': [r'((ack)|(acp)|(agk)|(cck)|(ccp)|(eop)|(ion)|(ltf)|'
                         r'(mpd)|(sak)|(sck)|(scp)|(sff)|(spk)|(tro)|(wea))$'],
            'url_must_contain': ['rss','/ancillary/'],
            "label": "D",
            "support_np": True},
}
