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
from itertools import product

# variables naming specific parquet files in node_manifests
IMG_FILE = "img_jpl_mer_pan"

base = {
    "manifest": IMG_FILE,
    "url_must_contain": ['mer','po_0xxx/data', 'rdr'],
    "label": "A",
}

file_information = {
    # inverse LUT
    "ilut": base | {
        "fn_regex": [r"\w[0-9]{9}((ilf)|(isf)|(inn)|(ffl)|(sfl)|(dnl)).*img$"]},
    "ilut_thumb": base | {
        "fn_regex": [r"\w[0-9]{9}((ith)|(thn)).*img$"]},
    "filename_typo": base | {
        "fn_regex": [r"im$"]},
}

ptypes = ("mr", # radiometric; specifically the MIPLRAD correction
          "rs", # radiometric; also MIPLRAD but not mentioned in the camera SIS
          "di", # disparity
          "xy", # XYZ
          "rn", # range
          "uv", # UVW (XYZ) surface normal
          "ru", # surface roughness
          "sl", # slope
          "sr", # slope rover direction
          "sh", # slope heading
          "sm", # slope magnitude
          "se", # solar energy product
          "id", # IDD reachability
          "sn", # slope northerly tilt
          "us", # slope normal
          )
# Product types in the MER Camera SIS that I couldn't find, most are variations
# or components of the ptypes above:
# radiometric: "ra", "rf", "io", "if", "cc", "cf"
# disparity: "ds", "dl"
# XYZ: "ms", "xx", "yy", "zz", "dem"
# surface normal: "uu", "vv", "ww"
# terrain: "vi", "as"
image_size = ("[tn]", "[a-mo-su-z]") # thumnails vs. larger images

# products without thumbnail versions archived
no_thumbnail = ["ru", "id", "us"]

for ptype, size in product(ptypes, image_size):
    if ptype in no_thumbnail and size == "[tn]":
        # did not find thumbnails of these products
        continue
    pattern = rf"\w[0-9]{{9}}{ptype}{size}.*img$"
    info = base | {"fn_regex": [pattern]}
    if size == "[tn]":
        file_information[f"{ptype}_thumb"] = info
    else:
        file_information[f"{ptype}"] = info

# irrelevant
SKIP_FILES = ["VICAR2.TXT", "GEOMETRIC_CM.TXT"]
