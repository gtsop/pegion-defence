import cv2
from ultralytics import YOLO

def draw_results(frame, results):
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = f"{model.names[cls]} {conf:.2f}"
        if not model.names[cls] == "bird":
            continue
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, max(20, y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
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


