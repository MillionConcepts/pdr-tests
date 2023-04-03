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

GEO_MANIFEST = Path(MANIFEST_DIR, "geomgn.parquet")

file_information = {
	
    # Magellan Bistatic Radar Raw Data Archive:
    # Original Data Record (ODR)
    "odr": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.odr'],
        "url_must_contain": ['mgn-v-rss-1-bsr', 'odr'],
        "label": "D",
    },
    # Tracking Data Files (TDF; backup/ancillary)
    "tdf": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.tdf'],
        "url_must_contain": ['mgn-v-rss-1-bsr', 'tdf'],
        "label": "D",
    },
    # Magellan Bistatic Radar Calibrated Data Archive:
    # calibrated echo spectra (SPC)
    "spectra": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.spc'],
        "url_must_contain": ['mgn-v-rss-4-bsr', 'spc'],
        "label": "D",
    },
    # amplitude-calibrated complex time samples (PRR)
    # FND_HDR_TABLE opens fine, FND_TABLE fails (DATA_TYPE = IEEE_COMPLEX)
##    "prr": {
##        "manifest": GEO_MANIFEST,
##        "fn_must_contain": ['.prr'],
##        "url_must_contain": ['mgn-v-rss-4-bsr', 'prr'],
##        "label": "D",
##    },
    # amplitude- and frequency-calibrated complex time samples (PRT)
    # FND_HDR_TABLE opens fine, FND_TABLE fails (DATA_TYPE = IEEE_COMPLEX)
##    "prt": {
##        "manifest": GEO_MANIFEST,
##        "fn_must_contain": ['.prt'],
##        "url_must_contain": ['mgn-v-rss-4-bsr', 'prt'],
##        "label": "D",
##    },
    # Ancillary CDR products:
    # coefficients for calibrating time sample amplitude (GNC) and signal frequency (SC1 and SC2)
    # COEFFICIENTS_TABLE opens fine, HDR_TABLE fails (leaning towards reading the header as text)
##    "coeff": {
##        "manifest": GEO_MANIFEST,
##        "fn_regex": [r'(gnc$)|(sc[12]$)'],
##        "url_must_contain": ['mgn-v-rss-4-bsr'],
##        "label": "D",
##    },
    # summary geometry information (SRG)
    "geom": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.srg'],
        "url_must_contain": ['mgn-v-rss-4-bsr', 'srg'],
        "label": "D",
    },
    # noise power spectra (SRF)
    "noise": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['.srf'],
        "url_must_contain": ['mgn-v-rss-4-bsr', 'srf'],
        "label": "A",
    },
	
}
