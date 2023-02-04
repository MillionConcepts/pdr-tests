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

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
LRO_FILE = Path(MANIFEST_DIR, "geolro_coverage.parquet")

# the '/lro' on the end of the url_must_contain instructions is to exclude
# products in 'superseded' subdirectories
file_information = {
    # simple flat ascii tables including decoded telemetry
    # from a 1-hour period
    "edr": {
        "manifest": LRO_FILE,
        "fn_must_contain": ['edr.tab'],
        "url_must_contain": ['lro-l-dlre-2-edr-v1/lro'],
        "label": "D",
    },
    # ZIP-compressed flat ascii tables. directly derived from EDRs, but
    # calibration increases their data volume a lot, so each
    # RDR contains data from only 10 minutes.
    "rdr": {
        "manifest": LRO_FILE,
        "fn_must_contain": ['rdr.zip'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro'],
        "label": "D",
    },
    # L2 / GDR (gridded data record) products "mimic the format and intent
    # of the LOLA GDR...NASA Level 2 Diviner GDR products include solar
    # reflectances, brightness temperatures, and time-related values such as
    # local time and Julian Date that are binned and averaged according to
    # 27-day LRO mapping cycles. Each averaged product is further split into
    # daytime (local time 06:00 to 18:00) and nighttime (local time 18:00 to
    # 06:00) data products. Unlike the LOLA GDR data products, which use
    # interpolation to create continuous global grids, Diviner GDR data
    # products will include data gaps in grid cells where no observations
    # were acquired. Only nadir-pointing data will be used in these datasets
    # (RDR activity flag 110 – on moon, standard nadir). The thermal channel
    # data was further constrained to brightness temperature values of 10 to
    # 450 K as anything outside this range contains bad data. Observations
    # with excessive noise were also culled. The finite field of view of the
    # Diviner footprints will be taken into account to produce the master
    # maps, which will avoid resolution aliasing problems at higher
    # latitudes. All footprints will be projected by locating the fields of
    # view in three dimensions onto a LOLA digital elevation model of the
    # Moon."

    # "The GDR IMG data files are stored as 16-bit signed binary integers in
    # least- significant-byte (LSB) order." "The RDR channel names and
    # detector order have been changed from the method used in the Diviner
    # EDR dataset"

    # what the SIS refers to as a single L2 GDR "product" has up to (maybe
    # always?) 30 'planes' -- 9 visual brightness and/or brightness
    # temperature planes (one per channel), each of which also has raw count
    # and error backplanes; an (actually-L3) derived bolometric temperature
    # plane; a local time backplane, and a julian date backplane. because
    # each of these planes is stored in a separate raster file with its own
    # detached label, this is PDS-formally up to 30 distinct products per GDR.

    # each of these planes also comes in two "flavors" -- IMG and JP2. The
    # JP2 files are produced directly from the IMG files. They also include
    # both cylindrical and polar projections, and come at various resolutions,
    # but the basic formats do not appear different.
    # note that the 128px/deg GDRs can be _very_ big, ~25000 x ~45000,
    # which means even the 64px/deg GDRs ones are still _big_

    # ends_with instructions are intended to ignore detached XML files for
    # ArcGIS in EXTRAS
    "gdr_l2_img": {
        "manifest": LRO_FILE,
        "fn_ends_with": ['.img'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'gdr_l2'],
        "label": "D",
    },
    "gdr_l2_jp2": {
        "manifest": LRO_FILE,
        "fn_ends_with": ['.jp2'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'gdr_l2'],
        "label": "D",
    },
    # L3 GDRs -- gridded derived values, I think coregistered with the L2
    # GDRs. also scaled 16-bit ("16-byte integers"). 5 'planes' / files /
    # products for each version of each L3 GDR: Standard Christiansen
    # Feature (CF) wavelength, normalized CF wavelength, rock abundance,
    # soil termperature, and RMS errors between measured and modeled
    # radiances. again, both IMG and JP2 flavors.
    "gdr_l3_img": {
        "manifest": LRO_FILE,
        "fn_ends_with": ['.img'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'data', 'gdr_l3'],
        "label": "D",
    },
    "gdr_l3_jp2": {
        "manifest": LRO_FILE,
        "fn_ends_with": ['.jp2'],
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'data', 'gdr_l3'],
        "label": "D",
    },
    # L4 products: big flat ascii tables. they are comma-separated
    # but are also fixed-width. 3 flavors: Polar resource products
    # (derived quantities coregistered to Kaguya altimeter DEM mesh)
    # global cumulative products, polar cumulative products.
    # don't know yet if I want to stick examples of each in.
    "l4": {
        "manifest": LRO_FILE,
        "url_must_contain": ['lro-l-dlre-4-rdr-v1/lro', 'data'],
        "fn_regex": ["(pcp|dlre_prp|global)_.*tab"],
        "label": "D",
    }
}
