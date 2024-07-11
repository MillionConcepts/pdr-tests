"""settings for pdr-tests"""

from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Dict, Optional

PKG_ROOT = Path(__file__).parent.parent

@dataclass(frozen=True)
class IxSettings:
    """
    Attributes of this class are configurable settings for the 'ix' tool.

    To configure them, create settings/user.py, which should consist
    of a series of assignments to (module-)global variables with the
    same names as these attributes, or all-uppercase versions of those
    names.

    If you specify any of the Path-typed attributes as a relative path
    (either as a string or as a relative Path object), it will be
    resolved relative to the pdr_tests package directory, not the
    source root nor the current working directory.
    """

    #: Root of directory tree for dumping "browse products"
    #: (data products converted to easily inspectable formats)
    browse_root: Path = "browse"

    #: Root of directory tree holding a local copy of the test corpus.
    data_root: Path = "data"

    #: Directory containing manifest files, which catalogue the
    #: complete PDS archive
    manifest_dir: Path = "node_manifests"

    #: Directory to write tracker logs to.
    tracker_log_dir: Path = ".tracker_logs"

    #: S3 bucket holding the complete test corpus.
    #: Currently used only by 'ix finalize'.
    test_corpus_bucket: Optional[str] = None

    #: Additional request headers to send when downloading
    #: PDS files over HTTP.  You should probably set User-Agent
    #: to a value that identifies you and distinguishes you from
    #: a generic python-based web crawler.
    headers: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        """
        Post-init hook, enforces that Path-typed attributes are
        actually paths and resolves relative paths as described
        in the class's docstring.
        """
        for field in fields(self):
            if field.type is Path:
                object.__setattr__(self, field.name,
                                   PKG_ROOT / getattr(self, field.name))

    @classmethod
    def load(cls: type) -> 'IxSettings':
        """
        Factory method, creates a settings object from the defaults
        and from user.py (if it exists).
        """
        try:
            from pdr_tests.settings import user
            params = {}
            for setting in fields(cls):
                for name in [setting.name, setting.name.upper()]:
                    if hasattr(user, name):
                        params[setting.name] = getattr(user, name)
                        break
            return cls(**params)

        except ImportError:
            return cls()

SETTINGS = IxSettings.load()
