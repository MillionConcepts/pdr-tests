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
GEO_MESSENGER_FILE = "geomessenger"

file_information = {

    # Note: this whole volume is safed rather than officially archived.
    # Any unsupported data is very low priority for support, or just 'support 
    # not planned'

    "mdis": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".FIT"],
        "url_must_contain": ['ground_cal', 'MDIS/DATA'],
        "label": "D",
    },
	# most products are supported.
	# products ending in TIM_BST are known unsupported (format file is missing from archive)
    "mag": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".TAB"],
        "url_must_contain": ['ground_cal', 'MAG/DATA'],
        "label": "D",
    },
    # most products are supported.
    # products with filenames ending in BM are known unsupported (label, format, and data files not in agreement)
    "fips": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".CSV"],
        "url_must_contain": ['ground_cal', 'FIPS/DATA'],
        "label": "D",
    },
    # notionally supported
    # labels expect ".TXT.TXT" extensions to filenames
    "eps": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".TXT"],
        "url_must_contain": ['ground_cal', 'EPS/DATA'],
        "label": "D",
    },
    # supported
    "grs": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".TXT"],
        "url_must_contain": ['ground_cal', 'GRS/DATA'],
        "label": "D",
    },
    # supported
    "xrs": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".TXT"],
        "url_must_contain": ['ground_cal', 'XRS'],
        "label": "D",
    },
    # one label can have multiple (CSV) data files 
    # notionally supported (several data files have incorrect filenames and do not match labels)
    "mla": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".LBL"],
        "url_must_contain": ['ground_cal', 'MLA/DATA'],
        "label": "D",
    },
    # known unsupported; no PDS labels
    "mla_extras": {
        "manifest": GEO_MESSENGER_FILE,
        # "fn_regex": [r"(XLS)|(QPC)|(PRN)|(MCD)|(PPT)$"],
        "url_must_contain": ['ground_cal', 'MLA/DATA', 'EXTRAS'],
        "support_np": True
    },

    #known unsupported (not planned); no END_OBJECT for TABLE in the label
    "ns": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".BIN"],
        "url_must_contain": ['ground_cal', '/NS/DATA'],
        "label": "D",
        "support_np": True
    },
    # known unsupported; format file is a draft version
    "mascs": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['ground_cal', '/MASCS'],
        "label": "D",
        "support_np": True
    },
    # known unsupported; ascii text documents
    "ascii_docs": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".ASC"],
        "url_must_contain": ['ground_cal'],
        "label": "D",
        "support_np": True
    },
}
