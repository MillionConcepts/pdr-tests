from inspect import getmembers
import sys
from typing import Mapping


def patch_settings_from_module(settings, module_name):
    settings = {
        name: setting for name, setting in settings if "SETTING" in name
    }
    patches = {
        name: patch
        for name, patch in getmembers(
            sys.modules[module_name], lambda obj: isinstance(obj, Mapping)
        )
        if name in settings.keys()
    }
    for name, patch in patches.items():
        settings[name] |= patch
