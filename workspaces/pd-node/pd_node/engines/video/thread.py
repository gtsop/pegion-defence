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
            print("video_thread: initializing caputre device")
            cap = get_capture()

        if not cap.isOpened():
            print("video_thread: capture failed")
            clean_up()
            time.sleep(1)
            continue

        ret, frame = cap.read()
        state.video.set_frame(frame.copy())

        if not ret:
            print("Camera stream stopped, exiting...")
            clean_up()
            break

def clean_up():
    if cap:
        cap.release()

