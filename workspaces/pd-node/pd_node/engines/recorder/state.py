import threading

from pd_node.utils.state import BaseState

from .utils import get_video_disk_stats

class State(BaseState):
    def __init__(self):
        super().__init__()
        self.stack = []
            
    def push_frame(self, frame):
        with self._lock:
            self.stack.append(frame)

    def get_frames(self):
        with self._lock:
            frames = self.stack
            self.stack = []
            return frames

    def get_stats(self):
        return get_video_disk_stats()
        
