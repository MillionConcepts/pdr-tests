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
ATM_FILE = "atm"

file_information = {
    # image data; well-labeled 2-dimentsional arrays
    "IMG_RDR": {
        "manifest": ATM_FILE,
        "fn_must_contain": [".IMG", "RDR"],
        "url_must_contain": ['juno_jiram_bundle', "/data_calibrated/"],
        "label": "D",
    },
    # spectral data; fixed-length tables
    "SPE_RDR": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.DAT', 'SPE_RDR'],
        "url_must_contain": ['juno_jiram_bundle', '/data_calibrated/'],
        "label": "D",
    },
    # image data; well-labeled 2-dimentsional arrays
    "IMG_EDR": {
        "manifest": ATM_FILE,
        "fn_must_contain": [".IMG", "EDR"],
        "url_must_contain": ['juno_jiram_bundle', "/data_raw/"],
        "label": "D",
    },
    # spectral data; fixed-length tables
    "SPE_EDR": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.DAT', "SPE_EDR"],
        'url_must_contain': ['juno_jiram_bundle', '/data_raw/'],
        "label": "D",
    },
    # housekeeping telemetry data; fixed-length tables
    "LOG_IMG_RDR": {
        "manifest": ATM_FILE,
        "fn_must_contain": [".TAB", "LOG_IMG_RDR"],
        "url_must_contain": ['juno_jiram_bundle', "/data_calibrated/"],
        "label": "D",
    },
    # housekeeping telemetry data; fixed-length tables
    "LOG_SPE_RDR": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB', "LOG_SPE_RDR"],
        "url_must_contain": ['juno_jiram_bundle', '/data_calibrated/'],
        "label": "D",
    },
    # housekeeping telemetry data; fixed-length tables
    "LOG_IMG_EDR": {
        "manifest": ATM_FILE,
        "fn_must_contain": [".TAB", "LOG_IMG_EDR"],
        "url_must_contain": ['juno_jiram_bundle', '/data_raw/'],
        "label": "D",
    },
    # housekeeping telemetry data; fixed-length tables
    "LOG_SPE_EDR": {
        "manifest": ATM_FILE,
        "fn_must_contain": [".TAB", "LOG_SPE_EDR"],
        "url_must_contain": ['juno_jiram_bundle', "/data_raw/"],
        "label": "D",
    },

    # Volumes not included in the PDS4 juno_jiram_bundle:
    # jnojir_1000, jnojir_2000
    "flyby_img_edr": {
        "manifest": ATM_FILE,
        "fn_must_contain": [".IMG", "IMG_EDR"],
        "url_must_contain": ['jnojir_1000/DATA'],
        "label": "D",
    },
    "flyby_spe_edr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.DAT', "SPE_EDR"],
        'url_must_contain': ['jnojir_1000/DATA'],
        "label": "D",
    },
    "flyby_logs": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB', "LOG"],
        'url_regex': [r'jnojir_[12]000/DATA'],
        "label": "D",
    },
    # The RDRs open wrong. Looks like either a scaling or byte counting issue
    # "flyby_img_rdr": {
    #     "manifest": ATM_FILE,
    #     "fn_must_contain": [".IMG", "IMG_RDR"],
    #     "url_must_contain": ['jnojir_2000/DATA'],
    #     "label": "D",
    # },
    # "flyby_spe_rdr": {
    #     "manifest": ATM_FILE,
    #     "fn_must_contain": ['.DAT', 'SPE_RDR'],
    #     "url_must_contain": ['jnojir_2000/DATA'],
    #     "label": "D",
    # },

}
