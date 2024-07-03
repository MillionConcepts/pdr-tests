"""settings for pdr-tests - defaults"""

#: Used by _patcher.merge_settings to know which attributes are
#: supposed to be Path objects.  Relative path strings will be
#: resolved relative to the pdr_tests package directory, not the
#: source root, nor the current working directory.
__PKG_RELATIVE_PATH_ATTRS__ = [
    "BROWSE_ROOT",
    "DATA_ROOT",
    "MANIFEST_DIR",
    "TRACKER_LOG_DIR",
]

BROWSE_ROOT = "browse"
DATA_ROOT = "data"
MANIFEST_DIR = "node_manifests"
TRACKER_LOG_DIR = ".tracker_logs"

HEADERS = {}
TEST_CORPUS_BUCKET = None
