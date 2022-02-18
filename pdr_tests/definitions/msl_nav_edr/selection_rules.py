"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .csv file that contains urls, file sizes, etc., scraped directly
from the hosting institution for this product type. for some data sets, all
urls will be found in the same .csv file; for others, they may be split
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
from pathlib import Path

import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .parquet files
IMG_FILE = Path(MANIFEST_DIR, "img_jpl_msl_navcam.parquet")

base = {
    "manifest": IMG_FILE,
    "url_must_contain": ["MSLNAV_0XXX/DATA"],
    "label": "D",
}

# see: MSL Camera SIS, pp. 88+
# ...just explicitly discovered them in this case...
file_information = {}
for ptype_samp in (
    'ECS_N', 'EDR_F', 'EDR_T', 'EHG__', 'ERP_S', 'ERS_N',
    'EDR_D', 'EDR_S', 'EDR_M', 'EID_F', 'EID_T', 'EHG_N'
):
    info = base | {"fn_must_contain": [ptype_samp]}
    file_information[ptype_samp] = info


