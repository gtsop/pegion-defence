import cv2
import linuxpy.video.device

def draw_bboxes(frame, results):
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = f"{model.names[cls]} {conf:.2f}"
        #if not model.names[cls] == "bird":
        #    continue
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, max(20, y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

def get_webcams():
    webcams = []

    for path in Device.iter_devices():
        device = Device(path)

        caps = dev.capabilities

        if caps.meta_caputre:
            continue

        if caps.video_caputre or caps.video_capture_mplane:
            webcams.append(path)

    return webcams

