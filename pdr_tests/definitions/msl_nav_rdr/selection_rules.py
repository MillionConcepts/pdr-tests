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
IMG_FILE = "img_jpl_msl_navcam"

base = {
    "manifest": IMG_FILE,
    # note: "DATA_V1" is not an older version, but data from
    # the first 2000 sols -- make sure not to filter it out
    "url_must_contain": ["MSLNAV_1XXX/DATA"],
    "label": "D",
}


ptypes = (
 'ARM', 'ARP', 'DFF', 'DSP', 'DSR', 'ILT', 'MDS',
 'MXY', 'RAD', 'RAS', 'RNE', 'RNG', 'RNR', 'RUD',
 'RUT', 'SHD', 'SLP', 'SMG', 'SNT', 'SRD', 'UVS', 'UVW',
 'XYE', 'XYM', 'XYR', 'XYZ'
)
samps = ("D", "F", "S", "T")

# see: MSL Camera SIS, pp. 88+
file_information = {"ANAGLYPH": base | {"fn_regex": [r"NA.*"]}}
for ptype, samp in product(ptypes, samps):
    info = base | {"fn_regex": [rf"N[LR].*{ptype}(\w|_){samp}"]}
    file_information[f"{ptype}_{samp}"] = info

# range maps persistently reference first, don't know where it is;
# others are irrelevant
SKIP_FILES = ["MIPL_ERROR_METHODS.TXT", "VICAR2.TXT", "ODL.TXT"]


# identified as bad in testing (apparently a write underrun):
# NRA_404684268DFF_F0050104NCAM00107M1.IMG

# scaling behavior is a little inconsistent within some of the engineering
# maps because of label inconsistencies -- ARP maps for instance
# sometimes list 0 as a missing/invalid constant and sometimes, not
# but are almost always valued _only_ 0 and some other number --
# how to handle situations like this is unclear at the moment

