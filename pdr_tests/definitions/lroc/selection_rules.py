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
MANIFEST_FILE = "img_lroc"

file_information = {
    "NAC_CDR_if": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r"^M.*\.IMG"],
        "url_must_contain": ["CDR", "NAC"],
        "label": "A",
    },
    "NAC_CDR_rad": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r"^S.*\.IMG"],
        "url_must_contain": ["CDR", "NAC"],
        "label": "A",
    },
    "NAC_CDR_cal": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r"^C.*\.IMG"],
        "url_must_contain": ["CDR", "NAC"],
        "label": "A",
    },
    "NAC_CDR_earth": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r"^E.*\.IMG"],
        "url_must_contain": ["CDR", "NAC"],
        "label": "A",
    },
    "WAC_CDR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": [".IMG"],
        "url_must_contain": ["CDR", "WAC"],
        "label": "A",
    },
    "NAC_EDR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": [".IMG"],
        "url_must_contain": ["EDR", "NAC"],
        "label": "A",
    },
    "WAC_EDR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": [".IMG"],
        "url_must_contain": ["EDR", "WAC"],
        "label": "A",
    },
    "GSFC_PFCAL_EDR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": [".IMG"],
        "url_must_contain": ["EDR", "PFCALIB/GSFC"],
        "label": "A",
    },
    "NAC_DTM": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_DTM", ".TIF"],
        "url_must_contain": ["/DATA/"],
        "label": "D",
    },
    "NAC_DTM_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_DTM", ".IMG"],
        "url_must_contain": ["/DATA/", "NAC_DTM"],
        "label": "A",
    },
    "NAC_PHO": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_PHO", ".IMG"],
        "label": "A",
    },
    "NAC_POLE": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_POLE_P8", ".IMG"],
        "label": "A",
    },
    "NAC_POLE_PSR": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_POLE_PSR", ".IMG"],
        "label": "A",
    },
    "NAC_ROI": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_ROI", ".IMG"],
        "label": "A",
    },
    "NAC_ROI_tif": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_ROI", ".TIF"],
        "url_must_contain": ["/DATA/", "NAC_ROI"],
        "label": "D",
    },
    "WAC_CSHADE": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_CSHADE", ".IMG"],
        "label": "A",
    },
    "WAC_EMP": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_EMP", ".IMG"],
        "label": "A",
    },
    "WAC_EMP_tl": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_EMP", ".TIF"],
        "url_must_contain": ["/DATA/"],
        "label": "D",
    },
    "WAC_HAPKE": {
        "manifest": MANIFEST_FILE,
        "url_must_contain": ["MDR/WAC_HAPKE"], 
        "fn_must_contain": [".IMG", "WAC_HAPKE_"],
        "label": "A",
    },
    "WAC_HAPKE_tl": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_HAPKE", ".TIF"],
        "url_must_contain": ["/DATA/"],
        "label": "D",
    },
    "WAC_HAPKE_PARAMMAP": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_HAPKEPARAMMAP", ".IMG"],
        "label": "A",
    },
    "WAC_GLD100": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_GLD100", ".IMG"],
        "label": "A",
    },
    "WAC_GLOBAL": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_GLOBAL", ".IMG"],
        "label": "A",
    },
    "WAC_MOVIE": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_MOVIE", ".IMG"],
        "label": "A",
    },
    "WAC_ORBITS": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_ORBITS", ".IMG"],
        "label": "A",
    },
    "WAC_POLE_ILL": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_POLE_ILL", ".IMG"],
        "label": "A",
    },
    "WAC_ROI": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_ROI", ".IMG"],
        "label": "A",
    },
    "WAC_TIO2": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["WAC_TIO2", ".IMG"],
        "label": "A",
    },
    "ANAGLYPH": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["ANAGLYPH", ".TIF"],
        "label": "D",
    },
    "AMES_DTM": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["DTM", ".TAB"],
        "url_must_contain": ["/EXTRAS/AMES_DTM"],
         "label": "D",
    },
    # NAC_DTM_extras and NAC_DTM_thumb are flagged "ix_skip" because they are 
    # supported but are imcompatible with ix because of missing or incomplete 
    # PDS labels.
    "NAC_DTM_extras": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_DTM", ".TIF"],
        "url_must_contain": ["/EXTRAS/AMES_DTM/LRONAC_DTMS"],
        "label": "D",
        "ix_skip": True, # incomplete PDS3 labels
    },
    "NAC_DTM_thumb": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ["NAC_DTM", "Thumbnail", ".TIF"],
        "url_must_contain": ["/EXTRAS/AMES_DTM/LRONAC_THUMBNAILS"],
        "label": "NA",
        "ix_skip": True, # no PDS labels
    },
    "SHAPEFILE": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r"((dbf)|(prj)|(shp)|(shx)|(DBF)|(PRJ)|(SHP)|"
                     r"(SHX)|(ZIP)|(CSV)|(XML))$"],
        "url_must_contain": ["/EXTRAS/", "SHAPEFILE"],
        "label": "NA",
        "support_np": True, # not all files have PDS labels
    },
    # .csv products (lowercase filename extensions) in the EXTRAS/SHAPEFILE 
    # directory are PDS4. It looks like they were added after our last update 
    # to the img_lroc manifest.
    # .XML files (uppercase filename extensions) are not PDS4 labels; some of 
    # the .xml files are labels, some are not
}
