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
SB_FILE = Path(MANIFEST_DIR, "tiny_rosetta.parquet")

file_information = {
    
# start ALICE data products

    "HK_alice": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['holdings/ro-', '-alice-2-', '/data'],
        "label": "D",
    },
    
    # These are FITS tables and need additional consideration:
    
#     "EDR_alice": {
#         "manifest": SB_FILE,
#         "fn_must_contain": ['.fit'],
#         "url_must_contain": ['holdings/ro-', '-alice-2-', '/data'],
#         "label": "D",
#     },
#     "RDR_alice": {
#         "manifest": SB_FILE,
#         "fn_must_contain": ['.fit'],
#         "url_must_contain": ['holdings/ro-', '-alice-3-', '/data'],
#         "label": "D",
#     },
#     "REFDR_alice": {
#         "manifest": SB_FILE,
#         "fn_must_contain": ['.fit'],
#         "url_must_contain": ['holdings/ro-', '-alice-4-', '/data'],
#         "label": "D",
#     },
    
# start MIRO data products

	# data acquired prior to arrival at comet 67P/CHURYUMOV-GERASIMENKO use a different 
	# format file than data acquired at the comet, so they are separated here.
    "EDR_miro_prior": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-miro-2-', '/data'],
        "url_regex": [r'(ro-a)|(ro-cal)|(ro-e)|(ro-x)|(ro-c-miro-2-cr2-9p-tempel1-v1.0)'],
        "label": "D",
    },
    "EDR_miro_67p": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-miro-2-', '-67p-', '/data'],
        "label": "D",
    },
    "RDR_miro_prior": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-miro-3-', '/data'],
        "url_regex": [r'(ro-a)|(ear1-earth1-v1.1)|(ear2-earth2-v1.0)|(cvp-commissioning-v1.1)|(cr2-9p-tempel1-v1.1)'],
        "label": "D",
    },
    "RDR_miro_67p": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-miro-3-', '-67p-', '/data'],
        "label": "D",
    },
    # 'level 4 processing' products also listed as RDRs, but different enough to get their own product type
    "RDR_miro_67p_lvl4": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['-miro-4-', '-67p-', '/data'],
        "label": "D",
    },
	
# start ROSINA data products

    "EDR_rosina": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rosina-2-', '/data'],
        "label": "A",
    },
    "RDR_rosina": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-rosina-3-', '/data'],
        "label": "A",
    },
    "DDR_rosina": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.asc'],
        "url_must_contain": ['-rosina-4-', '/data'],
        "label": "D",
    },
    
# start VITRTIS data products

	# Some of these qube products open and may be fully supported, but could use additional testing.
	# TODO: needs support for BIP
    # # raw data
    # "EDR_virtis": {
    #     "manifest": SB_FILE,
    #     "fn_must_contain": ['.qub'],
    #     "url_must_contain": ['-virtis-2-', '/data'],
    #     "label": "A",
    # },

#     # geometry corresponding to RDRs below (these do not open at all)
#     "EDR_virtis_geo": {
#         "manifest": SB_FILE,
#         "fn_must_contain": ['.geo'],
#         "url_must_contain": ['-virtis-3-', '/data'],
#         "label": "A",
#     },
    # TODO: multiple axplanes
    # # calibrated data
    # "RDR_virtis": {
    #     "manifest": SB_FILE,
    #     "fn_must_contain": ['.cal'],
    #     "url_must_contain": ['-virtis-3-', '/data'],
    #     "label": "A",
    # },

    # derived data (maps)
    "DDR_virtis": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-virtis-5-', '/data'],
        "label": "D",
    },
    
}


