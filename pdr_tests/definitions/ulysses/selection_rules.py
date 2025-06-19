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
PPI_FILE = "plasm_full"
SBN_FILE = "tiny_sbnarchive"

file_information = {
    # dust detector subsystem
    "dds_data": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['ulyd', '.tab'],
        "url_must_contain": ['ulysses/ULY_D_UDDS_5_DUST_V3_1/data'],
        "label": "D",
    },
    "dds_sounder": {
        "manifest": SBN_FILE,
        "fn_must_contain": ['sounder', '.tab'],
        "url_must_contain": ['ulysses/ULY_D_UDDS_5_DUST_V3_1/data'],
        "label": "D",
    },
    # neutral gas experiment
    "gas": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-GAS-5-SKY-MAPS-V1.0/DATA'],
        "label": "D",
    },
    # solar x-ray/gamma-ray burst instrument
    "grb": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-GRB-2-RDR-RAW-COUNT-RATE-V1.0/DATA'],
        "label": "D",
    },
    # solar wind over poles of the sun
    "swoops": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-SWOOPS-5-RDR-PLASMA-HIRES-V1.0/DATA'],
        "label": "D",
    },
    # solar corona experiment
    "sce_rdr": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-SCE-3-RDR-DOPPLER-HIRES-V1.0/DATA'],
        "label": "D",
    },
    "sce_summ": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-SCE-4-SUMM-RANGING-10MIN-V1.0/DATA'],
        "label": "D",
    },
    "sce_rocc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.ODR'],
        "url_must_contain": ['ULY-J-SCE-1-ROCC-V1.0/DATA'],
        "label": "D",
    },
    "sce_tdf": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TDF'],
        "url_must_contain": ['ULY-J-SCE-1-TDF-V1.0/DATA'],
        "label": "D",
    },
    # magnetic field experiment (VHM/FGM)
    "mag": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-VHM_FGM-4-SUMM-JGCOORDS-60S-V1.0/DATA'],
        "label": "D",
    },
    # heliosphere spectra composition and anisotropy
    "hiscale": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-HISCALE-4-SUMM-', '/DATA'],
        "label": "D",
    },
    # cosmic ray and solar particle investigation
    "cospin_at": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-COSPIN-AT-4-FLUX-256SEC-V1.0/DATA'],
        "label": "D",
    },
    "cospin_het": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-COSPIN-HET-3-RDR-FLUX-HIRES-V1.0/DATA'],
        "label": "D",
    },
    "cospin_hft": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-COSPIN-HFT-3-RDR-FLUX-HIRES-V1.0/DATA'],
        "label": "D",
    },
    "cospin_ket_int": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-COSPIN-KET-3-RDR-INTENS-HIRES-V1.0/DATA'],
        "label": "D",
    },
    "cospin_ket_raw": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-COSPIN-KET-3-RDR-RAW-HIRES-V1.0/DATA'],
        "label": "D",
    },
    "cospin_let": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-COSPIN-LET-3-RDR-FLUX-32SEC-V1.0/DATA'],
        "label": "D",
    },
    # energetic particle composition
    "epac_all_chan": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-EPAC-4-SUMM-ALL-CHAN-1HR-V1.0/DATA'],
        "label": "D",
    },
    "epac_omni_ele": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-EPAC-4-SUMM-OMNI-ELE-FLUX-1HR-V1.0/DATA'],
        "label": "D",
    },
    "epac_omni_pro": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-EPAC-4-SUMM-OMNI-PRO-FLUX-1HR-V1.0/DATA'],
        "label": "D",
    },
    "epac_pha_asc": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-EPAC-4-SUMM-PHA-24HR-V1.0/DATA/ASCII'],
        "label": "D",
    },
    "epac_pha_bin": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.BIN'],
        "url_must_contain": ['ULY-J-EPAC-4-SUMM-PHA-24HR-V1.0/DATA/BINARY'],
        "label": "D",
    },
    "epac_prtl": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-EPAC-4-SUMM-PRTL','-FLUX-1HR-V1.0/DATA'],
        "label": "D",
    },
    "epac_pstl": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-EPAC-4-SUMM-PSTL','-FLUX-1HR-V1.0/DATA'],
        "label": "D",
    },
    # unified radio and plasma experiment
    "urap_pfr_avg": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-PFR-AVG-E-10MIN-V1.0/DATA'],
        "label": "D",
    },
    "urap_pfr_peak": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-PFR-PEAK-E-10MIN-V1.0/DATA'],
        "label": "D",
    },
    "urap_rar_avg_min": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-RAR-AVG-E-10MIN-V1.0/DATA'],
        "label": "D",
    },
    "urap_rar_avg_sec": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-RAR-AVG-E-144S-V1.0/DATA'],
        "label": "D",
    },
    "urap_rar_peak": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-RAR-PEAK-E-10MIN-V1.0/DATA'],
        "label": "D",
    },
    "urap_wfa_avg_b": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-WFA-AVG-B-10MIN-V1.0/DATA'],
        "label": "D",
    },
    "urap_wfa_avg_e": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-WFA-AVG-E-10MIN-V1.0/DATA'],
        "label": "D",
    },
    "urap_wfa_peak_b": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-WFA-PEAK-B-10MIN-V1.0/DATA'],
        "label": "D",
    },
    "urap_wfa_peak_e": {
        "manifest": PPI_FILE,
        "fn_must_contain": ['.TAB'],
        "url_must_contain": ['ULY-J-URAP-4-SUMM-WFA-PEAK-E-10MIN-V1.0/DATA'],
        "label": "D",
    },

    # Spice kernels - support not planned
    "spice": {
        "manifest": PPI_FILE,
        "fn_regex": [r'((LSK)|(PCK)|(XSP))$'],
        "url_must_contain": ['ULY-J-SCE-1-', '/GEOMETRY'],
        "label": "D",
        "support_np": True
    },
}
