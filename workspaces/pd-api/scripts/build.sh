#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(dirname -- "$(readlink -f -- "${BASH_SOURCE[0]}")")"
cd $SCRIPT_DIR/../

uv sync

uv run pyinstaller --onedir -n pd-api pd_api/main.py
