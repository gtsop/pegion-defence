#from common.utils import get_webcams
import argparse
import sys

import cv2

import utils

def parse_cli_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--mode", default="preview")

    args = parser.parse_args()

    return args

args = parse_cli_args()

print("================")
print("=== RPI NODE ===")
print("================")
print("")
print("-> Mode:", args.mode)
print("")

DETECTION_ON = args.mode == "detect"
model = ''

if DETECTION_ON:
    print("-> Initializing model")
    #model = YOLO("yolov8n.pt")

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

while True:
    _, frame = cap.read()

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


