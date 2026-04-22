#!/usr/bin/env bash
set -euo pipefail

uv run yolo export project=./models model=yolov8n.pt format=ncnn half=True imgsz=320 path=./models
