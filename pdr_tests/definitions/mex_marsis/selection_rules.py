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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
GEO_MEX_FILE = Path(MANIFEST_DIR, "geomex.parquet")

file_information = {
    "EDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_f.dat'],
        "url_must_contain": ["-edr-"],
        "label": ('_f.dat', '.lbl'),
    },
    "SS_RDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_cmp_m.dat'],
        "url_must_contain": ['-rdr-ss-'],
        "label": "D",
    },
    # we appear to not be able to read these (AIS_RDR) due to an inconsistent format file
    "AIS_RDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_ais_rdr_', '.dat'],
        "url_must_contain": ['-rdr-ais-'],
        "label": "D",
    },
    "TEC_DDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['tec_ddr', '.tab'],
        "url_must_contain": ['-ddr-ss-tec-'],
        "label": "D",
    },
    "ELEDENS_BMAG_DDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_bmag_ddr', '.csv'],
        "url_must_contain": ["-ddr-eledens-bmag-"],
        "label": "D",
    },

}
