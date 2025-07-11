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

# variables naming specific parquet files in node_manifests
GEO_FILE = "geompf"
IMG_FILE = "img_usgs_mars-pathfinder"


file_information = {
    # Stereo 3D position data
    "3d_pos": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mpfl-m-imp-5-3dposition-v1/mpim_2xxx/data'],
        "label": "A",
    },
    # Radio science - ODF
    "rss_odf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.odf'],
        "url_must_contain": ['mpf-m-rss-1-5-radiotrack-v1', 'odf'],
        "label": "D",
    },
    # Radio science - TDF
    "rss_tdf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tdf'],
        "url_must_contain": ['mpf-m-rss-1-5-radiotrack-v1', 'tdf'],
        "label": "D",
    },
    # Radio science - reduced range and doppler data
    "rss_reduced": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mpf-m-rss-1-5-radiotrack-v1', 'reduced'],
        "label": "D",
    },
    # Radio science - estimated rotation angles and positions
    "rss_results": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mpf-m-rss-1-5-radiotrack-v1', 'results'],
        "label": "D",
    },
    # Imager EDRS
    "imp_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mpim_000', '/seq'],
        "label": "A",
    },
    "imp_cal": {
        "manifest": IMG_FILE,
        "fn_regex": [r'((drk)|(nul)|(str)$)'],
        "url_must_contain": ['mpim_000', 'calimg', '/seq'],
        "label": "A",
    },
    # Rover Camera EDRs
    "rvrcam_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mprv_0001/rvr_edr'],
        "label": "A",
    },
    # Rover Camera derived mosaics - .img format
    "rvrcam_midr_img": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mprv_0001/rvr_midr'],
        "label": "A",
    },
    # Rover Camera derived mosaics - .haf format
    "rvrcam_midr_haf": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.haf'],
        "url_must_contain": ['mprv_0001/rvr_midr'],
        "label": "A",
    },
    # APXS raw spectra
    "apxs_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mprv_0001/apxs_edr'],
        "label": "A",
    },
    # APXS derived abundances
    "apxs_ddr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mprv_0001/apxs_ddr'],
        "label": "D",
    },
    
    # Note: these are in a compressed (.zip) format at the IMG node
    # raw engineering data
    "eng_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['dn.zip'],
        "url_must_contain": ['mprv_0001/rvr_eng'],
        "label": "D",
    },
    # calibrated engineering data
    "eng_rdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['eu.zip'],
        "url_must_contain": ['mprv_0001/rvr_eng'],
        "label": "D",
    },
    
    # # Ancillary table of informal rock/feature names
    # # Not supported - one row includes a letter with an accent that throws an 
    # # error when opened through _interpret_as_ascii() and pd.read_csv(). 
    # # Could add a special case; low priority
    # "gazetter": {
    #     "manifest": IMG_FILE,
    #     "fn_must_contain": ['.tab'],
    #     "url_must_contain": ['mpim_000', 'gazetter'],
    #     "label": "D",
    # },
    
    # Support not planned
    # Supplementary files without labels; compressed with gzip
    "3d_unsupported": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.wrz'],
        "url_must_contain": ['mpfl-m-imp-5-3dposition-v1/mpim_2xxx/extras'],
        "label": "A",
        "support_np": True
    },
}

