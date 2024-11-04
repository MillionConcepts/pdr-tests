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
THEMIS_FILE = "img_asu_themis_tes_coverage"

file_information = {
    # brightness temperature derived from ir_RDR; well-labeled two-dimensional
    # raster images
    "BTR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtib'],
        "label": "A",
    },
    # apparent brightness derived from vis_RDR; well-labeled two-dimensional
    # raster images
    "ABR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtvb'],
        "label": "A",
    },
    # projected brightness temperature derived from ir_GEO; well-labeled
    # two-dimensional raster images; version 1
    "PBT_v1": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTGEO_v1/', 'odtip'],
        "label": "A",
    },
    # projected brightness temperature derived from ir_GEO; well-labeled
    # two-dimensional raster images; version 2
    "PBT_v2": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTGEO_v2/', 'odtip'],
        "label": "A",
    },
    # projected albedo derived from vis_GEO; well-labeled two-dimensional
    # raster images
    "ALB_v2": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['/ODTGEO_v2/', 'odtva'],
        "label": "A",
    },
    # geographically projected products derived from ir_RDR;
    # three-dimensional spectral image CUBEs; version 2
    "ir_GEO_v2": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.CUB.gz'],
        "url_must_contain": ['/ODTGEO_v2/', 'odtig'],
        "label": (".CUB.gz", ".LBL"),
    },
    # geographically projected products derived from vis_RDR;
    # three-dimensional spectral image CUBEs; version 2
    "vis_GEO_v2": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.CUB'],
        "url_must_contain": ['/ODTGEO_v2/', 'odtvg'],
        "label": "D",
    },
    "ir_EDR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.QUB'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtie'],
        "label": "A",
    },

    # raw visible data; three-dimensional spectral image QUBEs
    "vis_EDR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.QUB'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtve'],
        "label": "A",
    },
    # calibrated visible data; three-dimensional spectral image QUBEs
    "vis_RDR": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.QUB'],
        "url_must_contain": ['/ODTSDP_v1/', 'odtvr'],
        "label": "A",
    },

    # Support not planned:
    # note that _v1 geoprojected products are, per data providers, not really 
    # science products -- they contain cosmetic processing

    # geographically projected products derived from ir_RDR; three-dimensional 
    # spectral image CUBEs; version 1
    "ir_GEO_v1": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.CUB.gz'],
        "url_must_contain": ['/ODTGEO_v1/', 'odtig'],
        "label": "D",
        "support_np": True
    },
    # geographically projected products derived from vis_RDR; three-dimensional 
    # spectral image CUBEs; version 1
    "vis_GEO_v1": {
        "manifest": THEMIS_FILE,
        "fn_must_contain": ['.CUB'],
        "url_must_contain": ['/ODTGEO_v1/', 'odtvg'],
        "label": "D",
        "support_np": True
    },
}

"""
# following ptypes are currently (and maybe permanently) not supported due to 
# ISIS axplanes along multiple axes

# calibrated infrared data; three-dimensional spectral image QUBEs
"ir_RDR": {
    "manifest": THEMIS_FILE,
    "fn_must_contain": ['.QUB'],
    "url_must_contain": ['/ODTSDP_v1/', 'odtir'],
    "label": "A",
},
"""
