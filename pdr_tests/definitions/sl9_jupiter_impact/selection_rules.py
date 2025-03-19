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
ATM_FILE = "atm"

file_information = {
    
    # NASA Infra Red Telescope Facility - NSFCAM Near-IR images
    "irtf": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['irtf-j_c-nsfcam-3-rdr-sl9-v1.0/irtf'],
        "label": "D",
    },
    
    # Global Imaging Campaign - high-speed optical CCD imaging from 5
    # observatories during the impact
    "gic": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ear-j_c-hsccd-3-rdr-sl9-v1.0/data/gic'],
        "label": "D",
    },
    
    # Anglo-Australian Observatory - imaging, spectroscopy, and spectral mapping
    # FITS cubes
    "aao": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['/aat/frag'],
        "url_regex": [r'(sl9_000[89])|(sl9_001[012])'],
        "label": "D",
    },
    # Four additional ground-based observatory datasets are archived at the
    # ATM node pending peer review. They open fine during manual spot checks
    # of a handful of products, and are notionally supported.
    # (https://atmos.nmsu.edu/PDS/review/sl9_0007/)
    
    # Io and Europa Photometry during impact flashes
    "flash": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ear-j_sa-hsotp-2-edr-sl9-v1.0/data/flash'],
        "label": "D",
    },
    
    # European Southern Observatory - EMMI images, IR spectra, and SUSI images
    # Mirrored at SBN and ATM
    "eso_emmi": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['eso-c-emmi-3-rdr-sl9-v1.0/eso/emmi'],
        "label": "D",
    },
    "eso_ir": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['eso-j-irspec-3-rdr-sl9-v1.0/eso/irspec'],
        "label": "D",
    },
    "eso_susi": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['eso-j-susi-3-rdr-sl9-v1.0/eso/susi'],
        "label": "D",
    },
    
    # Mount Stromlo Siding Spring Observatory
    # Mirrored at SBN and ATM
    "mssso_star": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['mssso-j-caspir-3-rdr-sl9-stds-v1.0/mssso/caspir'],
        "label": "D",
    },
    # CASPIR calibration is missing from the tiny_other manifest (as of 8/19/24)
    "mssso_cal": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['sl9_0004/mssso/caspir'],
        "label": "D",
    },
    
    # Okayama Astrophysical Observatory - OASIS images
    # (Mirrored at ATM; sl9_0001/oao)
    "oao": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['oao-j-oasis-3-rdr-sl9-v1.0/oao/oasis'],
        "label": "D",
    },
    
    # Hubble Space Telescope - WFPC2 images
    # Mirrored at SBN and ATM, and already covered by jup_sl9_impact in the hst 
    # selection rules.
    
    # International Ultraviolet Explorer - spectra
    # Already covered by sl9_raw and sl9_image in the iue selection rules.
    
    # Galileo Orbiter - subset of NIMS, PPR, SSI, and UVS data specific to the
    # SL9 impact. There may be overlap with a few products covered by the
    # Galileo specific selection rules, but most products appear to be unique.
    # (Mirrored at ATM; sl9_0001/galileo)
    "go_nims": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['go-j-nims-4-adr-sl9impact-v1.0/galileo/nims'],
        "label": "D",
    },
    "go_ppr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['go-j-ppr-3-edr-sl9-g_h_l_q1-v1.0/galileo/ppr'],
        "label": "D",
    },
    "go_uvs_edr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['go-j-uvs-2-edr-sl9-v1.0/galileo/uvs'],
        "label": "D",
    },
    "go_uvs_rdr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['go-j-uvs-3-rdr-sl9-g-fragment-v1.0/galileo/uvs'],
        "label": "D",
    },
    # The SSI IMAGE, IMAGE_HEADER, and TELEMETRY_TABLE pointers open fine.
    # The BAD_DATA_VALUES_HEADER might be opening correctly.
    # The LINE_PREFIX_TABLE is supported now.
    "go_ssi": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['go-j-ssi-2-redr-sl9-v1.0/galileo/ssi'],
        "label": "D",
    },

    # Files in the NOTES and CODE directories; no PDS labels
    # Volumes: ear-j_sa-hsotp-2-edr-sl9-v1.0 and ear-j_c-hsccd-3-rdr-sl9-v1.0
    "unsupported": {
        "manifest": SBN_FILE,
        "url_must_contain": ['ear-j'],
        "url_regex": [r'(NOTES)|(CODE)'],
        "support_np": True
    },
}

SKIP_FILES = ["vicar2.txt", "baddata.txt", "VICAR2.TXT", "BADDATA.TXT"]
