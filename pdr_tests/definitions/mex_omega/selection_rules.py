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
    # DDR global maps
    "ddr_maps": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['mex-m-omega-5-ddr-global-maps', 'data'],
        "label": "D",
    },
    # DDR hydrous sites
    "ddr_hydrous": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['mex-m-omega-5-ddr-global-maps', 'data'],
        "label": "D",
    },
    
    # The MEX-M-OMEGA-4-DDR-PROF-V1.0 dataset is archived at PSA but not GEO.
    # The products are ascii tables. They are notionally supported.

    # Products in the DDR extras directory (none have PDS labels)
    # The .tif and .png images are supported; the rest are 'support not planned'
    "extras": {
        "manifest": GEO_FILE,
        "fn_regex": [r'(cub)|(kml)|(dbf)|(shp)|(shx)$'],
        "url_must_contain": ['mex-m-omega-5-ddr-global-maps', '/extras'],
        "support_np": True
    },
}

"""
Unsupported product types:
    # EDR data cubes
    # Error message: "UserWarning: This product's QUBE is not yet supported:
    # ISIS-style axplanes along multiple axes are not supported."
    # From the label: "ISIS cube with non-standard sideplanes"
    "edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.qub'],
        "url_must_contain": ['mex-m-omega-2-edr-flight', 'data'],
        "label": "A",
    },
    # EDR geometry cubes
    # Example error message: "UserWarning: Unable to load QUBE: cannot reshape
    # array of size 1632000 into shape (4000,51,16)"
    "geom": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.nav'],
        "url_must_contain": ['mex-m-omega-2-edr-flight', 'data'],
        "label": "A",
    },
"""
SKIP_FILES = ["OMEGA_CALIBRATION_DESC.TXT", "OMEGA_HK.TXT", "OMEGA_DESC.TXT",
              "OMEGA_DATA_QUALITY_DESC.TXT", "GEOCUBE_DESC.TXT", "DSMAP.CAT",
              "MEX_ORIENTATION_DESC.TXT", "ODY_JGR2012_EDR_DESC.TXT"]
