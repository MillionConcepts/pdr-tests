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
# modified the last manifest file to remove files on an outdated path, .old
# so this DAT_FILE may have to be renamed to work again
DAT_FILE = "img_jpl_msl_mahli"

base = {
    "manifest": DAT_FILE,
    "url_must_contain": ["/EDR/"],
    "label": "D",
}

# see table below
ptypes = ('B', 'J', 'E', 'G', 'I', 'Q', 'M', 'R', 'T', 'S', 'C', 'H', 'A', 'U', 'O', 'P', 'N', 'D', 'K', 'F')

file_information = {}
for ptype in ptypes:
    # caution: f-string + regex overload curly braces, and f-string wins
    info = base | {"fn_regex": ["^.{22}" + ptype + r".*\.DAT"]}
    file_information[ptype] = info

"""
product type codes (not all exist in RDR archive)
see MMM Camera SIS (pp. 23-24)

A Raster 16 bit image
B Raster 8 bit image
C Losslessly compressed raster 8 bit image
D JPEG grayscale image
E JPEG 422 image
F JPEG 444 image
G Raster 8 bit thumbnail
H JPEG grayscale thumbnail
I JPEG 444 thumbnail
J Raster 8 bit video
K Losslessly compressed raster 8 bit video
L JPEG grayscale video
M JPEG 422 video
N JPEG 444 video
O Raster 8 bit video thumbnail
P JPEG grayscale video thumbnail
Q JPEG 444 video thumbnail
R JPEG 444 focus merge image
S JPEG grayscale range map image
T JPEG 444 focus merge thumbnail
U JPEG grayscale range map thumbnail
"""
