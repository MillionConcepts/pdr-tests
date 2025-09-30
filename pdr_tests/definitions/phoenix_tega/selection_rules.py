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
    # LED Sensor data
    # (Notionally Supported: These open better now with a special case, but 
    # several of the products' time columns are still wonky. It might be due to 
    # typos in the data files at this point.)
    "lededr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/lededr'],
        "label": "D",
    },
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
        "label": "A", # these are the labels, so treat them as attached
    },
    # The engedr ptype as written works great for ix testing, but leaves the 
    # many .dat files per label marked as 'uncovered' in the coverage analysis 
    # pipeline. This engedr_additional_files ptype makes sure they are 
    # correctly counted as covered products. 
    # The "ix_skip" flag ensures they are skipped on all ix calls that do not 
    # specifically pass this ptype.
    "engedr_additional_files": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/engedr'],
        "label": "A", # not actually attached labels, but don't want to double count them 
        "ix_skip": True
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
        "label": "A", # these are the labels, so treat them as attached
    },
    # The engrdr ptype as written works great for ix testing, but leaves the 
    # many .dat files per label marked as 'uncovered' in the coverage analysis 
    # pipeline. This engrdr_additional_files ptype makes sure they are 
    # correctly counted as covered products. 
    # The "ix_skip" flag ensures they are skipped on all ix calls that do not 
    # specifically pass this ptype.
    "engrdr_additional_files": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['rdr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/engrdr'],
        "label": "A", # not actually attached labels, but don't want to double count them 
        "ix_skip": True
    },
    # Thermal scanning calorimetry processed data
    "scrdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['rdr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008',
                             '/scrdr'],
        "label": "D",
    },
    # CSV files in the extras directory --> support not planned
    "extras": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/extras'],
        "label": "A", # no PDS labels
        "support_np": True
    },
}
