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
IMG_FILE = "img_usgs"

file_information = {
    # TEGA edr and rdr
    "tega_edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['edr','.dat'],
        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008'],
        "url_regex": [r'(/egaedr)|(/eghedr)|(/msgedr)|(/lededr)|(/scedr)'],
        "label": "D",
    },
##    # The "EGS' and "EGH" products looks fine, the "SC" products have 
##    # potential problems in the time columns.
##    "tega_rdr": {
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['rdr','.dat'],
##        "url_must_contain": ['phx-m-tega-2-scedr-v1/phxteg_0001/2008'],
##        "url_regex": [r'(/eghrdr)|(/egsrdr)|(/scrdr)'],
##        "label": "D",
##    },
    # MECA TECP edr and rdr
    "tecp_edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['ps','.dat'],
        "url_must_contain": ['phx-m-meca-2-niedr-v1/phxmec_0xxx/data'],
        "label": "A",
    }, 
    "tecp_rdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['phx-m-meca-4-nirdr-v1/phxmec_1xxx/data','/tecp'],
        "label": "D",
    },
    # MECA WCL edr and rdr
##    # Some products have offsets in the tables and a row missing from the
##    # end of the table.
##    "wcl_edr": {
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['ws','.dat'],
##        "url_must_contain": ['phx-m-meca-2-niedr-v1/phxmec_0xxx/data'],
##        "label": "A",
##    },
##    # The "PT", "ISES", and "COND" products open fine. The "CT" and "CV" 
##    # products have multiple pointers opening wrong. (Wrong starting byte)
##    "wcl_rdr": {
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['.tab'],
##        "url_must_contain": ['phx-m-meca-4-nirdr-v1/phxmec_1xxx/data','/wcl'],
##        "label": "D",
##    },
    # MECA AFM edr and rdr
    "afm_edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['fs','.dat'],
        "url_must_contain": ['phx-m-meca-2-niedr-v1/phxmec_0xxx/data'],
        "label": "A",
    },
##    # The HEADER_TABLE pointers do not open. The ERROR_TABLE and HEIGHT_TABLE
##    # pointers usually look right, but sometimes the data extends into an
##    # extra row at the bottom of the table.
##    "afm_rdr": {
##        "manifest": GEO_FILE,
##        "fn_must_contain": ['.tab'],
##        "url_must_contain": ['phx-m-meca-4-nirdr-v1/phxmec_1xxx/data','/af'],
##        "label": "D",
##    },
    
    # MECA OM edr
    "om_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxom_0xxx/data'],
        "label": "A",
    },
    # SSI edr and rdr
    "ssi_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxssi_0xxx/data'],
        "label": "A",
    },
    "ssi_rdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxssi_1xxx/data'],
        "label": "A",
    },
    # RAC edr and rdr
    "rac_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxrac_0xxx/data'],
        "label": "A",
    },
    "rac_rdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxrac_1xxx/data'],
        "label": "A",
    },
    # Science RDRs
    "om_sci": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxsci_0xxx/data/om/'],
        "label": "A",
    },
    "ssi_sci": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxsci_0xxx/data/ssi'],
        "label": "A",
    },
    "rac_sci": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxsci_0xxx/data/rac'],
        "label": "A",
    },
    # Mosaics
    "rac_mosaic": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxmos_0xxx/data/rac'],
        "label": "A",
    },
    "ssi_mosaic": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['Phoenix/phxmos_0xxx/data/ssi'],
        "label": "A",
    },
}

