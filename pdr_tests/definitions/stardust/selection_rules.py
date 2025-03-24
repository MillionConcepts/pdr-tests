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
SB_FILE = "tiny_other"

file_information = {
    # Sample Return Capsule (SRC) - temperature
    "src_temp": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c-src-2-temps-v1.0/data'],
        "label": "D",
    },
    # SRC - geometry
    "src_geom": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c-src-6-geometry-v1.0/data'],
        "label": "D",
    },
    # Cometary and Interstellar Dust Analyzer (CIDA) - EDF
    "cida": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c_d-cida-1-edf_hk-v1.0/data/edfascii'],
        "label": "A",
    },
    # CIDA - housekeeping
    "cida_hk": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c_d-cida-1-edf_hk-v1.0/data/hkvalues'],
        "label": "A",
    },
    # NAVCAM - pre-flight calibration
    "nav_cal": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['stardust-cal-nc-2-preflight-v2.0/data/minus'],
        "label": "D",
    },
    "nav_cal_unusable": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['stardust-cal-nc-2-preflight-v2.0/data/unusable'],
        "label": "D",
    },
    # NAVCAM - raw images
    "nav_edr": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['sdu-', '-navcam-2-edr-', '/data'],
        "label": "D",
    },
    # NAVCAM - calibrated images
    "nav_rdr": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['sdu-', '-navcam-3-rdr-', '/data'],
        "label": "D",
    },
    # NAVCAM - derived shape models
    "nav_ddr": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c-navcam-5-wild2-shape-model-v2.1/data'],
        "label": "D",
    },
    # Dust Flux Monitor (DFMI) - EDR
    "dfmi": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c-dfmi-2-edr-wild2-v1.0/data'],
        "label": "D",
    },
    # Dynamic Science Experiment (DSE)
    "dse": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['sdu-c-dynsci-2-wild2-v1.0/data'],
        "label": "D",
    },

    # Earth-based observations supporting Stardust; Keck Observatory
    "keck_raw": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ear-c-i0039-2-sbn0007_keckiiesi-v1.0/data',
                             'raw'],
        "label": "D",
    },
    "keck_processed": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ear-c-i0039-2-sbn0007_keckiiesi-v1.0/data',
                             'processed'],
        "label": "D",
    },
    "keck_ancil": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ear-c-i0039-2-sbn0007_keckiiesi-v1.0/data'],
        "label": "D",
    },
    "keck_notes": {
        "manifest": SB_FILE,
        "url_must_contain": ['ear-c-i0039-2-sbn0007_keckiiesi-v1.0/NOTES'],
        "support_np": True
    },

    # SAFED datasets:
    # STARDUST-C/E/L-DFMI-2-EDR-V1.0 - early cruise phase DFMI data
    "safed_dfmi": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['stardust-c_e_l-dfmi-2-edr-v1.0/data'],
        "label": "D",
    },
    # STARDUST-C/E/L-NC-2-EDR-V1.0 - early cruise phase NAVCAM images
    # The IMAGE pointers open fine; the IMAGE_HISTOGRAMs fail
    "safed_nav_cruise": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['stardust-c_e_l-nc-2-edr-v1.0/data'],
        "label": "A",
    },
    # STARDUST-CAL-NC-2-PREFLIGHT-V1.0
    # V2.0 is tested above (nav_cal), and V1.0 is not included in the manifest

    # Supplementary files in the extras directory
    "extras": {
        "manifest": SB_FILE,
        "url_must_contain": ['sdu-'],
        "url_regex": [r'/extras$'],
        "support_np": True,
    },
    # Mostly ascii text files; none have PDS labels
    "notes": {
        "manifest": SB_FILE,
        "url_must_contain": ['sdu-', '/NOTES'],
        "support_np": True,
    },
    # (The extras and notes ptypes also include products from the Stardust-NEXT 
    # volumes. They are included here instead of the stardust_next selection 
    # rules for simplicity.)
}
