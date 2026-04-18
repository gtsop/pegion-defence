#from common.utils import get_webcams
import argparse
import signal
import sys

import cv2
from ultralytics import YOLO

import utils

running = True

def handle_signal(a, b):
    running = False

def parse_cli_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--detect", default="on")
    parser.add_argument("--preview", default="off")

    args = parser.parse_args()

    return args

args = parse_cli_args()

print("================")
print("=== RPI NODE ===")
print("================")
print("")
print("- Detect:", args.detect)
print("- Preview:", args.preview)
print("")

DETECTION_ON = args.detect == "on"
PREVIEW_ON = args.preview == "on"
model = ''

if DETECTION_ON:
    print("-> Initializing model")
    model = YOLO("yolov8n_ncnn_model", task="detect")
    print("")

print("-> Listing available cameras")

cameras = utils.get_webcams()
if not cameras:
    sys.exit("There are no available cameras, exiting...")
for camera in cameras:
    print("\t", camera.filename, ":", camera.info.card)
print("")

print("-> Autoselecting camera")
camera = cameras[0]
camera_index = int(str(camera.filename).replace("/dev/video", ""))
print("\t", camera.filename)
print("")

print("-> Initializing video caputre")
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    sys.exit("Failed to open camera stream, exiting...")
else:
    print("\t", "Camera stream opened:", cap.getBackendName())
    print("\t", "Press ESC to exit")
    print("")

results = None
frame_id = 0

try:
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    while running:
        ret, frame = cap.read()

        if not ret:
            print("Camera stream stopped, exiting...")
            break

        frame_id = (frame_id + 1) % 2

        if DETECTION_ON and frame_id == 0:
            results = model(frame)[0]

        if PREVIEW_ON and results:
            utils.draw_bboxes(model, frame, results)
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
finally:
    cap.release()
    cv2.destroyAllWindows()


