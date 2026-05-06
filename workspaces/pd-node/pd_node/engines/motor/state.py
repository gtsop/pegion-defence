import threading

from pd_node.utils.state import BaseState

class State(BaseState):
    def __init__(self):
        super().__init__()
        self.angle = 50
        self.target_angle = 50
            
    def needs_movement(self):
        with self._lock:
            return self.angle != self.target_angle

    def did_move(self):
        with self._lock:
            self.angle = self.target_angle

    def set_target_angle(self, angle):
        with self._lock:
            self.target_angle = angle

    def get_target_angle(self):
        with self._lock:
            return self.target_angle

    def is_moving_right(self):
        with self._lock:
            return self.target_angle < self.angle

    def is_moving_left(self):
        with self._lock:
            return self.target_angle > self.angle


