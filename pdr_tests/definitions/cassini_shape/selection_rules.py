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
SB_FILE = "tiny"


file_information = {

	# Dione
    "dione": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['CO_SA_ISSNA_ISSWA_5_DIONESHAPE', 'data'],
        "label": "D",
    },
    # Mimas
    "mimas": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['CO_SA_ISSNA_5_MIMASSHAPE_V2', 'data'],
        "label": "D",
    },
    # Phoebe
    "phoebe": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['CO_SA_ISSNA_5_PHOEBESHAPE_V2', 'data'],
        "label": "D",
    },
    # Tethys
    "tethys": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['CO_SA_ISSNA_5_TETHYSSHAPE', 'data'],
        "label": "D",
    },
    # Saturn Small Moon/Satellite (PDS4 labels only)
    "satellite": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['cassini/saturn_satellite_shape_models', 'data'],
        "label": ('.tab', '.xml'),
    },
    
}
