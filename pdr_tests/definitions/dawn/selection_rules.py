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
MANIFEST_FILE = Path(MANIFEST_DIR, "tiny.parquet")

file_information = {
    # GRaND products have PDS4 versions available: EDR, RDR, maps/mosaics
    
    # Framing Camera - calibration images
    # A few products are known unsupported: 20110925_FC1_VTH_CHKOUT_DARK_V01,
    # 20120626_FC1_VT2_CHKOUT_DARK_V01, FC1_FLAT_HI_F4_N,
    # FC2_F7_FLAT_V02_SLR_NORM, and FC2_F8_FLAT_V02_SLR_NORM
    "fc_cal": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['dawn/fc/DWNCALFC', 'DATA'],
        "label": "A",
    },
    # Framing Camera - EDR (IMG version)
    "fc_edr_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['dawn/fc/DWN', '_1A/DATA'],
        "label": "A",
    },
    # Framing Camera - EDR (FITS version)
    "fc_edr_fit": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.FIT'],
        "url_must_contain": ['dawn/fc/DWN', '_1A/DATA'],
        "label": "D",
    },
    # Framing Camera - RDR (IMG version)
    "fc_rdr_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['dawn/fc/DWN', '_1B/DATA'],
        "label": "A",
    },
    # Framing Camera - RDR (FITS version)
    "fc_rdr_fit": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.FIT'],
        "url_must_contain": ['dawn/fc/DWN', '_1B/DATA'],
        "label": "D",
    },
    # Framing Camera - mosaics and shape models
    "fc_mosaic": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['dawn/fc/DWN', '_2/DATA'],
        "label": "A",
    },
    # Framing Camera - shape models
    "fc_shape": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.ICQ'],
        "url_must_contain": ['dawn/fc/DWNCSPC_4_01/DATA/ICQ'],
        "label": "D",
    },
    
    # VIR - IR and VIS EDR
    # Support planned --> BAND_STORAGE_TYPE=SAMPLE_INTERLEAVED
##    "vir_edr": {
##        "manifest": MANIFEST_FILE,
##        "fn_must_contain": ['.QUB'],
##        "url_must_contain": ['dawn/vir/DWN', '1A/DATA'],
##        "label": "D",
##    },
    # VIR - IR and VIS RDR
    # Support planned --> BAND_STORAGE_TYPE=SAMPLE_INTERLEAVED
##    "vir_rdr": {
##        "manifest": MANIFEST_FILE,
##        "fn_must_contain": ['.QUB'],
##        "url_must_contain": ['dawn/vir/DWN', '1B/DATA'],
##        "label": "D",
##    },
    # VIR - Ceres mosaics
    "vir_mosaic_ceres": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['dawn/vir/DWNCVIR_2/DATA'],
        "label": "D",
    },
    # VIR - Vesta mosaics
    # (4 products in archive. Only 1 has actual data, the rest are just labels.)
    "vir_mosaic_vesta": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['dawn/vir/DWNVVIR_2/DATA'],
        "label": "A",
    },
    
    # RSS - gravity models
    "shadr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['dawn/grav/DWN', 'GRS_2', 'DATA/SHADR'],
        "label": "D",
    },
    "shbdr": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['dawn/grav/DWN', 'GRS_2', 'DATA/SHBDR'],
        "label": "D",
    },
    "rsdmap": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.IMG'],
        "url_must_contain": ['dawn/grav/DWN', 'GRS_2', 'DATA/RSDMAP'],
        "label": "D",
    },
    # RSS - gravity EDR -> brief manual testing of PDS4 products looks good
}