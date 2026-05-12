import time
from datetime import datetime, timezone

from ultralytics import YOLO
import numpy as np

from pd_node.utils import get_base_path
import pd_node.db as db

model = YOLO(get_base_path() / "models/yolo11n_ncnn_model", task="detect")

session = db.create_session()

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

        results = model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            verbose=False
        )[0]

        state.inference.set_results(results)

        store_detections(results.boxes)

        time.sleep(1/15)

live_detections = {}
def store_detections(boxes):
    global live_detections

    ids = boxes.id
    if ids is not None:
        ids = ids.cpu().numpy().astype(int).tolist()
    else:
        ids = []

    live_ids = list(live_detections.keys())

    out_ids = list(set(live_ids) - set(ids))
    in_ids = list(set(ids) - set(live_ids))

    for id in out_ids:
        obj = live_detections[id]
        record = db.models.ObjectDetection(
            name=obj['name'],
            model="yolo11n",
            detection_start=obj['detection_start'],
            detection_end=datetime.now(timezone.utc)
        )
        session.add(record)
        del live_detections[id]

    session.commit()

    for box in boxes:
        if box.id in in_ids:
            live_detections[int(box.id)] = {
                "name": model.names[int(box.cls[0])],
                "detection_start": datetime.now(timezone.utc)
            }

def log(msg):
    print("[inference_thread]:" + msg)
