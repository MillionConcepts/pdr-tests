"""
This is a dictionary of information about each product type.
the keys of the dictionary are the names of each product type. This will
translate into local file and/or directory names for various outputs of
pdr-tests: index files, data downloads, etc.

These selection rules are ideally for the _largest individual file_ of each
product (which in some cases will be the only file; lucky you, if so).

manifest: the .parquet file that contains urls, file sizes, etc., scraped
directly from the hosting institution for this product type. for some data
sets, all urls will be found in the same .parquet file; for others, they may
be split between nodes or scraping sessions.

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
PSA = "img_esa_ve"

file_information = {
    # SPICAV SOIR

    # level 2 RDRs
    "LVL2_RDR_OBS": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', 'OBS'],
        "url_must_contain": ['SPICAV-SOIR', 'SPICAV-2-SOIR'],
        "label": "D",
    },
    "LVL2_RDR_TC1": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', 'TC1'],
        "url_must_contain": ['SPICAV-SOIR', 'SPICAV-2-SOIR'],
        "label": "D",
    },
    "LVL2_RDR_TC2": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', 'TC2'],
        "url_must_contain": ['SPICAV-SOIR', 'SPICAV-2-SOIR'],
        "label": "D",
    },
    # level 3 RDRs
    "LVL3_REFTABLE": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_R1'],
        "url_must_contain": ['SPICAV-SOIR', 'SPICAV-3-SOIR'],
        "label": "D",
    },
    "LVL3_SOIRTABLE": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_1'],
        "url_must_contain": ['SPICAV-SOIR', 'SPICAV-3-SOIR'],
        "label": "D",
    },
    # level 3 RDRs
    "LVL3_TRT": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_TRT'],
        "url_must_contain": ['SPICAV-SOIR', 'SPICAV-3-SOIR'],
        "label": "D",
    },
    # level 3 RDRs
    "LVL3_TC2": {
        "manifest": PSA,
        "fn_must_contain": ['.TAB', '_TC2'],
        "url_must_contain": ['SPICAV-SOIR', 'SPICAV-3-SOIR'],
        "label": "D",
    },
}


