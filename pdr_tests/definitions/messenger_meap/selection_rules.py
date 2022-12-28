"""
This is a stub dictionary to allow the addition of a single example of
MEAP Enhanced Gamma Ray Spectrometry Data. This dataset did not undergo a full ix testing, but
an example was chosen to make sure the byte order changes made to support this did not revert
with later iterations and changes
"""

from pathlib import Path
import pdr_tests

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

# shorthand variables for specific .csv files
GEO_MESSENGER_FILE = Path(MANIFEST_DIR, "geomessenger.parquet")

file_information = {
    "enh_grs_spec": {
        "manifest": GEO_MESSENGER_FILE,
        "fn_must_contain": [".dat"],
        "url_must_contain": ['data_grsspectra', 'pdart14_meap/'],
        "label": ('.dat', '.xml'),
    },
}
