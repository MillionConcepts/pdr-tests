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
MANIFEST_FILE = "jaxa_sln"
MANIFEST_FILE_TC_2B = "jaxa_sln_tc_2b"
MANIFEST_FILE_TC = "jaxa_sln_tc_no_2b"

file_information = {
    # TEX: extreme ultraviolet telescope
    "texi_images": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['.img','texi_'],
        "url_must_contain": ['sln','tex-5-plasmasphere','data'],
        "label": "D",
    },
    # TVIS: telescope of visible light
    "tvis_2a_images": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['tvis_', '.img'],
        "url_must_contain": ['sln', 'level2a-v1.0', 'data'],
        "label": "D",
    },
    # ARD: alpha ray detector
    # these are big files!
    "ard_tables": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['ARD_', '.TAB'],
        "url_must_contain": ['sln', 'sln-l-ard-4-event-v1.0', 'data'],
        "label": ('.TAB', '.lbl'),
    },
    # GRS: gamma ray spectrometer
    "grs_eng_tables": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['GRS_ESPEC2_', '.tbl'],
        "url_must_contain": ['sln', 'sln-l-grs-3-eng-spectrum-v1.0', 'data'],
        "label": "D",
    },
    # different maps for Al, Ca, Fe, K, Mg, O, Si, Th, Ti, U
    "grs_map": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['GRS_IMAP_', '.img'],
        "url_must_contain": ['sln', 'sln-l-grs-5-gamma-ray-map-v1.0', 'data'],
        "label": "D",
    },
    # Nuclide maps for Ca, K, Th, U
    "grs_nmap": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['GRS_NMAP_', '.img'],
        "url_must_contain": ['sln', 'sln-l-grs-5-nuclide-map', 'data'],
        "label": "D",
    },
    # some V2.0 nuclide maps are tables?
    "grs_nmap_tables": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['GRS_NMAP_', '.tab'],
        "url_must_contain": ['sln', 'sln-l-grs-5-nuclide-map-v2.0', 'data'],
        "label": "D",
    },
    # LALT: lase altimeter
    "lalt_rd_tables": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_RD', '.TAB'],
        "url_must_contain": ['sln', 'sln-l-lalt-3-range-v1.0', 'data'],
        "label": "D",
    },
    # laser altimeter time series topographic data
    "lalt_topo_tables": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_LGT_TS', '.TAB'],
        "url_must_contain": ['sln', 'sln-l-lalt-4-topo-lgt-ts-v2.0', 'data'],
        "label": "D",
    },
    # LALT spherical harmonics of topography (1 table)
    "lalt_sh_table": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_SH', '.TAB'],
        "url_must_contain": ['sln', 'sln-l-lalt-5-sht-coef-v2.0', 'data'],
        "label": "D",
    },
    # one map image file
    "lalt_ggt_map": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_GGT', '.IMG'],
        "url_must_contain": ['sln', 'sln-l-lalt-5-topo-ggt-map-v2.0', 'data'],
        "label": "D",
    },
    # one table file
    "lalt_ggt_num": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_GGT_NUM', '.TAB'],
        "url_must_contain": ['sln', 'sln-l-lalt-5-topo-ggt-num-v2.0', 'data'],
        "label": "D",
    },
    "lalt_gt_np_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_GT_NP_IMG', '.IMG'],
        "url_must_contain": ['sln', 'sln-l-lalt-5-topo-gt-np-img-v2.0', 'data'],
        "label": "D",
    },
    "lalt_gt_np_num_tab": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_GT_NP_NUM', '.TAB'],
        "url_must_contain": ['sln', 'sln-l-lalt-5-topo-gt-np-num-v2.0',
                             'data'],
        "label": "D",
    },
    "lalt_gt_sp_img": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_GT_SP_IMG', '.IMG'],
        "url_must_contain": ['sln', 'sln-l-lalt-5-topo-gt-sp-img-v2.0',
                             'data'],
        "label": "D",
    },
    "lalt_gt_sp_num_tab": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LALT_GT_SP_NUM', '.TAB'],
        "url_must_contain": ['sln', 'sln-l-lalt-5-topo-gt-sp-num-v2.0',
                             'data'],
        "label": "D",
    },
    # Magnetic field time series from LMAG
    # has an "optional" and a "nominal" folder but seem to have the same format
    "mag_ts_table": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MAG_TSOP', '.dat'],
        "url_must_contain": ['sln', 'sln-l-lmag-3-mag-ts-v1.0',
                             'data'],
        "label": "D",
    },
    # 1d sigma constraints on the electrical conductivity structure
    "mag_sigma_table": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['1DSigma', '.dat'],
        "url_must_contain": ['sln', 'sln-l-lmag-5-1d-sigma-ecs-v1.0',
                             'data'],
        "label": "D",
    },
    "mag_grid_option": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MA_GDOP', '.dat'],
        "url_must_contain": ['sln', 'sln-l-lmag-5-ma-grid-option-v1.0',
                             'data'],
        "label": "D",
    },
    "mag_grid_tables": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MA_GD', '.dat'],
        "url_must_contain": ['sln', 'sln-l-lmag-5-ma-grid-v1.0',
                             'data'],
        "label": "D",
    },
    "mag_map_opt": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MA_MAPOP', '.img'],
        "url_must_contain": ['sln', 'sln-l-lmag-5-ma-map-option-v1.0',
                             'data'],
        "label": "D",
    },
    "mag_map_image": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MA_MAP', '.img'],
        "url_must_contain": ['sln', 'sln-l-lmag-5-ma-map-v1.0',
                             'data'],
        "label": "D",
    },
    # LRS: Lunar Radar Sounder
    "sndr_waveform_high": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SW_WF', '.tbl'],
        "url_must_contain": ['sln', 'sln-l-lrs-2-sndr-waveform-high-v1.0',
                             'data'],
        "label": "D",
    },
    "sndr_waveform_low": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SA_WF', '.tbl'],
        "url_must_contain": ['sln', 'sln-l-lrs-2-sndr-waveform-low-v1.0',
                             'data'],
        "label": "D",
    },
    # LRS spectra are in CDF (Common Data Format) format
    # and do not have labels because of that?
    # CDF is not supported by PDR.
    # "lrs_wfc_spectrum": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['LRS_WFC_', '.cdf'],
    #     "url_must_contain": ['sln', 'sln-l-lrs-4-wfc-spectrum-v1.0',
    #                          'data'],
    #     "label": "A",
    # },
    # "lrs_npw_spectrum": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['LRS_NPW_', '.cdf'],
    #     "url_must_contain": ['sln', 'sln-l-lrs-5-npw-spectrum-v1.0',
    #                          'data'],
    #     "label": "A",
    # },
    "sndr_gsi_map": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_GEO_', '.img'],
        "url_must_contain": ['sln', 'sln-l-lrs-5-sndr-gsi-map-v1.0',
                             'data'],
        "label": "D",
    },
    "sndr_ss_high": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SWH_RV', '.img'],
        "url_must_contain": ['sln', 'sln-l-lrs-5-sndr-ss-high-v2.0',
                             'data'],
        "label": "D",
    },
    "sndr_ss_low": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SAL_RV', '.img'],
        "url_must_contain": ['sln', 'sln-l-lrs-5-sndr-ss-low-v1.0',
                             'data'],
        "label": "D",
    },
    # sounder subsurface SAR 5 km complex
    "sndr_ss_sar05_complex": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SAR05KM', '.tbl'],
        "url_must_contain": ['sln', 'sln-l-lrs-5-sndr-ss-sar05-complex-v1.0',
                             'data'],
        "label": "D",
    },
    "sndr_ss_sar05_power": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SAR05KM', '.img'],
        "url_must_contain": ['sln', 'sln-l-lrs-5-sndr-ss-sar05-power-v1.0',
                             'data'],
        "label": "D",
    },
    "sndr_ss_sar10_complex": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SAR10KM', '.tbl'],
        "url_must_contain": ['sln', 'sln-l-lrs-5-sndr-ss-sar10-complex-v1.0',
                             'data'],
        "label": "D",
    },
    "sndr_ss_sar10_power": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SAR10KM', '.img'],
        "url_must_contain": ['sln', 'sln-l-lrs-5-sndr-ss-sar10-power-v1.0',
                             'data'],
        "label": "D",
    },
    "sndr_ss_sar40_power": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['LRS_SAR40KM', '.img'],
        "url_must_contain": ['sln', 'sln-l-lrs-5-sndr-ss-sar40-power-v1.0',
                             'data'],
        "label": "D",
    },
    # NIR level 2B2
    "MNA_NIR_2B2_01": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MNA_2B2', '.img.gz'],
        "url_must_contain": ['sln', 'sln-l-mi-3-nir-level2b2-v1.0',
                             'data'],
        "label": ('.img.gz', '.lbl'),
    },
    "MVA_VIS_2B2_01": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MVA_2B2', '.img.gz'],
        "url_must_contain": ['sln', 'sln-l-mi-3-vis-level2b2-v1.0',
                             'data'],
        "label": ('.img.gz', '.lbl'),
    },
    "MIA_3C5_03": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MIA_3C5_03', '.img.gz'],
        "url_must_contain": ['sln', 'sln-l-mi-4-level3c5-v3.0',
                             'data'],
        "label": ('.img.gz', '.lbl'),
    },
    "MNA_NIR_2C2_01": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MNA_2C2', '.img.gz'],
        "url_must_contain": ['sln', 'sln-l-mi-4-nir-level2c2-v1.0',
                             'data'],
        "label": ('.img.gz', '.lbl'),
    },
    "MVA_VIS_2C2_01": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MVA_2C2', '.img.gz'],
        "url_must_contain": ['sln', 'sln-l-mi-4-vis-level2c2-v1.0',
                             'data'],
        "label": ('.img.gz', '.lbl'),
    },
    "MI_MAP": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['MI_MAP_03', '.img'],
        "url_must_contain": ['sln', 'sln-l-mi-5-map-v3.0',
                             'data'],
        "label": "D",
    },
    "IPACE_PBF1": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['IPACE_PBF1', '.dat.gz'],
        "url_must_contain": ['sln', 'sln-l-pace-3-pbf1-v3.0',
                             'data'],
        "label": ('.dat.gz', '.lbl'),
    },
    "PACE_ET1": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['PACE_ET1', '.png'],
        "url_must_contain": ['sln', 'sln-l-pace-5-et-summary-v1.0',
                             'data'],
        "label": "D",
    },
    # Relay satellite stuff
    # much of RISE is in GEODYN format not supported by PDR
    # "RISE_SRV": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['SRV_', '.bin'],
    #     "url_must_contain": ['sln', 'sln-l-rise-3-dvlbi-1wr-v1.0',
    #                          'data'],
    #     "label": "D",
    # },
    # "RISE_GRAV_COEF": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['SGM', 'coef', '.txt'],
    #     "url_must_contain": ['sln', 'sln-l-rise-5-grav-coef-v1.0',
    #                          'data'],
    #     "label": "D",
    # },
    # "RISE_GRAV_COV": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['SGM', 'cov', '.bin'],
    #     "url_must_contain": ['sln', 'sln-l-rise-5-grav-cov-v1.0',
    #                          'data'],
    #     "label": "D",
    # },
    # "RISE_GRAV_INFO": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['SGM', 'info', '.txt'],
    #     "url_must_contain": ['sln', 'sln-l-rise-5-grav-info-v1.0',
    #                          'data'],
    #     "label": "D",
    # },
    "RISE_GRAV_MAP": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['SGM', 'map', '.img'],
        "url_must_contain": ['sln', 'sln-l-rise-5-grav-map-v1.0',
                             'data'],
        "label": "D",
    },
    # GEODYN format not supported by PDR
    # "RISE_GRAV_POWER": {
    #     "manifest": MANIFEST_FILE,
    #     "fn_must_contain": ['SGM', 'power', '.ps'],
    #     "url_must_contain": ['sln', 'sln-l-rise-5-grav-power-v1.0',
    #                          'data'],
    #     "label": "D",
    # },
    "RISE_TRAJ": {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['TR_', '_SGM', '.txt'],
        "url_must_contain": ['sln', 'sln-l-rise-5-traj-',
                             'data'],
        "label": "D",
    },
    'ELECTRON_COLUMN_DENSITY': {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['RS', '.TAB'],
        "url_must_contain": ['sln', 'rs-5-electron-column-density',
                             'data'],
        "label": "D",
    },
    # spectral profiler reflectance spectrometer
    'sp_2b1': {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['SP_2B1', '.spc'],
        "url_must_contain": ['sln', 'sln-l-sp-3-level2b1-v2.0',
                             'data'],
        "label": "D",
    },
    'sp_2b2': {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['SP_2B2', '.spc'],
        "url_must_contain": ['sln', 'sln-l-sp-4-level2b2-v2.0',
                             'data'],
        "label": "D",
    },
    'sp_2c': {
        "manifest": MANIFEST_FILE,
        "fn_must_contain": ['SP_2C', '.spc'],
        "url_must_contain": ['sln', 'sln-l-sp-4-level2c-v3.0',
                             'data'],
        "label": "D",
    },
    # # terrain camera
    'tc_level2b': {
        "manifest": MANIFEST_FILE_TC_2B,
        "fn_must_contain": ['TC', '.img.gz'],
        "url_must_contain": ['sln', 'sln-l-tc-3-', 'level2b0',
                             'data'],
        "label": ('.img.gz', '.lbl'),
    },
    'tc_dem_ortho_v1_dqa': {
        "manifest": MANIFEST_FILE_TC,
        "fn_must_contain": ['DTMTCO', '.img', 'dqa'],
        "url_must_contain": ['sln', 'sln-l-tc-4-dem-ortho-v1.0',
                             'data'],
        "label": ('.img', '.lbl'),
    },
    'tc_dem_ortho_v1_dtm': {
        "manifest": MANIFEST_FILE_TC,
        "fn_must_contain": ['DTMTCO', '.img', 'dtm'],
        "url_must_contain": ['sln', 'sln-l-tc-4-dem-ortho-v1.0',
                             'data'],
        "label": ('.img', '.lbl'),
    },
    'tc_dem_ortho_v1_img': {
        "manifest": MANIFEST_FILE_TC,
        "fn_must_contain": ['DTMTCO', '.img', '_img'],
        "url_must_contain": ['sln', 'sln-l-tc-4-dem-ortho-v1.0',
                             'data'],
        "label": (r'\.img', '.lbl'),
    },
    # not captured by scraping?
    # 'tc_dem_ortho_v3_dqa': {
    #     "manifest": MANIFEST_FILE_TC,
    #     "fn_must_contain": ['DTMTCO', '.img', 'dqa'],
    #     "url_must_contain": ['sln', 'sln-l-tc-4-dem-ortho-v3.0',
    #                          'data'],
    #     "label": "D",
    # },
    # 'tc_dem_ortho_v3_dtm': {
    #     "manifest": MANIFEST_FILE_TC,
    #     "fn_must_contain": ['DTMTCO', '.img', 'dtm'],
    #     "url_must_contain": ['sln', 'sln-l-tc-4-dem-ortho-v3.0',
    #                          'data'],
    #     "label": "D",
    # },
    # 'tc_dem_ortho_v3_img': {
    #     "manifest": MANIFEST_FILE_TC,
    #     "fn_must_contain": ['DTMTCO', '.img', 'img'],
    #     "url_must_contain": ['sln', 'sln-l-tc-4-dem-ortho-v3.0',
    #                          'data'],
    #     "label": "D",
    # },
    'tc_dtm_map_seamless': {
        "manifest": MANIFEST_FILE_TC,
        "fn_must_contain": ['DTM_MAP', '.img'],
        "url_must_contain": ['sln', 'sln-l-tc-5-dtm-map-seamless',
                             'data'],
        "label": ('.img', '.lbl'),
    },
    'tc_dtm_map': {
        "manifest": MANIFEST_FILE_TC,
        "fn_must_contain": ['DTM_MAP_', '.img'],
        "url_must_contain": ['sln', 'sln-l-tc-5-dtm-map-v2.0',
                             'data'],
        "label": ('.img', '.lbl'),
    },
    # one off products
    # 'tc_evening_map': {
    #     "manifest": MANIFEST_FILE_TC,
    #     "fn_must_contain": ['TCO_MAPe04', '.img'],
    #     "url_must_contain": ['sln', 'evening',
    #                          'data'],
    #     "label": "D",
    # },
    # 'tc_morning_map': {
    #     "manifest": MANIFEST_FILE_TC,
    #     "fn_must_contain": ['TCO_MAPe04', '.img'],
    #     "url_must_contain": ['sln', 'morning',
    #                          'data'],
    #     "label": "D",
    # },
    # 'tc_ortho_map_seamless': {
    #     "manifest": MANIFEST_FILE_TC,
    #     "fn_must_contain": ['TCO_MAPs02', '.img'],
    #     "url_must_contain": ['sln', 'tc-5-ortho-map-seamless',
    #                          'data'],
    #     "label": "D",
    # },
    # 'tc_ortho_map': {
    #     "manifest": MANIFEST_FILE_TC,
    #     "fn_must_contain": ['TCO_MAPs02', '.img'],
    #     "url_must_contain": ['sln', 'tc-5-ortho-map-v2.0',
    #                          'data'],
    #     "label": "D",
    # },
    # 'tc_sldem': {
    #     "manifest": MANIFEST_FILE_TC,
    #     "fn_must_contain": ['DTM_MAP', '.img'],
    #     "url_must_contain": ['sln', 'tc-5-sldem2013',
    #                          'data'],
    #     "label": "D",
    # },
    # there is also a folder of stills from kaguya television that was used
    # for educational purposes. I haven't included that. They are fits files.
}
    

