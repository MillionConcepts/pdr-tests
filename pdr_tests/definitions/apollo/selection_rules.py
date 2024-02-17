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
LUNAR_FILE = "geolunar"
IMG_FILE = "img_usgs"

# note: most of these tables are not easy to validate -- technically L1 but
# lots of mysterious numbers read straight off cybernetic-era instrumentation.
# bottom line is that the formatting looks sane.

file_information = {
    # Apollo 12 ALSEP Solar Wind Spectrometer Plasma data.
    # one directory of L1-ish data from '69 to '76,
    # with gaps during lunar night. reformatted by NSSDC
    # in 2007. flat ASCII tables with slightly weird headers.
    # PDR's insertion of label format content is very nice here
    # because the in-table column headers are just numerical indices.
    "A12_SWS": {
        "manifest": LUNAR_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['a12sw_0001', 'data'],
        "label": "D",
    },
    # A15 ALSEP 1-hour-resolution Solar Wind Spectrometer 
    # Plasma data. same basic format as A12_SWS. '71-'72.
    "A15_SWS_1h": {
        "manifest": LUNAR_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['a15sw_0002', 'data'],
        "label": "D",
    },
    # 28-second resolution version of previous. same format,
    # but more of it.
    "A15_SWS_28s": {
        "manifest": LUNAR_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['a15sw_0001', 'data'],
        "label": "D",
    },
    # More David Williams / NSSDC late-00s reformatted Apollo sets.
    # a ~week of x-ray spectrometry data collected from orbit. lots of
    # mysterious numbers, but fundamentally just four flat ASCII files.
    # A15 and A16 formats are identical.
    "A15_16_XRFS": {
        "manifest": LUNAR_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['xr_0001', 'data'],
        "label": "D",
    },
    # atmospheric density plots directly scanned from microfiche and left as
    # image files. format is identical between the a14 and a15 sets. the
    # 'data' files here are indices; the TIF files under 'document' are the
    # actual plots. although they're indices, I'm adding support because
    # they're in a data tree and contain essential metadata for the data in
    # 'documents'; although the data are basically structured like browse
    # images, they're data, so I'm adding support for them too. confusing!
    "A14_15_CCIG_index": {
        "manifest": LUNAR_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['ccg_000', 'data'],
        "label": "D",
    },
    "A14_15_CCIG_plot": {
        "manifest": LUNAR_FILE,
        "fn_must_contain": [".tif"],
        "url_must_contain": ['ccg_000', 'document'],
        "label": "D",
    },
    # 4-band (453/550/751/952 nm) BRDFs for 6 Apollo soil samples, produced
    # in the 00s. Simple ASCII CSV, well-labeled by GEO personnel.
    "BUG": {
        "manifest": LUNAR_FILE,
        "fn_must_contain": [".csv"],
        "url_must_contain": ['bug_9002', 'data'],
        "label": "D",
    },
    # hand-typed reproductions of handwritten charts made from
    # the raw data of Earth-returned penetrometer drums + LSRP Soil Mechanics
    # runs, presented as flat ASCII tables. photographs of the charts are also
    # included, but these tables appear to contain all the "science" content
    # of the charts. format is almost identical between A15 and A16.
    "A15_16_SMSS": {
        "manifest": LUNAR_FILE,
        "fn_must_contain": [".tab"],
        "url_must_contain": ['sm_000', 'data'],
        "label": "D",
    },
    # High-res scans of usable A15, A16, and A17 metric camera frames.
    # Large tif images (~1.3 gb); only tested a dozen or so.
    # Headers open wrong (as copies of the IMAGE pointer)
    "metric_camera": {
        "manifest": IMG_FILE,
        "fn_must_contain": [".tif"],
        "url_must_contain": ['Metric_Camera', 'DATA'],
        "label": "D",
    },
}

"""
    # Scans of the original film photos of returned lunar rock/soil/core samples.
    # Pointers and object names don't match.
    # These are partially supported. data["DOCUMENT"] outputs array data but
    # data.show() fails. Changing the TIFF_DOCUMENT object to match the DOCUMENT
    # pointer fixes it, but a first attempt at a check_special_block() special
    # case didn't work.
    "sample_photos": {
        "manifest": IMG_FILE,
        "fn_must_contain": [".TIF"],
        "url_must_contain": ['Lunar_Sample_Photographs', 'DATA'],
        "label": "D",
    },
"""
