from inspect import getmembers
from types import FunctionType, ModuleType
from typing import Union

from hostess.utilities import get_module


def find_literals(module: ModuleType) -> list[str]:
    members = []
    for name, member in getmembers(module):
        if member == module:
            continue
        if isinstance(member, (ModuleType, FunctionType, type)):
            continue
        else:
            members.append(name)
    return members


def monkeypatch_literals(
    target_module: Union[str, ModuleType],
    source_module: Union[str, ModuleType],
):
    if not isinstance(target_module, ModuleType):
        target_module = get_module(target_module)
    if not isinstance(source_module, ModuleType):
        source_module = get_module(source_module)
    source_literals = find_literals(source_module)
    target_literals = find_literals(target_module)
    for attrname in set(source_literals).intersection(target_literals):
        setattr(target_module, attrname, getattr(source_module, attrname))
