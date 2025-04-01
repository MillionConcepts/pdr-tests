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
MANIFEST_FILE = "geomgs"
IMG_FILE = "img_usgs_mars_global_surveyor"

file_information = {
    # precision EDRs; have non-standard labels but they open with special cases
    "pedr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.b'],
        "url_must_contain": ['-mola-', '-pedr-'],
        "label": "A",
    },
    # precision RDRs; well-labeled fixed-length tables
    "prdr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-mola-', '-prdr-'],
        "url_regex": [r'(/mapping/)|(/passive/)'],
        "label": "D",
    },
    # topographic maps of mars (tables); well-labeled fixed-length tables
    "iegdr_v1": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['-mola-', '-iegdr-', '-v1/'],
        "label": "D",
    },
    # topographic maps of mars (images); well-labeled 2-dimensional arrays
    "iegdr_v2": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-mola-', '-iegdr-', '-v2/'],
        "label": "D",
    },
    # gridded images; Mars global topography maps; well-labeled 2-dimensional arrays
    "megdr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['-mola-', '-megdr-'],
        "label": "D",
    },
    # ENVI headers for MEGDR images
    "megdr_envi": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.hdr'],
        "url_must_contain": ['-mola-', '-megdr-', 'extras'],
        "support_np": True
    },
    # topography model; well-labeled header and coefficient tables
    "shadr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.sha'],
        "url_must_contain": ['-mola-', '-shadr-'],
        "label": "D",
    },
    
    # ascii PEDR products in the "science sampler" dataset at IMG node
    "pedr_ascii": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mgs_0001/mola/pedr_asc'],
        "label": "D",
    },
}

"""

    # known unsupported; files are not in an archive compliant format
    "aedr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.b'],
        "url_must_contain": ['-mola-', '-aedr-'],
        "label": "A",
    },

Needed for aedr support:
- figure out which format file to apply 
    - there are 2 described in the labels, but the data only calls for one depending on a flag at byte 11 of the file
    - seems like the whole table is either one format or the other
    - unlike the pedr tables which change format from row to row
- would need to extend the mgs.mola_pedr_special_block() hook to include aedr products
"""
