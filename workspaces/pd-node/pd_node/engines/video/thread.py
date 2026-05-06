import time

import cv2

from .utils import get_capture

def thread(state):

    cap = None

    while True:

        if not state.video.is_running():
            clean_up(cap)
            time.sleep(1)
            continue

        if not cap:
            log("initializing capture device")
            cap = get_capture()

        if not cap.isOpened():
            log("capture failed")
            clean_up(cap)
            time.sleep(1)
            continue

        ret, frame = cap.read()
        state.video.set_frame(frame.copy())

        if not ret:
            log("camera stream stopped")
            clean_up(cap)
            time.sleep(1)
            continue

def log(msg):
    print("[video_thread]:", msg)

def clean_up(cap):
    if cap:
        cap.release()

