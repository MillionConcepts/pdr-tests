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

GEO_FILE = "geomex"

file_information = {
    
    # level 2 raw image data
    # notionally supported
    "edr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.raw'],
        "url_must_contain": ['mex-m-vmc-2-edr', 'data'],
        "label": "D",
    },
    # level 3 calibrated image data
    # notionally supported
    "rdr": {
        "manifest": GEO_FILE,
        "fn_must_contain": ['.fit'],
        "url_must_contain": ['mex-m-vmc-3-rdr', 'data'],
        "label": "D",
    },
    
}

"""
EDR
- Most of the 200 test products open fine
- Those that don't open give an error in the format of "cannot reshape array of 
  size x into shape (y, z)"
- They are smaller files, and will open after replacing “LINES = 480” in the 
  label with a smaller number. 
- 2448 out of 83687 EDR products are <307 KB. Files >=307 KB appear to be the 
  complete images
- Based on the 200 product sample set, most of the incomplete images/files are 
  from earlier in the mission. Extended mission 2 and earlier

RDR
- Two IMAGE objects per the one IMAGE pointer
    - 3 band, SAMPLE_INTERLEAVED, IEEE_REAL, 32 bit
    - 1 band, BAND_SEQUENTIAL, UNSIGNED_INTEGER, 8 bit
- HDU 0 is the header, HDU 1 is a multiband image, HDU 2 is a single band image
- From the volume's readme: "The first layer includes the calibrated values, 
  and the second layer includes the raw values." It is unclear whether or not 
  the 'second layer' is a copy of the EDR image or if intermediate calibration 
  steps have been applied to it.
- A special case returns the multiband calibrated images under the assumption 
  that the single band raw images are akin to the EDRs
"""
