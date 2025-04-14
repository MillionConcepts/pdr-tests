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
GEO_FILE = "geoviking"

file_information = {
    # Lander image EDRs; mirrored at GEO and IMG
    "lcs_edr": {
        "manifest": GEO_FILE,
        "fn_regex": [r'^[12].[a-j][0-9]{3}'],
        "url_must_contain": ['vl1_vl2-m-lcs-2-edr-v1'],
        "url_regex": [r'vl_000[12]/..xx'],
        "label": "A",
    },
    # Lander rock dataset
    "lcs_rock": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vl1_vl2-m-lcs-5-rocks-v1/vl_9001/data'],
        "label": "D",
    },
    # Lander labeled release experiment
    "lr_edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vl1_vl2-m-lr-2-edr-v1/vl_9010/data'],
        "label": "D",
    },
    # Lander 2 seismology experiment
    "seis_raw": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['vl2-m-seis-5-rdr-v1/vl_9020/data'],
        "label": "D",
    },
    "seis_summary": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['vl2-m-seis-5-rdr-v1/vl_9020/data'],
        "label": "D",
    },

    # # IRTM - 1989 version
    # # Unsupported: the pointers are in an old format (easy special case), the
    # # tables use VAX_INTEGER (probably not the issue) and VAX_BIT_STRING (more
    # # likely a problem) data types, AND the tables are in a messy "partially
    # # transposed" format (likely part of the problem)
    # "irtm_89": {
    #     "manifest": GEO_FILE,
    #     "fn_must_contain": ['.DAT'],
    #     "url_must_contain": ['vo1_vo2-m-irtm-4-v1/old_vo_0001', 'DATA'],
    #     "label": "D",
    # },

    # Support not planned (incomplete labels)
    # IRTM - 1994 version "intended to be compatible with the TES data format"
    "irtm_94": {
        "manifest": GEO_FILE,
        "fn_regex": [r'\.[0-9]{3}$'],
        "url_regex": ['vo1_vo2-m-irtm-4-v1/vo_000[12]/VO[12]_DATA'],
        "label": "A",
        "support_np": True
    },
    # Support not planned (webpages, not PDS products)
    "lr_edr_extras": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.htm'],
        "url_must_contain": ['vl1_vl2-m-lr-2-edr-v1/vl_9010/extras'],
        "label": "NA",
        "support_np": True
    },
}

r"""
Viking Lander
PDS4:
- FTS (vl_1002)
- MET (vl_1001)
Safed:
- LCS MIDRs and special products

Viking Orbiter
PDS4:
- VIS-EDR images
- DIM/DTM
- MAWD (vo_3001)
- IRTM binned/derived data (vo_3002)
- radio occultation electron density profiles
Safed:
- Viking Orbiter and Mariner 9 Occultation, Gravity and Topography Data
Included in other selection rules:
- RSS LOS gravity data (part of GEO's pre-magellan collection)
- Viking Orbiter and Mariner 9 cloud catalog (tested with Mariner)
    
"""
