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
ATM_FILE = "atm"

file_information = {
	
    # AEROSOL COLLECTOR PYROLYSER
    "acp": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['ACP', '.TAB'],
        "url_must_contain": ['hpacp', 'DATA'],
        "label": "D",
    },
    
    # GAS CHROMATOGRAPH MASS SPECTROMETER
    # (some products are duplicated in the ACP directory)
	"gcms": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['GCMS', '.TAB'],
        "url_must_contain": ['hpgcms', 'DATA'],
        "label": "D",
    },
    
    
# DISR instument
    # dark data
    "dark": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['DARK', '.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA'],
        "label": "D",
    },
    # derived data products: ir, violet, and vis
    "ddr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA/DERIVED_DATA_PRODUCTS'],
        "label": "D",
    },
    # combined descent cycles, housekeeping, and lamp --> all txt files
    "misc_img_text": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TXT'],
        "url_must_contain": ['hpdisr_0001/DATA'],
        "url_regex": [r'(DESCENT)|(HOUSEKEEPING)|(LAMP)'],
        "label": "D",
    },    
    # imager; 3 formats
    "img_table": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['IMAGE', '.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA', 'TABLE_FORMAT'],
        "label": "D",
    },
    "img_tiff": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['TIFIMG', '.TIF'],
        "url_must_contain": ['hpdisr_0001/DATA', 'TIFF_FORMAT'],
        "label": "D",
    },
    "img_xdr": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['XDRIMG', '.XDR'],
        "url_must_contain": ['hpdisr_0001/DATA', 'XDR_FORMAT'],
        "label": "D",
    },
    # IR spectrometer (data format is hugely problematic; low priority support planned)
    # "ir": {
    #     "manifest": ATM_FILE,
    #     "fn_must_contain": ['IR', '.TAB'],
    #     "url_must_contain": ['hpdisr_0001/DATA/IR_SPECTROMETER'],
    #     "label": "D",
    # },
    # Side Looking Imager (SLI), sum of 2 strips
    "strip": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA/SLI_STRIP'],
        "label": "D",
    },
    # Solar Aureole Cameras
    "solar": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['SOLAR', '.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA/SOLAR'],
        "label": "D",
    },
    # Sun Sensor
    "sun": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['SUN', '.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA/SUN'],
        "label": "D",
    },
    # Time
    "time": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['TIME', '.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA/TIME'],
        "label": "D",
    },
    # Violet Photometers
    "violet": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['VIOLET', '.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA/VIOLET'],
        "label": "D",
    },
    # visible wavelength spectrometer extra columns
    "vis_extra": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['VIS_EX', '.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA/VISIBLE_EXTRA_COLUMNS'],
        "label": "D",
    },
    # VIS spectrometer
    "vis": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['VISIBL', '.TAB'],
        "url_must_contain": ['hpdisr_0001/DATA/VISIBLE_SPECTROMETER'],
        "label": "D",
    },
    
    
    # entry and descent trajectory data (reconstructed)
    "trajectory": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['hpdtwg', 'DATA'],
        "label": "D",
    },
    
    # doppler wind experiment
    "dwe": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['hpdwe', 'DATA'],
        "label": "D",
    },
    
# HASI instrument
    # Accelerometer sensor subsystem
    "hasi_acc": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['_ACC','.TAB'],
        "url_must_contain": ['hphasi', 'DATA'],
        "label": "D",
    },
    # Pressure Profile Instrument 
    "hasi_ppi": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['_PPI', '.TAB'],
        "url_must_contain": ['hphasi', 'DATA/PPI'],
        "label": "D",
    },
    # Permittivity, Wave and Altimetry package 
    "hasi_pwa": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['_PWA', '.TAB'],
        "url_must_contain": ['hphasi', 'DATA'],
        "label": "D",
    },
    # Temperature sensors
    "hasi_tem": {
        "manifest": ATM_FILE,
        "fn_regex": [r'_TEM[DS_].*\.TAB'],
        "url_must_contain": ['hphasi', 'DATA'],
        "label": "D",
    },
    # Data Processing Unit Subsystem
    "hasi_dpu": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['_DPU', '.TAB'],
        "url_must_contain": ['hphasi', 'DATA'],
        "label": "D",
    },
    # derived profiles
    "hasi_prof": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['hphasi', 'DATA/PROFILES'],
        "label": "D",
    },
    
    
    # general probe housekeeping data
    "hsk": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['hphk', 'DATA'],
        "label": "D",
    },
    
    # surface science package
    "ssp": {
        "manifest": ATM_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['hpssp', 'DATA'],
        "label": "D",
    },
    
}
