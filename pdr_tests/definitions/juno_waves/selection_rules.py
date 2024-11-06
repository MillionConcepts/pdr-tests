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
PLASM_FILE = "plasm_full"

# not including EDR as declared out of scope due to prose description of format

file_information = {
    "CDR_BURST": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO', "CDR", 'WAVES_BURST'],
        "label": "D",
    },
#    # support planned, but only if time
#    # the SPREADSHEET CSV files are very weirdly formatted with 5 lines of metadata and a change in table orientation partway through
#    "CDR_SURVEY": {
#        "manifest": PLASM_FILE,
#        "fn_must_contain": [".CSV"],
#        "url_must_contain": ['JNO', "CDR", 'WAVES_SURVEY'],
#        "label": "D",
#    },
    "edr_hsk": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".DAT"],
        "url_must_contain": ['JNO-E_J_SS-WAV-2-EDR-V1.0/DATA'],
        "label": "D",
    },
    # Support not planned - The labels have no pointers to the data files
    "edr": {
        "manifest": PLASM_FILE,
        "fn_must_contain": [".PKT"],
        "url_must_contain": ['JNO-E_J_SS-WAV-2-EDR-V1.0/DATA'],
        "label": "D",
        "support_np": True
    },
}
