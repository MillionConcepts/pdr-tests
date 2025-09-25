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
GEO_FILE = "geomsl"

# NOTE: commented-out RDR types are specified in the SIS as valid product
# categories, but no examples of them are actually present in the online
# archive.

file_information = {
    # "DIFFRACTION_SINGLE_RDR": {
    #     "manifest": GEO_FILE,
    #     "fn_regex": [r"cm.*rd1.*"],
    #     "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
    #     "label": "D",
    # },
    # "DIFFRACTION_SPLIT_RDR": {
    #     "manifest": GEO_FILE,
    #     "fn_regex": [r"cm.*rds.*"],
    #     "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
    #     "label": "D",
    # },
    "DIFFRACTION_ALL_RDR": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*rda.*\.csv"],
        "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
        "label": "D",
    },
    # "DIFFRACTION_ALL_RAW_RDR": {
    #     "manifest": GEO_FILE,
    #     "fn_regex": [r"cm.*rtr.*"],
    #     "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
    #     "label": "D"
    # },
    # "DIFFRACTION_FILM_RDR": {
    #     "manifest": GEO_FILE,
    #     "fn_regex": [r"cm.*rdf.*"],
    #     "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
    #     "label": "D"
    # },
    # "ENERGY_ALL_RDR": {
    #     "manifest": GEO_FILE,
    #     "fn_regex": [r"cm.*rea.*"],
    #     "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
    #     "label": "D",
    # },
    "ENERGY_SINGLE_RDR": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*re1.*\.csv"],
        "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
        "label": "D",
    },
    # "ENERGY_SPLIT_RDR": {
    #     "manifest": GEO_FILE,
    #     "fn_regex": [r"cm.*res.*"],
    #     "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
    #     "label": "D",
    # },
    "MINERAL_TABLES": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*min.*\.csv"],
        "url_must_contain": ["msl-m-chemin-4-rdr-v1"],
        "label": "D",
    },
    "CCD_FRAME": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ecc.*\.img"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "DIFFRACTION_SINGLE": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ed1.*\.img"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "DIFFRACTION_SPLIT": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*eds.*\.img"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "DIFFRACTION_ALL": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*eda.*\.img"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "ENERGY_ALL": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*eea.*\.dat"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "ENERGY_SINGLE": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ee1.*\.dat"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "ENERGY_SPLIT": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ees.*\.dat"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    # Notionally supported: they open VERY slowly (table is all bit columns)
    # Flagging them as "ix_skip" because of how slow they open.
    "FILM": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*efm.*\.dat"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
        "ix_skip": True,
    },
    "HOUSEKEEPING": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*ehk.*\.dat"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D",
    },
    "TRANSMIT_RAW": {
        "manifest": GEO_FILE,
        "fn_regex": [r"cm.*etr.*\.dat"],
        "url_must_contain": ["msl-m-chemin-2-edr-v1"],
        "label": "D"
    }
}
