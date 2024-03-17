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
GEO_FILE = "geophx"

file_information = {
    # EDRs:
    # Mass Spectrometer sweep raw data
    "egaedr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/egaedr'],
        "label": "D",
    },
    # Mass Spectrometer peak hopping raw data
    "eghedr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/eghedr'],
        "label": "D",
    },
    # TA and EGA engineering raw data (each lbl has pointers to many dat files)
    "engedr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.lbl'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/engedr'],
        "label": "D",
    },
    # TEGA message log
    "msgedr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/msgedr'],
        "label": "D",
    },
    # Thermal scanning calorimetry raw data
    "scedr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/scedr'],
        "label": "D",
    },
    # RDRs:
    # Mass Spectrometer sweep processed data
    "egsrdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['rdr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/egsrdr'],
        "label": "D",
    },
    # Mass Spectrometer peak hopping processed data
    "eghrdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['rdr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/eghrdr'],
        "label": "D",
    },
    # TA and EGA engineering processed data (each lbl has pointers to many dat files)
    "engrdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['rdr','.lbl'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/engrdr'],
        "label": "D",
    },
}
"""
All tables have 1 fewer rows than the labels claim. The time columns are also a mess.
    # LED Sensor data
    "lededr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/lededr'],
        "label": "D",
    },
    
The time columns have problems. Some are all 0, others are not human readable.
    # Thermal scanning calorimetry processed data
    "scrdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['rdr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/scrdr'],
        "label": "D",
    },
"""
