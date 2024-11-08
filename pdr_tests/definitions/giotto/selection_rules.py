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
SB_FILE = "tiny_other"

file_information = {
    # Dust Impact Detector System (DID)
    "did": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gio-c-did-3-rdr-halley-v1.0/data'],
        "label": "D",
    },
    # Radio Science Experiment (GRE)
    # The EDRs are also archived, but their labels are missing pointers.
    "gre": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gio-c-gre-3-rdr-halley-v1.0/data'],
        "label": "D",
    },
    "gre_edr_unsupported": {
        "manifest": SB_FILE,
        "fn_regex": [r'(odr$)|(tdf$)'],
        "url_must_contain": ['gio-c-gre-1-edr-halley-addenda-v1.0/data'],
        "label": "D",
        "support_np": True
    },
    # Halley Multicolour Camera (HMC)
    "hmc": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['gio-c-hmc-3-rdr-halley-v1.0/data'],
        "label": "D",
    },
    # Ion Mass Spectrometer (IMS) - also available at PPI node
    "ims": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gio-c-ims-3-rdr-', '-halley-v1.0/data'],
        "label": "D",
    },
    # Johnstone Plasma Analyzer (JPA) - also available at PPI node
    "jpa": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gio-c-jpa-4-ddr-halley-merge-v1.0/data'],
        "label": "D",
    },
    # Magnetometer (MAG) - also available at PPI node
    "mag": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gio-c-mag-4-rdr-halley-8sec-v1.0/data'],
        "label": "D",
    },
    # Neutral Mass Spectrometer (NMS)
    "nms": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gio-c-nms-4-halley-v1.0/data'],
        "label": "A",
    },
    # Optical Probe Experiment (OPE)
    "ope": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['gio-c-ope-3-rdr-halley-v1.0/data'],
        "label": "D",
    },
    # Particle Impact Analyzer (PIA)
    "pia": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.dat'],
       "url_must_contain": ['gio-c-pia-3-rdr-halley-v1.0/data/mode'],
       "label": "D",
    },
}
