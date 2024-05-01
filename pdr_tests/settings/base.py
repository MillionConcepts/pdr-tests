"""settings for pdr-tests"""
from pathlib import Path
import sys

from pdr_tests.settings._patcher import monkeypatch_literals

import pdr_tests.settings.user

HEADERS = None
MANIFEST_DIR = Path(Path(pdr_tests.__file__).parent, "node_manifests")
TEST_CORPUS_BUCKET = None

monkeypatch_literals(sys.modules[__name__], pdr_tests.settings.user)
