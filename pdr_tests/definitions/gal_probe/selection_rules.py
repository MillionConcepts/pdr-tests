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
    # ATMOSPHERIC STRUCTURE INSTRUMENT
    "asi": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/asi'],
        "label": "D",
    },
    # DOPPLER WIND EXPERIMENT
    # Most products open fine but orbtrtrj.tab and probetrj.tab appear to have
    # newline characters that aren't being dealt with correctly (possibly a data
    # QA problem with the labels).
    "dwe": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/dwe'],
        "label": "D",
    },
    # 1 DWE product has a different extension
    "dwe_adj": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.adj'],
        "url_must_contain": ['gp_0001/data/dwe'],
        "label": "D",
    },
    # ENERGETIC PARTICLES INSTRUMENT
    "epi": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/epi'],
        "label": "D",
    },
    # HELIUM ABUNDANCE DETECTOR
    "had": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/had'],
        "label": "A",
    },
    # GALILEO PROBE NEPHELOMETER
    "nep": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/nep'],
        "label": "D",
    },
    # GALILEO PROBE MASS SPECTROMETER
    # (A92NO21.TAB and A85JL02.TAB open wrong because of mistakes in the labels)
    "nms": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/nms'],
        "label": "D",
    },
    # NET FLUX RADIOMETER - calib array
    "nfr_cal_array": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['gp_0001/data/nfr/calib'],
        "label": "D",
    },
    # NET FLUX RADIOMETER - calib table
    "nfr_cal_table": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/nfr/calib'],
        "label": "A",
    },
    # NET FLUX RADIOMETER - EDR
    "nfr_edr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.sdm'],
        "url_must_contain": ['gp_0001/data/nfr/edr'],
        "label": "D",
    },
    # NET FLUX RADIOMETER - engineering data
    "nfr_eng": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/nfr/engnring'],
        "label": "A",
    },
    # NET FLUX RADIOMETER - raw data
    "nfr_raw": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gp_0001/data/nfr/raw'],
        "label": "A",
    },
}
