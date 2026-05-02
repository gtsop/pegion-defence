import time

import cv2

cap = None
def thread(state):
    global cap

    while True:

        if not state.video.is_running():
            print("video capture is turned off, sleeping for 5 seconds")
            time.sleep(5)
            clean_up()
            continue

        if not cap:
            print("Initializing cap")
            cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            cap.set(cv2.CAP_PROP_FPS, 15)

        if not cap.isOpened():
            print("capture failed")
            clean_up()
            time.sleep(3)
            continue


        ret, frame = cap.read()
        state.video.set_frame(frame.copy())

        if not ret:
            print("Camera stream stopped, exiting...")
            clean_up()
            break

def clean_up():
    global cap

    if cap:
        cap.release()
        cv2.destroyAllWindows()

    cap = None

