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
SBN_FILE = "tiny_other"

file_information = {
    # ION PROPULSION SYSTEM DIAGNOSTIC SUBSYSTEM (IDS)
    # RDRs
    "ids_rdr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ds1-c-ids-3-rdr-borrelly-v1.0/data'],
        "label": "D",
    },
    # MINIATURE INTEGRATED CAMERA-SPECTROMETER (MICAS)
    # DLR and USGS DEMs
    "micas_dem": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['dem.tab'],
        "url_must_contain": ['ds1-c-micas-5-borrelly-dem-v1.0/data'],
        "label": "D",
    },
    # images used for DEM
    "micas_img": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ds1-c-micas-5-borrelly-dem-v1.0/data/images'],
        "label": "D",
    },
    # scale/matrix values used for USGS DEM
    "micas_mat": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ds1-c-micas-5-borrelly-dem-v1.0/data/matrices'],
        "label": "D",
    },

    # Safed Datasets:
    # DS1-C-MICAS-2-EDR-VISCCD-BORRELLY-V1.0
    "micas_edr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ds1-c-micas-2-edr-visccd-borrelly-v1.0/data'],
        "label": "D",
    },
    # DS1-C-MICAS-3-RDR-VISCCD-BORRELLY-V1.0
    "micas_rdr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.cub'],
        "url_must_contain": ['ds1-c-micas-3-rdr-visccd-borrelly-v1.0/document/derived'],
        "label": "A",
    },
    # DS1-C-PEPE-2-EDR-BORRELLY-V1.0
    "pepe_tab": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ds1-c-pepe-2-edr-borrelly-v1.0/data'],
        "label": "D",
    },
    "pepe_dat": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "fn_regex": [r'(elc)|(ion)|(log)|(mq)|(tof)'],
        "url_must_contain": ['ds1-c-pepe-2-edr-borrelly-v1.0/data'],
        "label": "D",
    },

    # Support not planned:
    # PEPE EDR - safed binary housekeeping files
    "pepe_dat_unsupported": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['hsk', '.dat'],
        "url_must_contain": ['ds1-c-pepe-2-edr-borrelly-v1.0/data'],
        "label": "D",
        "support_np": True
    },
}
