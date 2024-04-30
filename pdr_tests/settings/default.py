"""settings for pdr-tests"""
from inspect import getmembers
from pathlib import Path
import sys

from _patcher import patch_settings_from_module

import pdr_tests.settings.user

# TODO: I'm inclined not to hardcode this...but not sure. --michael
headers = {
    "User-Agent": "MillionConcepts-PDART-pdrtestsuitespider "
                  "(sierra@millionconcepts.com)"
}

MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")

patch_settings_from_module(
    getmembers(sys.modules[__name__]), "pdr_tests.settings.user"
)

