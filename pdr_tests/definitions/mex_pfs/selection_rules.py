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

GEO_FILE = "geomex"
ATM_FILE = "atm"

file_information = {
    
    # Nominal mission and extended mission 1 datasets are mirrored at ATM.
    
    # Between orbits 8944 and 8945 (in extended mission 3) errors in the labels
    # are corrected. The errors are persistent throughout the early mission
    # products, and are fixed by a special case.
    
    # Raw interferograms
    "raw_lwc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['meas_raw_lw', '.dat'],
        "url_must_contain": ['mex-m-pfs-2-edr', 'data'],
        "label": "D",
    },
    "raw_swc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['meas_raw_sw', '.dat'],
        "url_must_contain": ['mex-m-pfs-2-edr', 'data'],
        "label": "D",
    },
    # Calibration data
    "cal_lwc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['cal_raw_lw', '.dat'],
        "url_must_contain": ['mex-m-pfs-2-edr', 'data'],
        "label": "D",
    },
    "cal_swc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['cal_raw_sw', '.dat'],
        "url_must_contain": ['mex-m-pfs-2-edr', 'data'],
        "label": "D",
    },
    # Housekeeping data
    # The format file changes between orbits 8944 and 8945, but its filename
    # stays the same.
    "hk_early_mission": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['_hk_', '.dat'],
        "fn_regex": [r'pfs_(([0-7]\d{3})|(8[0-8]\d{2})|(89[0-3]\d)|(894[0-4]))_'],
        "url_must_contain": ['mex-m-pfs-2-edr', 'data'],
        "label": "D",
    },
    "hk_late_mission": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['_hk_', '.dat'],
        "fn_regex": [r'pfs_((894[5-9])|(89[5-9]\d)|(9\d{3})|(\d{5}))_'],
        "url_must_contain": ['mex-m-pfs-2-edr', 'data'],
        "label": "D",
    },
    
    # orb001x products only at ATM
    "orb001_lwc": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['mexpfs', 'data/mars/lwc/orb001x'],
        "label": "D",
    },
    "orb001_swc": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['mexpfs', 'data/mars/swc/orb001x'],
        "label": "D",
    },

    # The MEX-M-PFS-5-DDR-MAPS-V1.0 dataset is at PSA but not mirrored at GEO.
    # There are a half dozen ascii table products; water vapour maps. They
    # open fine and are listed as notionally supported.

    # Support not planned:
    # Calibrated radiance spectra
    # - ROWS does not always match FILE_RECORDS
    # - multiple columns have the wrong DATA_TYPE 
    # - the wavelength and radiance columns have the wrong START_BYTE
    "rad_lwc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['meas_rad_lw', '.dat'],
        "url_must_contain": ['mex-m-pfs-2-edr', 'data'],
        "label": "D",
        "support_np": True
    },
    "rad_swc": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['meas_rad_sw', '.dat'],
        "url_must_contain": ['mex-m-pfs-2-edr', 'data'],
        "label": "D",
        "support_np": True
    },
}

SKIP_FILES = ["MEX_ORIENTATION_DESC.TXT"]
