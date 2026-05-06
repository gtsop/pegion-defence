import time

import cv2

from .utils import get_capture, make_no_camera_frame

fallback_frame = make_no_camera_frame()

def thread(state):

    state.video.set_frame(fallback_frame)

    cap = None

    while True:

        frame = fallback_frame

        if not state.video.is_running():
            cap = clean_up(cap)
            time.sleep(1)

        if not cap:
            log("initializing capture device")
            cap = get_capture()
            if not cap:
                log("cannot detect cameras")
                time.sleep(1)

        if cap and not cap.isOpened():
            log("capture failed")
            cap = clean_up(cap)
            time.sleep(1)

        if cap:
            ret, frame = cap.read()
            if not ret:
                log("camera stream stopped")
                cap = clean_up(cap)
                frame = fallback_frame
                time.sleep(1)

        state.video.set_frame(frame.copy())

def log(msg):
    print("[video_thread]:", msg)

def clean_up(cap):
    if cap:
        cap.release()
    return None
