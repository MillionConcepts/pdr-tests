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
PPI_FILE = "plasm_full"
GEO_FILE = "geomex"

file_information = {
    
    # ELS high and low range EDRs
    "els_edr_high": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['ELSSCIH', '.CSV'],
        "url_must_contain": ['MEX-M-ASPERA3-2-EDR-ELS', 'DATA'],
        "label": "D",
    },
    "els_edr_low": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['ELSSCIL', '.CSV'],
        "url_must_contain": ['MEX-M-ASPERA3-2-EDR-ELS', 'DATA'],
        "label": "D",
    },
    # ELS high and low range RDRs
    "els_rdr_high": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['ELSSCIH', '.CSV'],
        "url_must_contain": ['MEX-M-ASPERA3-3-RDR-ELS', 'DATA'],
        "label": "D",
    },
    "els_rdr_low": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['ELSSCIL', '.CSV'],
        "url_must_contain": ['MEX-M-ASPERA3-3-RDR-ELS', 'DATA'],
        "label": "D",
    },
    # IMA EDRs
    "ima": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['MEX-M-ASPERA3-2-EDR-IMA', 'DATA'],
        "label": "D",
    },
    # Solar wind data derived from IMA
    # (This dataset is at GEO but not PPI)
    "ima_ddr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mex-sun-aspera3-4-swm', 'data'],
        "label": "D",
    },
    # NPI counts/accumulation EDRs
    "npi_acc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.CSV'],
        "url_must_contain": ['MEX-M-ASPERA3-2-EDR-NPI', 'DATA'],
        "label": "D",
    },
    # NPI counts/second combined EDR/RDRs
    # (Extended mission 5 products at PPI have broken links)
    "npi_sec": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['mex-m-aspera3-2-3-edr-rdr-npi', 'data'],
        "label": "D",
    },

    # ancillary index table
    "index_table": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['mex-m-aspera3-2-3-edr-rdr-npi', 'extras'],
        "label": "D",
    },
    "index_table_PPI": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['MEX-M-ASPERA3', 'EXTRAS'],
        "label": "D",
    },
    # support not planned
    "spice": {
        "manifest": GEO_FILE,
        "url_must_contain": ['mex-m-aspera3-2-3-edr-rdr-npi',
                            'extras/spice_data'],
        "label": "NA",
        "support_np": True
    },
    "compressed": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.zip'],
        "url_must_contain": ['mex-m-aspera3-2-3-edr-rdr-npi', 'extras'],
        "label": "D",
        "support_np": True
    },
    "spice_PPI": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((BC)|(TF)|(TI)|(TLS)|(ORB)|(TPC)|(BPC)|(TSC)|(BSP))$'],
        "url_must_contain": ['MEX-M-ASPERA3', 'EXTRAS/SPICE_DATA'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    "compressed_PPI": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.ZIP'],
        "url_must_contain": ['MEX-M-ASPERA3', 'EXTRAS'],
        "label": "D",
        "support_np": True
    },
}
