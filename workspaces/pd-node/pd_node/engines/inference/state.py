import threading

from pd_node.utils.state import BaseState

class State(BaseState):
    def __init__(self):
        super().__init__()
        self.results = None
        self.names = None

    def set_results(self, resluts):
        with self._lock:
            self.results = resluts

    def get_results(self):
        with self._lock:
            return self.results

    def set_names(self, names):
        with self._lock:
            self.names = names

    def get_names(self):
        with self._lock:
            return self.names



