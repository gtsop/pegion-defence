import os
import time

from ultralytics import YOLO
from pd_node.utils import get_base_path

model = YOLO(get_base_path() / "models/yolo11n_ncnn_model", task="detect")

def thread(state):

    state.inference.set_names(model.names)

    while True:
        
        if not state.inference.is_running():
            state.inference.set_results(None)
            time.sleep(5)
            continue

        frame = state.video.get_frame()

        if frame is None:
            time.sleep(1/15)
            continue

        results = model(frame)[0]

        state.inference.set_results(results)

        time.sleep(1/15)


