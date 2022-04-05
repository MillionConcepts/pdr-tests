"""troubleshooting & benchmarking utilities"""
import _ctypes
import gc
import time
from typing import Mapping


class FakeStopwatch:
    """fake simple timer object"""
    def __init__(self, digits=2, silent=False):
        self.digits = digits
        self.last_time = None
        self.start_time = None
        self.silent = silent

    def peek(self):
        return

    def start(self):
        return

    def click(self):
        return


class Stopwatch(FakeStopwatch):
    """simple timer object"""
    def __init__(self, digits=2, silent=False):
        super().__init__(digits, silent)

    def peek(self):
        return round(time.time() - self.last_time, self.digits)

    def start(self):
        if self.silent is False:
            print("starting timer")
        now = time.time()
        self.start_time = now
        self.last_time = now

    def click(self):
        if self.last_time is None:
            return self.start()
        if self.silent is False:
            print(f"{self.peek()} elapsed seconds, restarting timer")
        self.last_time = time.time()


def filter_ipython_history(item):
    if not isinstance(item, Mapping):
        return True
    if item.get("__name__") == '__main__':
        return False
    if "_i" not in item.keys():
        return True
    return False


def print_referents(obj, filter_literal = True, filter_ipython = True):
    return print_references(
        obj, gc.get_referents, filter_literal, filter_ipython
    )


def print_referrers(obj, filter_literal = True, filter_ipython = True):
    return print_references(
        obj, gc.get_referrers, filter_literal, filter_ipython
    )


def print_references(
    obj, method, filter_literal=True, filter_ipython=True
):
    refs = method(obj)
    if filter_literal is True:
        refs = tuple(
            filter(lambda ref: not isinstance(ref, (float, str)), refs)
        )
    if filter_ipython is True:
        refs = tuple(filter(filter_ipython_history, refs))
    extra_printables = [
        None if not isinstance(ref, tuple) else ref[0] for ref in refs
    ]
    for ref, extra in zip(refs, extra_printables):
        print(id(ref), type(ref), id(extra), type(extra))
    return refs


def di(obj_id):
    return _ctypes.PyObj_FromPtr(obj_id)