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

file_information = {
    
    # The PRA data from VG1 (Jupiter/Saturn encounters) are all PDS4.
    # VG2 products are still PDS3.
    
    # high rate data from VG2 Uranus/Neptune encounters; wave flux density 
    "high_rate": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2', 'PRA-2-RDR-HIGHRATE-60MS', '/DATA'],
        "label": "D",
    },
    # jupiter encounter lowband data
    # Special case: corrects START_BYTE for columns within a CONTAINER.
    "lowband_jup": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-J-PRA-3-RDR-LOWBAND-6SEC-V1.0/DATA'],
        "label": "D",
    },
    # saturn/uranus/neptune encounters lowband data
    # Special case: corrects BYTES and ITEM_BYTES for columns w/ multiple ITEMS.
    "lowband_other": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['/DATA'],
        "url_regex": [r'VG2-[SUN]-PRA-3-RDR-LOWBAND-6SEC'],
        "label": "D",
    },
    # jupiter 48sec summ browse data
    "summ_jup": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-J-PRA-4-SUMM-BROWSE-48SEC-V1.0/DATA'],
        "label": "D",
    },
    # neptune 48sec summ browse data
    "summ_nep": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-PRA-4-SUMM-BROWSE-48SEC-V1.0/DATA'],
        "label": "D",
    },
}

"""
VG2-U-PRA-4-SUMM-BROWSE-48SEC-V1.0 has multiple known unsupported products
(support not planned).
- The original binary versions use an illegal format for ITEMS and START_BYTE.
- The newer ascii version fixes the table formatting but is missing pointers
  in the label. The PPI node has been emailed about this.
- Ancillary summary products open fine.

    # uranus 48sec summ browse data; ascii product
    "summ_ur_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-PRA-4-SUMM-BROWSE-48SEC-V1.0', '/DATA'],
        "label": "D",
    },
    # uranus 48sec summ browse data; 'original binary' products
    "summ_ur_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-PRA-4-SUMM-BROWSE-48SEC-V1.0',
                             '/DATA/ORIGINAL_BINARY'],
        "label": "D",
    },
"""
