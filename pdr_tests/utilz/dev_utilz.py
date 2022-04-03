"""troubleshooting & benchmarking utilities"""
import time


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
