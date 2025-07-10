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
MANIFEST_FILE = "tiny_sbnarchive"

file_information = {
    # GRaND products have PDS4 versions available: EDR, RDR, maps/mosaics
    
    # Framing Camera - calibration images
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
    # Framing Camera - shape models ancillary tables
    "fc_shape_anc": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['dawn/fc/DWNCSPC_4_01/DATA'],
        "label": "D",
    },
    # VIR - IR and VIS EDR
    "vir_edr": {
       "manifest": MANIFEST_FILE,
       "fn_must_contain": ['.QUB'],
       "url_must_contain": ['dawn/vir/DWN', 'DATA'],
       "url_regex": [r'(VIR_V1A)|(VIR_I1A)'],
       "label": "D",
     },
    # VIR - IR and VIS RDR
    "vir_rdr": {
       "manifest": MANIFEST_FILE,
       "fn_must_contain": ['.QUB'],
       "url_must_contain": ['dawn/vir/DWN', 'DATA'],
       "url_regex": [r'(VIR_V1B)|(VIR_I1B)'],
       "label": "D",
    },
    # VIR - housekeeping data
    "vir_hk": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['dawn/vir/DWN','DATA'],
        "label": "D",
    },
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

    # SPICE kernels - lists of SPICE kernels used
    "vir_spice": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((TM)|(MK))$'],
        "url_must_contain": ['dawn/vir/DWN', 'GEOMETRY'],
        "label": "D",
    },
    "fc_spice": {
        "manifest": MANIFEST_FILE,
        "fn_regex": [r'((mk)|(tpc))$'],
        "url_must_contain": ['dawn/fc/DWN', 'GEOMETRY'],
        "label": "D",
    },
    "fc_spice_no_label": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.MK'],
        "url_must_contain": ['dawn/fc/DWN', 'GEOMETRY'],
        "label": "A", # missing a label
        "support_np": True,
    },
}
