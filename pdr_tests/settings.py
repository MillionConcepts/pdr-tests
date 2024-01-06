"""settings for pdr-tests"""
from pathlib import Path

import pdr_tests

# TODO: I'm inclined not to hardcode this...but not sure. --michael
headers = {
    "User-Agent": "MillionConcepts-PDART-pdrtestsuitespider (sierra@millionconcepts.com)"
}

PARQUET_SETTINGS = {
    "row_group_size": 100000,
    "version": "2.6",
    "use_dictionary": ["domain", "url", "size"],
}
MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")
