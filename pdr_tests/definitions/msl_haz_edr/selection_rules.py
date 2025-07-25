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
IMG_FILE = "img_jpl_msl_hazcam"

# NOTE: commented-out RDR types are specified in the SIS as valid product
# categories, but no examples of them are actually present in the online
# archive.

base = {
        "manifest": IMG_FILE,
        "url_must_contain": ["MSLHAZ_0XXX/DATA"],
        "label": "D",
    }

# see: MSL Camera SIS, pp. 88+
file_information = {
    "extras": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['DATA'],
        "url_must_contain": ['MSLHAZ_0XXX/EXTRAS'],
        "label": "A", # no PDS labels
        "support_np": True
    },
}
for ptype, samp in product(
    ("EDR", "ERP"),
    ("F", "S", "D", "T")
):
    if (ptype == "ERP") and (samp != "S"):
        continue
    # underscore between ptype and samp because these are never linearized (I think)
    pattern = fr"[FR][LR].*{ptype}_{samp}.*\.IMG"
    info = base | {"fn_regex": [pattern]}
    file_information[
        f"{ptype}_{samp}"
    ] = info

# irrelevant
SKIP_FILES = ["VICAR2.TXT", "ODL.TXT"]
