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
manifest files

url_must_contain: an optional additional list of strings that must be in the
url (counting the entire url) to differentiate this from other types in the
manifest file. useful for specifying directories.

label: "A" if the labels for this product type are attached; "D" if the labels
are detached.
"""

# variables naming specific parquet files in node_manifests
BC_FILE = "img_esa_bc"

file_information = {
    #
    "mag_ob_scf": {
        "manifest": BC_FILE,
        "fn_must_contain": ['mag_der_sc_ob', '_scf_', '.tab'],
        "url_must_contain": ['BepiColombo', 'data_derived'],
        "label": ('.tab', '.xml'),
    },
    #
    "mag_ob_e2k": {
        "manifest": BC_FILE,
        "fn_must_contain": ['mag_der_sc_ob', '_e2k_', '.tab'],
        "url_must_contain": ['BepiColombo', 'data_derived'],
        "label": ('.tab', '.xml'),
    },
    #
    "mag_ib_scf": {
        "manifest": BC_FILE,
        "fn_must_contain": ['mag_der_sc_ib', '_scf_', '.tab'],
        "url_must_contain": ['BepiColombo', 'data_derived'],
        "label": ('.tab', '.xml'),
    },
    #
    "mag_ib_e2k": {
        "manifest": BC_FILE,
        "fn_must_contain": ['mag_der_sc_ib', '_e2k_', '.tab'],
        "url_must_contain": ['BepiColombo', 'data_derived'],
        "label": ('.tab', '.xml'),
    },
    "mag_ib_gse": {
        "manifest": BC_FILE,
        "fn_must_contain": ['mag_der_sc_ib', '_gse_', '.tab'],
        "url_must_contain": ['BepiColombo', 'data_derived'],
        "label": ('.tab', '.xml'),
    },
    "cam1_raw": {
        "manifest": BC_FILE,
        "fn_must_contain": ['cam1', 'cam_raw', '.fits'],
        "url_must_contain": ['BepiColombo', 'data_raw'],
        "label": ('.fits', '.xml'),
    },
    "cam2_raw": {
        "manifest": BC_FILE,
        "fn_must_contain": ['cam2', 'cam_raw', '.fits'],
        "url_must_contain": ['BepiColombo', 'data_raw'],
        "label": ('.fits', '.xml'),
    },
    # the directory where this was disappeared??
    # "cam3_raw": {
    #     "manifest": BC_FILE,
    #     "fn_must_contain": ['cam3', 'cam_raw', '.fits'],
    #     "url_must_contain": ['BepiColombo', 'data_raw'],
    #     "label": ('.fits', '.xml'),
    #},
}
