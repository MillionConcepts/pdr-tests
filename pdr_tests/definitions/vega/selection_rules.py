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
ATM_FILE = Path(MANIFEST_DIR, "atm.parquet")
PPI_FILE = Path(MANIFEST_DIR, "plasm_full.parquet")
SBN_FILE = Path(MANIFEST_DIR, "tiny.parquet")


file_information = {
    # balloon and lander data; Vega 1 & 2
    "balloon": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['vega_5001/data'],
        "label": "D",
    },
    # PLASMAG-1 experiment; Vega 1 & 2
    "pm1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VEGA','-C-PM1-2-RDR-HALLEY-V1.0/DATA'],
        "label": "D",
    },
    # energetic particle analyzer; Vega 1
    "tnm": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VEGA1-C-TNM-2-RDR-HALLEY-V1.0/DATA'],
        "label": "D",
    },
    # fluxgate magnetometer; Vega 1
    # MISCHA "original" dataset is safed, "halley" and "cruise" are archived
    "mischa": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.'],
        "url_must_contain": ['VEGA1-C-MISCHA-3-RDR-', 'DATA'],
        "url_regex": [r'(HALLEY)|(CRUISE)'],
        "label": "D",
    },
    # Television System raw, processed, and transform data
    "tvs_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['vega','-c-tvs-2-rdr-halley-v1.0/data'],
        "label": "D",
    },
    "tvs_proc": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['vega','-c-tvs-3-rdr-halley-processed-v1.0/data'],
        "label": "D",
    },
    "tvs_tran": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['vega2-c-tvs-5-rdr-halley-transform-v1.0/data'],
        "label": "D",
    },
    # infrared spectrometer raw and processed data; Vega 1
    "iks_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vega1-c-iks-2-rdr-halley-v1.0/data'],
        "label": "D",
    },
    "iks_proc": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vega1-c-iks-3-rdr-halley-processed-v1.0/data'],
        "label": "D",
    },
    # dust-particle counter and mass analyzer; Vega 1 and 2
    "ducma": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vega','-c-ducma-3-rdr-halley-v1.0/data'],
        "label": "D",
    },
    # dust-particle impact detector 1 - electrode collector; Vega 1 & 2
    "sp1": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vega','-c-sp1-2-rdr-halley-v1.0/data'],
        "label": "D",
    },
    # dust-particle impact detector 2 - acoustic sensor; Vega 1 & 2
    "sp2": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vega','-c-sp2-2-rdr-halley-v1.0/data'],
        "label": "D",
    },
    # stooke shape models
    "shape": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['EAR_A_5_DDR_STOOKE_SHAPE_MODELS_V2_0/data'],
        "label": "D",
    },
    
    # dust impact mass analyzer
    # Unsupported; UserWarning: Unable to load ARRAY: 'DATA_TYPE'
    # The labels define a format with nested ARRAYs and COLLECTIONs.
##    "puma_mode": {
##        "manifest": SBN_FILE,
##        "fn_must_contain": ['.dat'],
##        "url_must_contain": ['vega','-c-puma-','-rdr-halley-','/data/mode'],
##        "label": "D",
##    },
    # Unsupported; missing PDS label files
##    "puma_raw": {
##        "manifest": SBN_FILE,
##        "fn_must_contain": ['piki','.dat'],
##        "url_must_contain": ['vega','-c-puma-2-rdr-halley-v1.0/data'],
##        "label": "D",
##    },
    # Unsupported; missing PDS label files
##    "puma_processed": {
##        "manifest": SBN_FILE,
##        "fn_must_contain": ['pmpi','.tbl'],
##        "url_must_contain": ['vega','-c-puma-3-rdr-halley-processed-v1.0/data'],
##        "label": "D",
##    },
}

