import threading

from pd_node.utils.state import BaseState

class State(BaseState):
    def __init__(self):
        super().__init__()
        self.frame = None

    def set_frame(self, frame):
        with self._lock:
            self.frame = frame

    def get_frame(self):
        with self._lock:
            return self.frame

