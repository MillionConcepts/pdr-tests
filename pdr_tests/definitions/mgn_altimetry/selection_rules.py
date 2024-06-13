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
GEO_MANIFEST = "geomgn"

file_information = {
    
    # Altimeter Experiment Data Record
    # known unsupported; support not planned; labels not PDS compliant (COLUMNS = 'UNK')
##     "edr": {
##         "manifest": GEO_MANIFEST,
##         "fn_must_contain": ['.DAT'],
##         "url_must_contain": ['mgn-v-rdrs-2-alt-edr-v1'],
##         "label": "D",
##     },
    # Altimetry and Radiometry Composite Data Records
    # 3 products per orbit: orbit header (OHF), altimetry (ADF), radiometry (RDF)
    # known unsupported; support planned --> VAX_REAL 64 bit data type
    # "arcdr": {
    #     "manifest": GEO_MANIFEST,
    #     "fn_regex": [r'((ad)|(oh)|(rd))f.*\.([1-9]*)$'],
    #     "url_must_contain": ['mgn-v-rdrs-5-cdr-alt-rad-v1'],
    #     "label": "D",
    # },
    
    # Derived products that pull at least some of their data from ALT-EDR and/or ARCDR:

    # Surface Characteristics Vector Data Record 
    # 6 products per orbit: altimetry inversion (ANF), emissivity (EDF), alt inversion fit
    # (NFF), orbit header (OHF), oblique sinusoidal image (OIF), sinusoidal image (SIF)
    # known unsupported; support not planned would require format specific parsers
    # "scvdr": {
    #     "manifest": GEO_MANIFEST,
    #     "fn_regex": [r'\.[1-9]$'],
    #     "url_must_contain": ['mgn-v-rdrs-5-scvdr-v1', '/s'],
    #     "label": "D",
    # },
    # Global Vector Data Record
    # Similar archive layout as GxDR with merc, north, south, and sinus subdirectories
    # Data products: GVADF, GVANF, GVRDF, GVXIF (others are ancilllary)
    "gvdr": {
        "manifest": GEO_MANIFEST,
        "fn_must_contain": ['gv', '.tab'],
        "url_must_contain": ['mgn-v-rdrs-5-gvdr-v1', '/gvdr/'],
        "label": "D",
    },
}
