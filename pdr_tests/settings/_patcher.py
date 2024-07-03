"""glue logic to merge settings.base and settings.user"""

import sys
import types
from pathlib import Path

def load_settings():
    """
    Called when pdr_tests.settings is first loaded.  Do not call
    unless you are pdr_tests/settings/__init__.py.

    Erase the contents of pdr_tests.settings and replace it with a
    clone of pdr_tests.settings.base; if pdr_tests.settings.user
    exists, each attribute in .user with the same name as an attribute
    of .base replaces base's value.

    Additionally, if BASE defines the attribute __PKG_RELATIVE_PATH_ATTRS__,
    each attribute with a matching name will be converted to a Path,
    resolving relative paths relative to the pdr_tests package root
    (not the source root or the cwd).
    """
    settings_mod = sys.modules["pdr_tests.settings"]
    pkg_root = Path(settings_mod.__file__).parent.parent

    from pdr_tests.settings import base
    try:
        from pdr_tests.settings import user
    except ImportError:
        user = types.ModuleType("pdr_tests.settings.user")

    path_attrs = frozenset(
        getattr(base, "__PKG_RELATIVE_PATH_ATTRS__", ())
    )

    # settings_mod.__dict__.clear() would delete things like __name__
    # also the Python reference manual says "modifying [a module
    # object's] __dict__ directly is not recommended"
    # dir() returns a list, not an iterator
    for unwanted in dir(settings_mod):
        if not unwanted.startswith("__"):
            delattr(settings_mod, unwanted)

    for attr in dir(base):
        if not attr.startswith("_"):
            if hasattr(user, attr):
                val = getattr(user, attr)
            else:
                val = getattr(base, attr)
            if attr in path_attrs:
                val = pkg_root / val
            setattr(settings_mod, attr, val)
