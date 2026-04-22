#!/usr/bin/env bash
set -euo pipefail

uv sync --group dev
uv run pyinstaller --onefile -n pd-daemon pd_daemon/__main__.py
