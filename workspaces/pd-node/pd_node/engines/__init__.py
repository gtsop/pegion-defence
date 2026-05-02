import threading

from . import video
from . import inference
from . import composer
from . import recorder

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


class VideoState(BaseState):
    def __init__(self):
        super().__init__()
        self.frame = None
    
    def set_frame(self, frame):
        with self._lock:
            self.frame = frame

    def get_frame(self):
        with self._lock:
            return self.frame

class InferenceState(BaseState):
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

class ComposerState(BaseState):
    def __init__(self):
        super().__init__()
        self.frame = None

    def set_frame(self, frame):
        with self._lock:
            self.frame = frame

    def get_frame(self):
        with self._lock:
            return self.frame

class RecorderState(BaseState):
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
