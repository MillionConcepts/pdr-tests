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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
GEO_FILE = Path(MANIFEST_DIR, "geoody.parquet")
PPI_FILE = Path(MANIFEST_DIR, "plasm_full.parquet")


file_information = {

    # Accelerometer data --> PDS4 version available at ATM node
    
    # MARS RADIATION ENVIRONMENT EXPERIMENT (MARIE)
    "marie_redr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['ODY-M-MAR-2-REDR-RAW-DATA', 'DATA/RAW'],
        "label": "D",
    },
    "marie_rdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ODY-M-MAR-3-RDR-CALIBRATED-DATA', 'DATA/2'],
        "label": "D",
    },
    
    # GRS Instrument Suite (GRS/NS/HEND)
    # EDR - gamma spectra
    "edr_gamma": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['gamma_spectra', '.dat'],
        "url_must_contain": ['ody-m-grs-2-edr-v1'],
        "label": "D",
    },
    # EDR - neutron spectra
    "edr_neutron": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['neutron_spectra', '.dat'],
        "url_must_contain": ['ody-m-grs-2-edr-v1'],
        "label": "D",
    },
    # EDR - hend spectra
    "edr_hend": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['hend_spectra', '.dat'],
        "url_must_contain": ['ody-m-grs-2-edr-v1'],
        "label": "D",
    },
    # EDR - pulser spectra
    "edr_pulser": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['pulser_spectra', '.dat'],
        "url_must_contain": ['ody-m-grs-2-edr-v1'],
        "label": "D",
    },
    # EDR - profile data
    "edr_profile": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['profile_data', '.dat'],
        "url_must_contain": ['ody-m-grs-2-edr-v1'],
        "label": "D",
    },
    # corrected gamma spectra
    "cgs": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ody-m-grs-4-cgs-v1/odgc1_xxxx/2'],
        "label": "D",
    },
    # derived neutron data
    "dnd": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['/ody-m-grs-4-dnd-v2/odgd2_xxxx/2'],
        "label": "D",
    },
    # derived hend data
    "dhd": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ody-m-grs-4-dhd-v1/odgr1_xxxx/2'],
        "label": "D",
    },
    # summed gamma spectra
    # Needs more testing. Some products open with fewer rows than their labels
    # claim. The labels could be wrong, or data could actually be missing.
##    "sgs": {
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['.dat'],
##        "url_must_contain": ['ody-m-grs-5-sgs-v1/odgs1_xxxx/yr'],
##        "label": "D",
##    },
    # averaged neutron data
    "and": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ody-m-grs-5-and-v2/odgn2_xxxx/yr'],
        "label": "D",
    },
    # averaged hend data
    "ahd": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ody-m-grs-5-ahd-v1/odgh1_xxxx/yr'],
        "label": "D",
    },
    # element concentration maps
    "maps": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ody-m-grs-5-elements-v1', '/data'],
        "label": "D",
    },
    # special data products
    "special": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ody-m-grs-special-v1'],
        "label": "D",
    },
    
    # Radio Science
    "odf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.odf'],
        "url_must_contain": ['ody-m-rss-1-raw-v1', '/odf'],
        "label": "D",
    },
    "tdf": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tdf'],
        "url_must_contain": ['ody-m-rss-1-raw-v1', '/tdf'],
        "label": "D",
    },
    "rsr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.rsr'],
        "url_must_contain": ['ody-m-rss-1-raw-v1', '/rsr'],
        "label": "D",
    },
}

