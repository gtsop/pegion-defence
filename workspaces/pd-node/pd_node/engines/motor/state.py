import threading

from pd_node.utils.state import BaseState

class State(BaseState):
    def __init__(self):
        super().__init__()
        self.angle = 50
        self.target_angle = 50
        self._move = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
            
    def move(self, direction):
        with self._lock:
            self._move[direction] = True

    def freeze(self, direction):
        with self._lock:
            self._move[direction] = False

    def should_move(self, direction):
        with self._lock:
            return self._move[direction]
