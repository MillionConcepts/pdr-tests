"""settings for pdr-tests"""
from pathlib import Path
import sys

self_path = Path(__file__)
pkg_path = self_path.parent.parent
user_settings_path = self_path.parent / "user.py"
if not user_settings_path.exists():
    user_settings_path.touch()

from pdr_tests.settings._patcher import monkeypatch_literals
from pdr_tests.settings import user as user_settings_mod

BROWSE_ROOT = pkg_path / "browse"
DATA_ROOT = pkg_path / "data"
MANIFEST_DIR = pkg_path / "node_manifests"
TRACKER_LOG_DIR = pkg_path / ".tracker_logs"

HEADERS = {}
TEST_CORPUS_BUCKET = None

monkeypatch_literals(sys.modules[__name__], user_settings_mod)
