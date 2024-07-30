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

file_information = {
    
    # # EDR -  binary tables
    # "edr": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": [".DAT"],
    #     "url_must_contain": ["MSL-M-RAD-2-EDR-V1.0/DATA"],
    #     "label": "D",
    # },
    # # RDR - ascii tables
    # "rdr": {
    #     "manifest": PPI_FILE,
    #     "fn_must_contain": [".TXT"],
    #     "url_must_contain": ["MSL-M-RAD-3-RDR-V1.0/DATA"],
    #     "label": "D",
    # },

}

"""
EDR
- The labels define a single SCIENCE_TABLE pointer, which breaks down into FRAME_HEADER and SCIENCE_OBSERVATION CONTAINERs within the format file.
- That might be fine, but there are also bit column issues popping up

RDR
- ascii tables in .txt files
- class TypeError
- pvl issues; the labels are very large with many many pointers

"""
