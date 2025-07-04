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
MANIFEST_FILE = "geomgs"

file_information = {
    
    # May be missing product types due to the many unique file extensions and an archive layout that makes finding them difficult.
    
    # spacecraft engineering data; well-labeled fixed-length tables
    "ech": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'^((csv)|(CSV)).*((ech)|(ECH))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # engineering channels summary data; well-labeled fixed-length tables
    "ecs": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.ecs'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # engineering telemetry data as function of time; well-labeled fixed-length tables
    "ect": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((ect)|(ECT))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # filtered body rates; well-labeled fixed-length tables
    "fbr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.fbr'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # DSN monitor data; well-labeled fixed-length tables
    "mch": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'^((csv)|(CSV)).*((mch)|(MCH))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # DSN monitor data as function of time; well-labeled fixed-length tables
    "mct": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((mct)|(MCT))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # radio science receiver standard format data units; well-labeled fixed-length tables
    "rsr": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((rsr)|(RSR))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
        
    # orbit data files; fixed-length tables
    "odf": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((odf)|(ODF))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # original data records; fixed-length tables
    # include 'BCD' and 'Binary Coded Decimal' DATA_TYPES
    "odr": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((odr)|(ODR))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # tracking data file; fixed-length tables
    "tdf": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((tdf)|(TDF))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
    },
    # UltraStable Oscillator data; fixed-length tables
    "uso": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mgs-m-rss-1-', 'uso'],
        "label": "D",
    },
    
    
    # support not planned  - stream and undefined RECORD_TYPEs
    "unsupported": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((agk)|(amd)|(dkf)|(ps[123])|(eop)|(gd[nf])|(ion)|(ipn)|'
                     r'(lit)|(mif)|(mp[dfk])|(opt)|(sak)|(sfo)|(soe)|(spk)|'
                     r'(tck)|(tro)|(tnf)|(wea))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
        "support_np": True
    },
    "unsupported_upper": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((AGK)|(AMD)|(DKF)|(EOP)|(ION)|(MPD)|(OPT)|(SAK)|(SOE)|'
                     r'(SPK)|(TCK)|(TRO)|(PS1)|(WEA))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
        "support_np": True
    },
    # The ech and mch products have 2 verions: filenames that start with 'csv' 
    # are supported products, the rest are not
    "unsupported_ech_mch": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'^(([0-9])|(g)|(h)).*((mch)|(MCH)|(ech)|(ECH))$'],
        "url_must_contain": ['mgs-m-rss-1-'],
        "label": "D",
        "support_np": True
    },
}
