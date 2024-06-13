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
GEO_FILE = "geomex"

file_information = {
    # RDR - Super-Resolution Camera images
    "rdr_src": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['_sr', '.img'],
        "url_must_contain": ['mex-m-hrsc-3-rdr','data'],
        "label": "A",
    },
    # RDR - High Resolution Stereo Camera images
    # Currently unsupported; their line prefixes throw a "not yet supported"
    # error/warning.
#    "rdr_hrsc": {
#        "manifest": GEO_FILE,
#        "fn_must_contain": ['.img'],
#        "fn_regex": [r'(_nd)|(_s[12])|(_p[12])|(_bl)|(_gr)|(_ir)|(_re)'],
#        "url_must_contain": ['mex-m-hrsc-3-rdr','data'],
#        "label": "A",
#    },
    # REFDR - Map-Projected Image Data, v4
    "projected_v4": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mex-m-hrsc-4-refdr-mapproject','data', '-v4/'],
        "label": "A",
    },
    # REFDR - Map-Projected Image Data, v3
    # This dataset has been superseded by version 4, but I could only find
    # version 3 of products from the norminal mission phase.
    "projected_v3": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mex-m-hrsc-5-refdr-mapprojected','data', '-v3/'],
        "label": "A",
    },
    # REFDR - HRSC Orthophoto and DTM data
    "dtm": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mex-m-hrsc-5-refdr-dtm','data'],
        "label": "A",
    },
    # REFDR - Phobos images, DTM data, and mosaics
    "phobos_dtm": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mex-msa-hrsc-5-refdr-phobos-maps','data/dtm'],
        "label": "A",
    },
    "phobos_image": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mex-msa-hrsc-5-refdr-phobos-maps','data/image'],
        "label": "A",
    },
    "phobos_mosaic": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mex-msa-hrsc-5-refdr-phobos-maps','data/mosaic'],
        "label": "A",
    },
    
    # There is a DDR clouds dataset (MEX-M-HRSC-4-DDR-CLOUDS-V1.0) at PSA that
    # is not mirrored at GEO. It only has 1 ascii table product, which opens
    # correctly and is listed as notionally supported in supported_datasets.md
}

SKIP_FILES = ["MEX_ORIENTATION_DESC.TXT", "MEX_POINTING_DESC.TXT",
              "VICAR2.TXT", "DSMAP.CAT"]
