#!/usr/bin/env bash
set -euo pipefail

cd ./models
uv run yolo export project=./models model=yolov8n.pt format=ncnn half=True imgsz=320
