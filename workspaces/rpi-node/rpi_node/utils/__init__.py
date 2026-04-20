import cv2
from linuxpy.video.device import iter_video_capture_devices


def draw_bboxes(model, frame, results):
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

            if "bcm2835" in str(device.info.card):
                continue

            if "VIDEO_CAPTURE" in caps or "VIDEO_CAPTURE_MPLANE" in caps:
                webcams.append(device)

    return webcams

def get_objects(object_name, model, results):
    objects = []

    for box in results.boxes:
        name = model.names[int(box.cls[0])]

        if name == object_name:
            objects.append(box)

    return objects

# Compatibility check for running the same code on non-Rpi devices
detection_pin = 23
try:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(detection_pin, GPIO.OUT)

    def set_led(on):
        GPIO.output(detection_pin, GPIO.HIGH if on else GPIO.LOW)

except:
    def set_led(on):
        print(f"Turning LED {'ON' if on else 'OFF'}") 
