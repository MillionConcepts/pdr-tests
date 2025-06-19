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
GEO_FILE = "geolunar"
PPI_FILE = "plasm_full"

file_information = {
    # Line of Sight Acceleration Profile Data Record 
    "losapdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.los'],
        "url_must_contain": ['lp-l-rss-5-los-v1'],
        "url_regex": [r'(nominal)|(extended)'],
        "label": "D",
    },
    # LOSRES output; once decompressed they are text files without PDS labels
    "losres_output": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.zip'],
        "url_must_contain": ['lp-l-rss-5-los-v1', 'extras'],
        "label": "A",
        "support_np": True
    },

    # Electron Reflectometer (ER) high resolution data
    "er_rdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-3-RDR-HIGHRESFLUX-V1.1', 'ER_HI_TS'],
        "label": "D",
    },
    # ER low resolution data
    "er_summ": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-4-SUMM-OMNIDIRELEFLUX-V1.1', 'ER_LO_TS'],
        "label": "D",
    },
    # ER omni-directional 3-D electron flux data
    "er_3d": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-3-RDR-3DELEFLUX-80SEC-V1.1', 'ER_3D'],
        "label": "D",
    },
    # ER level 2 data
    "er_lvl2": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-4-ELECTRON-DATA-V1.0/DATA'],
        "label": "D",
    },
    # Magnetometer (MAG) 
    "mag_summ": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-4-SUMM-LUNARCRDS-5SEC-V1.0/DATA/MAG'],
        "label": "D",
    },
    # MAG level 2 data
    "mag_lvl2": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-4-LUNAR-FIELD-TS-V1.0/DATA'],
        "label": "D",
    },
    # MAG level 3 data: Regional Field Maps
    "mag_lvl3": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-5-LUNAR-FIELD-BINS-V1.0/DATA'],
        "label": "D",
    },
    # MAG level 4 data: Large-Scale Vector Field Maps
    "mag_lvl4": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-5-SURFACE-FIELD-MAP-V1.0/DATA'],
        "label": "D",
    },
    # level 0 data: spacecraft attitude
    "attitude": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ENG-6-ATTITUDE-V1.0/DATA/ATTITUDE'],
        "label": "D",
    },
    # level 0 data: spacecraft trajectory 
    "trajectory": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-6-TRAJECTORY-V1.0/DATA'],
        "label": "D",
    },
    # level 0 data: commands sent to the spacecraft
    "command": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ENG-6-COMMAND-V1.0/DATA/COMMAND'],
        "label": "D",
    },

    # ancillary/geometry ascii tables
    "er_ancillary": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ER-'],
        "url_regex": [r'(/EXTRAS)|(/DATA/((ANCILLARY)|(THETA)|(E_BINS)))'],
        "label": "D",
    },
    "mag_ancillary": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-4-SUMM-LUNARCRDS-5SEC-V1.0'],
        "url_regex": [r'(/EXTRAS)|(/DATA/ANCILLARY)'],
        "label": "D",
    },
    "mag_geometry": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-MAG-4-SUMM-LUNARCRDS-5SEC-V1.0/GEOMETRY'],
        "label": "D",
    },
    "eng_ancillary": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['LP-L-ENG', 'DATA/ANCILLARY'],
        "label": "D",
    },
    # "traj_ancillary": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": ['.TAB'],
    #     "url_must_contain": ['LP-L-6-TRAJECTORY-V1.0/EXTRAS'],
    #     "label": "D",
    # },

    # Support not planned (no pointers in the labels)
    "ephemeris": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['LP-L-6-EPHEMERIS-V1.0/DATA/EPHEMERIS'],
        "label": "D",
        "support_np": True
    },
    "position": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['LP-L-6-POSITION-V1.0/DATA/POSITION'],
        "label": "D",
        "support_np": True
    },
    "spice": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((TLS)|(TSP)|(TPC))$'],
        "url_must_contain": ['LP-L-', '/EXTRAS'],
        "label": "D",
        "support_np": True
    },
    "random_file": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.opt'],
        "url_must_contain": ['LP-L-MAG-4-LUNAR-FIELD-TS-V1.0/DATA'],
        "label": "A", # no PDS label
        "support_np": True
    },
}
"""
Support planned:

    # level 0 data: merged telemetry files
    # They do not open (UserWarning: Unable to load TABLE: "('BIT_STRING',
    # nan, 2) is not a currently-supported data type.")
    "telemetry": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.B'],
        "url_must_contain": ['LP-L-ENG_GRS_NS_APS_MAG_ER-1-MDR-V1.0/DATA/MERGED'],
        "label": "D",
    },
    # level 0 data: sun pulse data
    # They open but incorrectly (The time columns look like nonsense)
    "sunpulse": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.B'],
        "url_must_contain": ['LP-L-ENG-6-SUNPULSE-V1.0/DATA/SUNPULSE'],
        "label": "D",
    },
"""
