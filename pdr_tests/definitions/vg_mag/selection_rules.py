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

# variables naming specific parquet files in node_manifests
PPI_FILE = "plasm_full"

file_information = {

    # PDS4: VG1 Jupiter and Saturn, and VG2 Jupiter
    # Safed: VG1 and VG2 solar wind data
    # PDS3: VG2 Saturn, Uranus, and Neptune
    
    # ASCII Versions:
    
    # RDR - Saturn, Heliographic coordinates
    "rdr_sat_hg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-S-MAG-4-RDR-HGCOORDS', '/DATA'],
        "label": "D",
    },
    # RDR - Saturn, Kronographic coordinates
    "rdr_sat_l1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-S-MAG-4-RDR-L1COORDS', '/DATA'],
        "label": "D",
    },
    # SUMM - Saturn
    "summ_sat": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-S-MAG-4-SUMM', '/DATA'],
        "label": "D",
    },
    # RDR - Uranus, HG coordinates
    "rdr_ura_hg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-MAG-4-RDR-HGCOORDS', '/DATA'],
        "label": "D",
    },
    # RDR - Uranus, Uranus Longitude coordinates
    "rdr_ura_u1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-MAG-4-RDR-U1COORDS', '/DATA'],
        "label": "D",
    },
    # SUMM - Uranus, HG coordinates
    "summ_ura_hg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-MAG-4-SUMM-HGCOORDS', '/DATA'],
        "label": "D",
    },
    # SUMM - Uranus, UL coordinates
    "summ_ura_u1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-U-MAG-4-SUMM-U1COORDS', '/DATA'],
        "label": "D",
    },
    # RDR - Neptune
    "rdr_nep": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG2-N-MAG-4-RDR', '/DATA'],
        "label": "D",
    },
    # SUMM - Neptune
    "summ_nep": {
        "manifest": PPI_FILE,
        "fn_regex": [r'(TAB)|(ASC)$'],
        "url_must_contain": ['VG2-N-MAG-4-SUMM', '/DATA'],
        "label": "D",
    },
    
    # Binary Versions:
    
    # RDR - Uranus, HG coordinates
    "bin_rdr_ura_hg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-MAG-4-RDR-HGCOORDS', '/DATA'],
        "label": "D",
    },
    # RDR - Uranus, UL coordinates
    "bin_rdr_ura_u1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-MAG-4-RDR-U1COORDS', '/DATA'],
        "label": "D",
    },
    # SUMM - Uranus, HG coordinates
    "bin_summ_ura_hg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-MAG-4-SUMM-HGCOORDS', '/DATA'],
        "label": "D",
    },
    # SUMM - Uranus, UL coordinates
    "bin_summ_ura_u1": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-U-MAG-4-SUMM-U1COORDS', '/DATA'],
        "label": "D",
    },
    # RDR - Neptune
    "bin_rdr_nep": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-MAG-4-RDR', '/DATA'],
        "label": "D",
    },
    # SUMM - Neptune
    "bin_summ_nep": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG2-N-MAG-4-SUMM', '/DATA'],
        "label": "D",
    },
    
    # Safed datasets:
    # VG1 and VG2 solar wind data
    "solar_wind": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG','-SW-MAG-4-SUMM-HGCOORDS', '/DATA'],
        "label": "D",
    },
    # VG1 and VG2 cruise phase position/trajectory data
    "position_cruise": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG','-SS-POS-6-1DAY-V1.0/DATA'],
        "label": "D",
    },
}

