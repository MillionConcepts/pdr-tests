from ctypes import c_uint8, c_long
from multiprocessing.sharedctypes import Value
from multiprocessing import Process
import os
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


class Memwatcher:

    def __init__(self):
        self.peaks = []
        self.active_watcher = None

    def watch(self):
        self.active_watcher = _MemwatcherContext(self)
        return self.active_watcher
