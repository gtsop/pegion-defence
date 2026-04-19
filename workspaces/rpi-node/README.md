# rpi-node

Pegion Defence Node targeting the Raspberry Pi 4

The Node performs object detection through the webcam and turns on a pin when pegions ("bird") are in view

## Tech stack

- Uses opencv for getting the video feed
- Uses ultralytics for running the YOLO model
- Uses RPi GPIO for giving of a current signal when pegions are detected

## Running

Navigate to `workspaces/rpi-node` and run

```
uv run rpi_node
```

By default, the application will perform headless detection on "bird" objects and turn on the 23 pin.

For debugging you can override the following options:

```
uv run rpi-node
    --detect-target person   # change the detection target to some other object (use YOLO lables)
    --detection off          # turn off the object detection
    --preview on             # turns on GUI preview window
```
