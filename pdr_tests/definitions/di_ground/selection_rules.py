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
SBN_FILE = "tiny_other"

file_information = {
    
    # TO-DO: The hawaii HEADER and IMAGE_HEADER hashes are not stable.
    # University of Hawaii Reduced 9P/Tempel 1 Images/Astrometry
    # reduced/calibrated images, calibration images, and astrometric tables
    "hawaii": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-i0034-3-uh22m-tmpl1-v1.0/data'],
        "label": "D",
    },
    "hawaii_table": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['di_ear-c-i0034-3-uh22m-tmpl1-v1.0/data'],
        "label": "D",
    },
    
    # IRTF Near-IR Spectroscopy of Comet 9P-Tempel 1
    # raw spectral images, flat field and Argon lamp images, and time tables
    "irtf_nirspec": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-i0046-2-irtf-nirspec-tmpl1-v1.0/data'],
        "label": "D",
    },
    "irtf_nirspec_table": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['di_ear-c-i0046-2-irtf-nirspec-tmpl1-v1.0/data'],
        "label": "D",
    },
    
    # IRTF Near-IR Imaging of Comet 9P-Tempel 1 --> PDS4 version available
    # raw images, flat field and dark images, and standard star observations
    "irtf_nirimg": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-i0046-2-irtf-nirimg-tmpl1-v1.0/data'],
        "label": "D",
    },
    
    # IRTF Mid-IR Imaging of Comet 9P-Tempel 1 --> PDS4 version available
    # raw images, dark images, and calibration images
    "irtf_mir": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-i0071-2-irtf-mir-tmpl1-v1.0/data'],
        "label": "D",
    },
    
    # San Pedro Martir Optical Imaging of 9P/Tempel 1
    # raw and reduced optical broadband images
    "martir_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-i0276-2_3-martir15m-tmpl1-v1.0',
                             '/data/raw'],
        "label": "D",
    },
    "martir_reduced": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-i0276-2_3-martir15m-tmpl1-v1.0',
                             '/data/reduced'],
        "label": "D",
    },
    
    # KECK I LWS MID-IR IMAGES AND PHOTOMETRY OF 9P/TEMPEL 1
    # raw and reduced mid-ir images, and flux measurements
    # (Note: the raw images are 6-D arrays, so functions like data.show() 
    # and dump-browse fail)
   "keck_raw": {
       "manifest": SBN_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['di_ear-c-keck1lws-3-9p-images-phot-v1.0',
                            '/data/raw'],
       "label": "D",
   },
    "keck_reduced": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-keck1lws-3-9p-images-phot-v1.0',
                             '/data/reduced'],
        "label": "D",
    },
    "keck_flux": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['di_ear-c-keck1lws-3-9p-images-phot-v1.0',
                             '/data/phot'],
        "label": "D",
    },
    
    # TO-DO: The lowell_raw and lowell_reduced FITS_HEADER and IMAGE_HEADER
    # hashes are not stable.
    # LOWELL 72-IN IMAGES AND PHOTOM. OF 9P/TEMPEL 1 V1.0
    # raw and reduced broadband R images, and derived photometry
    "lowell_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-lo72ccd-3-9p-images-phot-v1.0',
                             '/data/raw'],
        "label": "D",
    },
    "lowell_reduced": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-lo72ccd-3-9p-images-phot-v1.0',
                             '/data/reduced'],
        "label": "D",
    },
    "lowell_phot": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['di_ear-c-lo72ccd-3-9p-images-phot-v1.0',
                             '/data/results'],
        "label": "D",
    },
    
    # KPNO Near-IR images of comet 9P/Tempel 1 --> PDS4 version available
    # raw and reduced near-ir images
    "kpno": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-sqiid-3-9pnirimages-v1.0/data'],
        "label": "D",
    },
    
    # MT. BIGELOW 61-INCH IMAGES OF 9P/TEMPEL 1 --> safed
    "mt_bigelow": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['di_ear-c-lplccd-3-mtbg61-tmpl1-v1.0/data'],
        "label": "D",
    },

    # Support not planned --> no PDS labels
    "notes": {
        "manifest": SBN_FILE,
        "url_must_contain": ['di_ear-','/NOTES'],
        "label": "NA",
        "support_np": True,
    },
}
