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
    
    # Safed: Crommelin products (practice target)
    # Archived: Halley (primary target), GZ (practice target)
    #   - version 1.0 of the Halley products are not in tiny.parquet
    # In-progress: version 2.0 of several Halley datasets
    
    # AMSN - amateur observations
    # Drawing, Photography, and Spectroscopy products were never digitized.
    # Visual products are ascii tables with detached labels and FITs headers
    "am_vis": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-amvis-2-rdr-halley', 'data'],
        "label": "D",
    },
    
    # ASTR - astrometry
    # ascii text files
    "astr_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-astr-2-edr-gz', 'data'],
        "label": "D",
    },
    # Halley observations from the 1980s; ascii tables
    # Some products miscount the padding bytes in columns 3 and 5 of the table
    # "astr_halley": {
    #     "manifest": SBN_FILE,
    #     "fn_must_contain": ['.tab'],
    #     "url_must_contain": ['ihw-c-astr-2-edr-halley', 'data/1986'],
    #     "label": "D",
    # },
    # re-reduced Halley data from its 1835 and 1910 appearances
    "astr_historic": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-astr-2-edr-halley'],
        "url_regex": [r'(data/1835)|(data/1910)'],
        "label": "D",
    },
    
    # LSPN - large-scale phenomena
    "lsp_subsampled": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.ibg'],
        "url_must_contain": ['ihw-c-lspn-2-didr', 'data/subsampled'],
        "label": "D",
    },
    "lsp_v2": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ihw-c-lspn-2-didr-halley-v2.0/data'],
        "label": "D",
    },
    
    # MSN - meteor studies
    # This product type has 5-6 similar but slightly different table formats.
    "ms_radar": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-msnrdr-3-rdr', 'data'],
        "label": "D",
    },
    "ms_vis": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-msnvis-3-rdr', 'data'],
        "label": "D",
    },
    
    # NNSN - near nucles studies
    # GZ products (Halley v1.0 products aren't in the manifest)
    "nns_v1": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['ihw-c-nnsn-3-edr', 'data'],
        "label": "D",
    },
    # Halley addenda products (most Halley v2.0 products aren't in the manifest)
    "nns_v2": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ihw-c-nnsn-3-edr-halley', 'data'],
        "label": "D",
    },
    
    # SSN - spectroscopy and spectrophotometry
    "spec_gz_didr": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-spec-2-didr-gz', 'data'],
        "label": "D",
    },
    "spec_hal_raw_img": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['ihw-c-spec-2-edr-halley', 'data'],
        "label": "D",
    },
    "spec_hal_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-spec-3-edr-halley', 'data'],
        "label": "D",
    },
    "spec_hal_didr_img": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['spec4', '.img'],
        "url_must_contain": ['ihw-c-spec-3-didr-halley', 'data'],
        "label": "D",
    },
    # # SPECTRAL_IMAGE_QUBE pointer does not open
    # "spec_hal_raw_dat": {
    #     "manifest": SBN_FILE,
    #     "fn_must_contain": ['.dat'],
    #     "url_must_contain": ['ihw-c-spec-2-edr-halley', 'data'],
    #     "label": "D",
    # },
    # # SPECTRAL_IMAGE_QUBE pointer does not open.
    # # Products with a SPECTRUM pointer do open.
    # "spec_hal_didr_dat": {
    #     "manifest": SBN_FILE,
    #     "fn_must_contain": ['.dat'],
    #     "url_must_contain": ['ihw-c-spec-3-didr-halley', 'data'],
    #     "label": "D",
    # },

    # Earth-based CCD observations of Halley outburst
    "ccd_outburst": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ear-c-ccd-3-edr-halley-outburst', 'data'],
        "label": "D",
    },
    # derived flux (3 products, but they're copies of the same table)
    "ccd_flux": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ear-c-ccd-3-edr-halley-outburst', 'data'],
        "label": "D",
    },
    # ascii log file
    "ccd_log": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.asc'],
        "url_must_contain": ['ear-c-ccd-3-edr-halley-outburst', 'data'],
        "label": "D",
    },

    # Most GZ products have incomplete PDS3 labels (support not planned)
    "spec_gz_raw": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-spec-2-edr-gz', 'data'],
        "label": "D",
        "support_np": True
    },
    "spec_gz_cal": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['ihw-c-spec-3-edr-gz', 'data'],
        "label": "D",
        "support_np": True
    },
    "am_vis_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c-amvis-2-rdr-gz', 'data'],
        "label": "D",
        "support_np": True
    },
    "lsp_gz_uncompressed": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['ihw-c-lspn-2-didr-gz', 'data/uncompressed'],
        "label": "A", # no PDS labels
        "support_np": True # notionally supported
    },
    # Compressed GZ and Halley v1.0 images are not supported. Some images open
    # incorrectly as all static, others do not open at all.
    "lsp_compressed": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.imq'],
        "url_must_contain": ['ihw-c-lspn-2-didr', 'data/compressed'],
        "label": "D",
        "support_np": True
    },
    # Null-data headers for products that were never digitized
    "null_data": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.hdr'],
        "url_must_contain": ['ihw-c-','-n-ndr-', 'data'],
        "label": "D",
        "support_np": True
    },

    # Geometry files
    "geom_gz": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c','-gz', 'geometry'],
        "label": "A", # no PDS labels
        "support_np": True # safed dataset
    },
    "geom_ephem": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['ephemeris.tab'],
        "url_must_contain": ['ihw-c','-halley', 'geometry/ephem'],
        "label": "D",
    },
    "geom_ephem_old": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['ephem.tab'],
        "url_must_contain": ['ihw-c','-halley', 'geometry/ephem'],
        "label": "A", # no PDS labels
        "support_np": True
    },
    # No newlines in the data files. Very very low priority for a special case 
    # (only v1.0 of the Halley datasets have geometry directories, they are not 
    # included in the updated v2.0 datasets)
    "geom_hist": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['ihw-c','-halley', 'geometry/ast_hist'],
        "label": "D",
        "support_np": True
    },

}
"""
Update 11/11/24:
It looks like these broken products were removed from SBN.

    # The filename extensions do not match the pointers in their labels.
    "spec_hal_didr_typo": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['.img'],
        "fn_regex": [r'spec[12]'],
        "url_must_contain": ['ihw-c-spec-3-didr-halley', 'data'],
        "label": "D",
    },
"""
