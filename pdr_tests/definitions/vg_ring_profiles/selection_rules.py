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
RMS_FILE = "ringvolumes"

file_information = {
    
    # vg_2810 - Saturn ring profiles derived from ISS data
    # Profile generated from a sequence of images
    "iss_multi": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG_28xx/VG_2810'],
        "url_regex": [r'DATA$'],
        "label": "D",
    },
    # Profile generated from a single image
    "iss_single": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['SCAN.TAB'],
        "url_must_contain": ['VG_28xx/VG_2810/DATA'],
        "label": "D",
    },
    # ISS images in tiff format (raw, calibrated/de-distorted, and annotated)
    "iss_tiff": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TIF'],
        "url_must_contain": ['VG_28xx/VG_2810/DATA'],
        "label": "D",
    },
    # Additional images (.IMG) in this dataset are duplicates of images included
    # in the vg_iss selection rules.
    # Compressed EDR images (.IMQ) are known unsupported, support not planned.
    
    
    # vg_2801 - Saturn/Uranus/Neptune PPS ring profiles
    # resampled, calibrated profiles
    "pps_resample": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG_28xx/VG_2801/EASYDATA'],
        "label": "D",
    },
    # edited data
    "pps_edited": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2801/EDITDATA'],
        "label": "D",
    },
    # noise data
    "pps_noise": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2801/NOISDATA'],
        "label": "D",
    },
    # raw data
    "pps_raw": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2801/RAWDATA'],
        "label": "D",
    },
    # Ancillary products: FOV maps, calibration models, geometry, jitter,
    # trajectory, and vector files. Source data files are safed.
    
    
    # vg_2802 - Saturn/Uranus/Neptune UVS ring profiles
    # calibrated profiles, resampled by filter and resolution
    "uvs_resample": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG_28xx/VG_2802/EASYDATA'],
        "label": "D",
    },
    # edited data
    "uvs_edited": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2802/EDITDATA'],
        "label": "D",
    },
    # noise data
    "uvs_noise": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2802/NOISDATA'],
        "label": "D",
    },
    # raw data
    # There are 3 versions of each product: IEEE, PC, and VAX formats. The VAX
    # tables do not open (as of 11/7/23).
    "uvs_raw": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2802/RAWDATA'],
        "label": "D",
    },
    # Ancillary products: calibration models, geometry, trajectory, and vector
    # files. Source data files are safed.
    # Image products (.IMG) in this dataset are duplicates of images included
    # in the vg_iss selection rules.
    
    
    # vg_2803 - Saturn/Uranus radio occultation ring profiles
    # resampled, calibrated profiles
    "rocc_resample": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG_28xx/VG_2803/','RINGS/EASYDATA'],
        "label": "D",
    },
    # edited data
    # There are 3 versions of each product: IEEE, PC, and VAX formats. The VAX
    # tables do not open (as of 11/7/23).
    "rocc_edited": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2803/','RINGS/EDITDATA'],
        "label": "D",
    },
    # low-level saturn data, converted from source files
    # There are 3 versions of each product: IEEE, PC, and VAX formats. The VAX
    # tables do not open (as of 11/7/23).
    "rocc_low_sat": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2803/S_RINGS/LOWDATA'],
        "label": "D",
    },
    # low-level saturn data, simulated data
    "rocc_low_sim": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG_28xx/VG_2803/S_RINGS/LOWDATA'],
        "label": "D",
    },
    # low-level uranus data, converted from source files
    "rocc_low_ur": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['VG_28xx/VG_2803/U_RINGS/LOWDATA'],
        "label": "D",
    },
    # Ancillary products: calibration models and geometry files. Source
    # data files are safed.


    # Safed source data files
    "source_pps": {
        "manifest": RMS_FILE,
        "fn_regex": [r'(DAT$)|(GS3$)|(SCO$)|(SGR$)|(LIS$)'],
        "url_must_contain": ['VG_28xx/VG_2801/SORCDATA'],
        "label": "D",
    },
    "source_uvs": {
        "manifest": RMS_FILE,
        "fn_regex": [r'(VOY$)|(TAB$)'],
        "url_must_contain": ['VG_28xx/VG_2802/SORCDATA'],
        "label": "D",
    },
    # Safed ptypes that do not open; support not planned
    "source_rss": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.DAT'],
        "url_must_contain": ['VG_28xx/VG_2803', '/SORCDATA'],
        "label": "D",
        "support_np": True
    },
    "source_iss": {
        "manifest": RMS_FILE,
        "fn_must_contain": ['.IMQ'],
        "url_must_contain": ['VG_28xx/VG_2810', '/SOURCE'],
        "label": "A",
        "support_np": True
    },
}

