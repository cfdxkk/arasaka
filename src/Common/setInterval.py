import threading
import time

class setInterval:
    def __init__(self, func, interval):
        self.func = func
        self.interval = interval
        self.thread = None
        self.stop_event = threading.Event()
        
    def _interval_func(self):
        while not self.stop_event.is_set():
            start_time = time.time()
            
            self.func()
            
            elapsed_time = time.time() - start_time
            sleep_duration = max(0, self.interval - elapsed_time)
            
            self.stop_event.wait(sleep_duration)

    def start(self):
        if self.thread is None:
            self.stop_event.clear()
            self.thread = threading.Thread(target=self._interval_func)
            self.thread.start()

    def stop(self):
        if self.thread:
            self.stop_event.set()
            self.thread.join()
