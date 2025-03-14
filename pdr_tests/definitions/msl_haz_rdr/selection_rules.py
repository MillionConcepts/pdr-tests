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
import re
from itertools import product
# variables naming specific parquet files in node_manifests
IMG_FILE = "img_jpl_msl_hazcam"

base = {
    "manifest": IMG_FILE,
    "url_must_contain": ["MSLHAZ_1XXX/DATA"],
    "label": "D",
}

# range maps persistently reference first, don't know where it is;
# others are irrelevant
SKIP_FILES = ["MIPL_ERROR_METHODS.TXT", "VICAR2.TXT", "ODL.TXT", 
              "GEOMETRIC_CM.TXT"]

# see: MSL Camera SIS, pp. 88+
file_information = {
    "ANAGLYPH": base | {"fn_regex": [r"^[FR]A[AB].*\.IMG"]},

    # unique products "generated using off nominal processing"
    "special": {
        "manifest": IMG_FILE,
        "fn_must_contain": [".IMG"],
        "url_must_contain": ["MSLHAZ_1XXX/EXTRAS/SPECIAL_PROCESSING"],
        "label": "D",
    },
}
for ptype, samp in product(
    ("XYZ", r"RA\w", r"D\w\w", r"RN\w", r"UV\w", r"RU\w", r"S[LRHMN]\w", r"AR\w", r"ILT", r"M\w\w", r"XY[EMR]"),
    ("F", "S", "D", "T")
):
    pattern = rf"^[FR][RL].*{ptype}(_|\w){samp}.*\.IMG"
    info = base | {"fn_regex": [pattern]}
    ptype_name = re.sub(r"(\\w|\[|])", "", ptype)
    file_information[
        f"{ptype_name}_{samp}"
    ] = info

