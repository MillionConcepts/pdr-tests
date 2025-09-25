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
GEO_MEX_FILE = "geomex"

file_information = {
    "EDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_f.dat'],
        "url_must_contain": ["-edr-"],
        "label": ('_f.dat', '.lbl'),
    },
    # The EDR ptype as written works great for ix testing, but leaves the 
    # label and AUXILIARY_DATA_TABLE files marked as 'uncovered' in the 
    # coverage analysis pipeline. This EDR_additional_files ptype makes sure 
    # they are correctly counted as covered products. 
    # The "ix_skip" flag ensures they are skipped on all ix calls that do not 
    # specifically pass this ptype.
    "EDR_additional_files": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_g.dat'],
        "url_must_contain": ["mex-m-marsis-2-edr", "/data/"],
        "label": "A", # not actually attached labels, but don't want to double count them 
        "ix_skip": True
    },
    "SS_RDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_cmp_m.dat'],
        "url_must_contain": ['-rdr-ss-'],
        "label": "D",
    },
    "SS_RDR_phobos": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_cmp_p.dat'],
        "url_must_contain": ['-rdr-ss-'],
        "label": "D",
    },
    "SS_RDR_cal": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_cmp_t.dat'],
        "url_must_contain": ['-rdr-ss-'],
        "label": "D",
    },
    # we appear to not be able to read these (AIS_RDR) due to an inconsistent format file
    "AIS_RDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_ais_rdr_', '.dat'],
        "url_must_contain": ['-rdr-ais-'],
        "label": "D",
    },
    "TEC_DDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['tec_ddr', '.tab'],
        "url_must_contain": ['-ddr-ss-tec-'],
        "label": "D",
    },
    "ELEDENS_BMAG_DDR": {
        "manifest": GEO_MEX_FILE,
        "fn_must_contain": ['_bmag_ddr', '.csv'],
        "url_must_contain": ["-ddr-eledens-bmag-"],
        "label": "D",
    },

}
