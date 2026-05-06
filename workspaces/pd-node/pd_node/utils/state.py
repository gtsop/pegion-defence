import threading

class BaseState:
    def __init__(self):
        self._lock = threading.Lock()
        self.running = False

    def _set_running(self, value):
        with self._lock:
            self.running = value

    def start(self):
        self._set_running(True)

    def stop(self):
        self._set_running(False)
    
    def is_running(self):
        with self._lock:
            return self.running


