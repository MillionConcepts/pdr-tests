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
MANIFEST_FILE = "geoearth"

file_information = {
    
    # Airborne Data Sets
    # ASAS
    "asas": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['earth/grsfe', 'asas'],
        "label": "D",
    },
    # AVIRIS
    "aviris_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['earth/grsfe', 'aviris'],
        "label": "D",
    },
    # TIMS
    "tims_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['earth/grsfe', 'tims'],
        "label": "D",
    },
    
    # Field Data Sets    
    # GPS Satellite Profiles
    "gps": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['earth/grsfe', 'gpsmicro'],
        "label": "D",
    },
    # Helicopter-Borne Stereophotography Profiles
    "heli_stereo": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['earth/grsfe', 'helprfl'],
        "label": "D",
    },
    # Spectral Hygrometer
    "spect_hygro": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['earth/grsfe', 'hygromtr'],
        "label": "D",
    },
    # PARABOLA
    "parabola": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['parabola'],
        "label": "D",
    },
    # PFES - Portable Field Emission Spectrometer
    "pfes": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['earth/grsfe', 'pfes'],
        "label": "D",
    },
    # Reagan Radiometer
    "reag_rad": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.'],
        "url_must_contain": ['earth/grsfe', 'reagrad'],
        "label": "D",
    },
    # Wind Experiment
    "wind": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['earth/grsfe', 'windexp'],
        "label": "D",
    },
    # Weather Station
    "weather": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.tab'],
        "url_must_contain": ['earth/grsfe', 'wthrsta'],
        "label": "D",
    },
    # VAX_REAL tables:
    "aviris_dat": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['earth/grsfe', 'aviris'],
        "label": "D",
    },
    "tims_dat": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['earth/grsfe', 'tims'],
        "label": "D",
    },
}

"""
Products missing/incomplete/wrong labels:
    # airborne data locator maps (appear to be ancillary)
    # SAMPLE_TYPE = BYTE should probably be VAX_INTEGER
    "locator": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img'],
        "url_must_contain": ['earth/grsfe', 'locator'],
        "label": "D",
    },
    # Daedalus Spectrometer
    # SPECTRUM does not open; it's defined wrong in the label.
    # SPECTRUM_HEADER fails because ReadTable is called instead of ReadHeader 
    "daedalus": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['earth/grsfe', 'daedalus'],
        "label": "D",
    },
    # Directional Emissivity Experiment - text files with no labels

Mistakes in data files:
    # SIRIS Spectrometer
    # Something is broken in these products' data files 
    "siris": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.dat'],
        "url_must_contain": ['earth/grsfe', 'siris'],
        "label": "D",
    },

Compressed images:
    "airsar": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.imq'],
        "url_must_contain": ['earth/grsfe', 'airsar'],
        "label": "D",
    },
"""
