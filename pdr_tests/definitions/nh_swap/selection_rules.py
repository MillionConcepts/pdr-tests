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
SB_FILE = "tiny_new_horizons"

file_information = {
    
   # post-launch raw and calibrated data
   "launch_raw": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-swap-2-launch-v2.0/data'],
       "label": "D",
   },
   "launch_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-swap-3-launch-v2.0/data'],
       "label": "D",
   },
   # jupiter flyby raw and calibrated data
   "jupiter_raw": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-j-swap-2-jupiter-v4.0/data'],
       "label": "D",
   },
   "jupiter_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-j-swap-3-jupiter-v4.0/data'],
       "label": "D",
   },
   # pluto cruise raw and calibrated data
   "cruise_raw": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-swap-2-plutocruise-v3.0/data'],
       "label": "D",
   },
   "cruise_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-swap-3-plutocruise-v3.0/data'],
       "label": "D",
   },
   # pluto encounter raw and calibrated data
   "pluto_raw": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-p-swap-2-pluto-v3.0/data'],
       "label": "D",
   },
   "pluto_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-p-swap-3-pluto-v3.0/data'],
       "label": "D",
   },
   # solar wind derived characteristics
   # V2.0 of the dataset is missing from tiny_new_horizons (as of 4/16/24)
    "solar_wind": {
        "manifest": SB_FILE,
        "fn_must_contain": ['.csv'],
        "url_must_contain": ['nh-','-swap-5-derived-solarwind','data'],
        "label": "D",
    },

   # Extended mission products:
   # KEM Cruise 1 raw and calibrated data
   "kem_cruise_raw": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-swap-2-kemcruise1-v2.0/data'],
       "label": "D",
   },
   "kem_cruise_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-x-swap-3-kemcruise1-v2.0/data'],
       "label": "D",
   },
   # arrokoth encounter raw and calibrated data
   "arrokoth_raw": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-a-swap-2-kem1-v','.0/data'],
       "label": "D",
   },
   "arrokoth_cal": {
       "manifest": SB_FILE,
       "fn_must_contain": ['.fit'],
       "url_must_contain": ['nh-a-swap-3-kem1-v','.0/data'],
       "label": "D",
   },
}
