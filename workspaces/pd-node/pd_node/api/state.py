import pd_node.engines as engines

class AppState:
    def __init__(self):
        self.composer = engines.composer.State()
        self.inference = engines.inference.State()
        self.motor = engines.motor.State()
        self.recorder = engines.recorder.State()
        self.video = engines.video.State()

        self.composer.start()
        self.inference.start()
        self.motor.start()
        self.video.start()

app_state = AppState()

