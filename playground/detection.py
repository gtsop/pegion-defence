import time
import cv2
import os
from ultralytics import YOLO

def draw_results(frame, results):
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = f"{model.names[cls]} {conf:.2f}"
        #if not model.names[cls] == "bird":
        #    continue
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, max(20, y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

model = YOLO("yolov8n.pt")

os.environ["OPENCV_VIDEOIO_DEBUG"] = "1"
os.environ["OPENCV_FFMPEG_DEBUG"] = "1"


cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("srt://127.0.0.1:9000?mode=caller&transtype=live&latency=200000", cv2.CAP_FFMPEG)
#cap = cv2.VideoCapture("./videos/athens.mp4", cv2.CAP_FFMPEG)

#url = "rtsp://localhost:8554/mystream"
#cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

print("opened:", cap.isOpened())
if cap.isOpened():
    print("backend:", cap.getBackendName())

print("opened:", cap.isOpened())

while True:
    _, frame = cap.read()

    results = model(frame)[0]

    draw_results(frame, results)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


