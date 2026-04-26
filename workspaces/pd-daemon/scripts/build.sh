#!/usr/bin/env bash
set -euo pipefail

uv sync

uv run pyinstaller --onedir --noconfirm -n pd-daemon pd_daemon/__main__.py
