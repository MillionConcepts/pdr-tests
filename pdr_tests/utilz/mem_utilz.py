from ctypes import c_uint8, c_long
from multiprocessing.sharedctypes import Value
from multiprocessing import Process
import os
from typing import MutableMapping, Optional

import psutil
import time


def watch_mempeak(
    pid: int,
    quitval: Value,
    memval: Value,
    interval: float = 0.005
):
    mems = []
    proc = psutil.Process(pid)
    while quitval.value == 0:
        mems.append(proc.memory_info().rss)
        time.sleep(interval)
    mems.append(proc.memory_info().rss)
    if len(mems) > 0:
        memval.value = max(mems) - memval.value
    else:
        memval.value = 0


class _MemwatcherContext:

    def __init__(self, parent):
        self.quitval = Value(c_uint8, 0, lock=False)
        self.memval = Value(
            c_long, psutil.Process().memory_info().rss, lock=False
        )
        self.peak = 0
        self.memwatch = None
        self.parent = parent

    def __enter__(self):
        self.memwatch = Process(
            target=watch_mempeak,
            args=(os.getpid(), self.quitval, self.memval)
        )
        self.memwatch.start()

    def __exit__(self, *_):
        self.quitval.value = 1
        self.memwatch.join()
        self.parent.peaks.append(self.memval.value)
        self.memwatch = None
        self.parent.active_watcher = None


class _FakeMemwatcherContext:

    def __init__(self, parent):
        self.parent = parent

    def __enter__(self):
        pass

    def __exit__(self, *_):
        self.parent.peaks.append(None)
        pass


class Memwatcher:

    def __init__(self, fake=False):
        self.peaks = []
        self.active_watcher = None
        self.fake = fake

    def watch(self):
        if self.fake is True:
            self.active_watcher = _FakeMemwatcherContext(self)
        else:
            self.active_watcher = _MemwatcherContext(self)
        return self.active_watcher


# TODO, maybe: add a timeout
class OOMLock:

    def __init__(
        self,
        memstats: MutableMapping,
        shared_memval: Optional[Value] = None,
        max_mem: int = 0,
    ):
        self.memstats = memstats
        self.shared_memval = shared_memval
        self.max_mem = max_mem
        self.pickmem = 0

    def __enter__(self):
        if self.shared_memval is None:
            return next(iter(self.memstats.keys()))
        while True:
            current = self.shared_memval.value
            for ix, mem in tuple(self.memstats.items()):
                if mem == 0:
                    self.pickmem = 0
                    self.memstats.pop(ix)
                    return ix
                if mem + current < self.max_mem:
                    self.shared_memval.value += mem
                    self.pickmem = mem
                    self.memstats.pop(ix)
                    return ix
            time.sleep(0.01)

    def __exit__(self, *_):
        if self.shared_memval is None or self.pickmem == 0:
            return
        self.shared_memval.value -= self.pickmem
