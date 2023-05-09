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
PPI_FILE = Path(MANIFEST_DIR, "plasm_full.parquet")
ATM_FILE = Path(MANIFEST_DIR, "atm.parquet")

file_information = {
    # OEFD - HIRES original binary files
    "oefd_hires_bi": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['EFD_HRES', '.FFD'],
        "url_must_contain": ['PVO-V-OEFD-3--EFIELD-HIRES-V1.0',
                             'ORIGINAL_BINARY'],
        "label": "D",
    },
    # OEFD - HIRES ascii version
    "oefd_hires_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['OEFD_HRES', '.TAB'],
        "url_must_contain": ['PVO-V-OEFD-3--EFIELD-HIRES-V1.0', 'ASCII'],
        "label": "D",
    },
    # OEFD - 24 second averages original binary files
    "oefd_24s_bi": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['EFD_24S', '.FFD'],
        "url_must_contain": ['PVO-V-OEFD-4--EFIELD-24SEC-V1.0',
                             'ORIGINAL_BINARY'],
        "label": "D",
    },
    # OEFD - 24 second averages ascii version
    "oefd_24s_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['OEFD_24S', '.TAB'],
        "url_must_contain": ['PVO-V-OEFD-4--EFIELD-24SEC-V1.0', 'ASCII'],
        "label": "D",
    },
    
    # OETP - HIRES
    "oetp_hires": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['PVO-V-OETP-3-HIRESELECTRONS', 'DATA'],
        "label": "D",
    },
    # OETP - Misc (bow shock, ionopause, lowres, solar) -> 1 product per dataset
    "oetp_misc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['OETP_', '.TAB'],
        "url_must_contain": ['PVO-V-OETP-5-', 'DATA'],
        "label": "D",
    },
    
    # OIMS - HIRES
    "oims_hires": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['PVO-V-OIMS-3-IONDENSITY-HIRES', 'DATA'],
        "label": "D",
    },
    # OIMS - 12 second averages
    # All labels define the table pointer as 42 rows, this is incorrect. Most
    # tables are shorter or longer than 42 rows. (fixed with a special case)
    "oims_12s": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['PVO-V-OIMS-4-IONDENSITY-12S', 'DATA'],
        "label": "D",
    },
    
    # ONMS - Misc -> 7 datasets, 1 product per dataset
    "onms_misc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['ONMS_', '.TAB'],
        "url_must_contain": ['PVO-V-ONMS-', 'DATA'],
        "label": "D",
    },
    
    # ORPA - ion
    "orpa_ion": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['ION.TAB'],
        "url_must_contain": ['PVO-V-ORPA-5-ELE_ION_PHOTO_UADS-V1.0',
                             'DATA/ION'],
        "label": "D",
    },
    # ORPA - ion uncertainty
    "orpa_ion_unc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['ION_UNC.TAB'],
        "url_must_contain": ['PVO-V-ORPA-5-ELE_ION_PHOTO_UADS-V1.0',
                             'DATA/ION_UNCERTAINTY'],
        "label": "D",
    },
    # ORPA - low resolution
    # A typo is introduced to the labels between orbits 0969 and 1039. The
    # table's ROW_BYTES should be 243, but are incorrectly changed to 241.
    # (fixed with a special case)
    "orpa_lowres": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['LOW_RES.TAB'],
        "url_must_contain": ['PVO-V-ORPA-5-ELE_ION_PHOTO_UADS-V1.0',
                             'DATA/LOW_RES'],
        "label": "D",
    },
    # ORPA - photo electron
    "orpa_photo": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['PHOTO_ELE.TAB'],
        "url_must_contain": ['PVO-V-ORPA-5-ELE_ION_PHOTO_UADS-V1.0',
                             'DATA/PHOTO_ELECTRON'],
        "label": "D",
    },
    # ORPA - thermal electron
    "orpa_thermal": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['THERM_ELE.TAB'],
        "url_must_contain": ['PVO-V-ORPA-5-ELE_ION_PHOTO_UADS-V1.0',
                             'DATA/THERMAL_ELECTRON'],
        "label": "D",
    },
    
    # POS - position data, original binary files
    "pos_bi": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.FFD'],
        "url_must_contain": ['PVO-V-POS-5--VSOCOORDS-12SEC-V1.0',
                             'ORIGINAL_BINARY'],
        "label": "D",
    },
    # POS - position data, ascii version
    "pos_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['PVO-V-POS-5--VSOCOORDS-12SEC-V1.0',
                             'ASCII'],
        "label": "D",
    },
    # POS - supplemental experimenter data records (SEDR)
    # Most format files include "IBM REAL" as a DATA_TYPE
    # SL.FMT uses "EBCDIC CHARACTER" as a DATA_TYPE
##    "pos_sedr": {
##        "manifest": PPI_FILE,
##        "fn_must_contain": ['.DAT'],
##        "url_must_contain": ['PVO-V-POS-6-SEDR-ORBITATTITUDE--V1.0/DATA'],
##        "label": "D",
##    },
    
    # OUVS - Inbound Monochrome Images (IMIDR)
    # The DATA_IMAGE pointer uses VAX_REAL as the DATA_TYPE.
    # BIN_IMAGE and RP_IMAGE are VAX_INTEGER and might be opening fine.
##    "imidr": {
##        "manifest": ATM_FILE,
##        "fn_must_contain": ['.img'],
##        "url_must_contain": ['pv01_100', 'data'],
##        "label": "A",
##    },
}
