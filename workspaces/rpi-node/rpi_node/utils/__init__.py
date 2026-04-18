import cv2
from linuxpy.video.device import iter_video_capture_devices


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

    for device in iter_video_capture_devices():

        with device:
            caps = dir(device.info.capabilities)

            if "VIDEO_CAPTURE" in caps or "VIDEO_CAPTURE_MPLANE" in caps:
                webcams.append(device)

    return webcams

