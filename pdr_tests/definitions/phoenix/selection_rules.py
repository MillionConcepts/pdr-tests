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
IMG_FILE = "img_usgs_phoenix"

file_information = {
    
    # Moved the TEGA product types to the phoenix_tega selection rules.
    
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
    # (there is a special case for the ema, emb, and amc tables)
    "wcl_edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['ws','.dat'],
        "url_must_contain": ['phx-m-meca-2-niedr-v1/phxmec_0xxx/data'],
        "label": "A",
    },
    # The "PT", "ISES", and "COND" rdr products open fine
    "wcl_rdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "fn_regex": [r'(pt_)|(ise_)|(cnd_)'],
        "url_must_contain": ['phx-m-meca-4-nirdr-v1/phxmec_1xxx/data','/wcl'],
        "label": "D",
    },
   # The "CP" and "CV" products are unsupported (wrong start bytes/offsets)
   "wcl_rdr_broken": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "fn_regex": [r'(cp_)|(cv_)'],
        "url_must_contain": ['phx-m-meca-4-nirdr-v1/phxmec_1xxx/data','/wcl'],
        "label": "D",
        "support_np": True
   },
    # MECA AFM edr and rdr
    "afm_edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['fs','.dat'],
        "url_must_contain": ['phx-m-meca-2-niedr-v1/phxmec_0xxx/data'],
        "label": "A",
    },
    # (there are 2 special cases for the rdrs)
    "afm_rdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['phx-m-meca-4-nirdr-v1/phxmec_1xxx/data','/af'],
        "label": "D",
    },
    # MECA ELEC edr (there is a special case for a subset of the em6 tables)
    "elec_edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['xs', '.dat'],
        "url_must_contain": ['phx-m-meca-2-niedr-v1/phxmec_0xxx/data'],
        "label": "A",
    },
    
    # MECA OM edr
    "om_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxom_0xxx/data'],
        "label": "A",
    },
    # SSI edr and rdr
    "ssi_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxssi_0xxx/data'],
        "label": "A",
    },
    "ssi_rdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxssi_1xxx/data'],
        "label": "A",
    },
    # RAC edr and rdr
    "rac_edr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxrac_0xxx/data'],
        "label": "A",
    },
    "rac_rdr": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxrac_1xxx/data'],
        "label": "A",
    },
    # Science RDRs
    "om_sci": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxsci_0xxx/data/om/'],
        "label": "A",
    },
    "ssi_sci": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxsci_0xxx/data/ssi'],
        "label": "A",
    },
    "rac_sci": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxsci_0xxx/data/rac'],
        "label": "A",
    },
    # Mosaics
    "rac_mosaic": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxmos_0xxx/data/rac'],
        "label": "A",
    },
    "ssi_mosaic": {
        "manifest": IMG_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['phxmos_0xxx/data/ssi'],
        "label": "A",
    },
}

