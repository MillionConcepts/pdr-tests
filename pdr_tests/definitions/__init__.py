"""PDR tests: definitions of test data sets."""

import importlib as _importlib
from collections.abc import Mapping as _Mapping


class _RulesModulesMap(_Mapping):
    """
    Rules modules are sub-sub-modules of this module:
    if `from .{name}.selection_rules import file_information` would work
    (in this file), then `name` is a rules module.

    This singleton acts like a read-only dictionary { name: module } where
    module is the `selection_rules` module corresponding to `name` (not
    the `file_information` object).
    """
    def __init__(self):
        self._rules_modules = {}
        self._scan_complete = False

    def __getitem__(self, key):
        try:
            return self._load_rules_mod(key)
        except (AttributeError, ModuleNotFoundError) as e:
            raise KeyError(key) from e

    def __iter__(self):
        self._ensure_all_loaded()
        return iter(self._rules_modules)

    def __len__(self):
        self._ensure_all_loaded()
        return len(self._rules_modules)

    def _ensure_all_loaded(self):
        if self._scan_complete:
            return

        for subdir in _importlib.resources.files(__name__).iterdir():
            if subdir.name in ("__cache__", "__init__.py"):
                continue
            try:
                self._load_rules_mod(subdir.name)
            except (AttributeError, ModuleNotFoundError):
                pass

        self._scan_complete = True

    def _load_rules_mod(self, name):
        try:
            return self._rules_modules[name]
        except KeyError:
            pass

        mod = _importlib.import_module(
            f".{name}.selection_rules",
            __name__,
        )
        getattr(mod, "file_information")
        self._rules_modules[name] = mod
        return mod


RULES_MODULES = _RulesModulesMap()
