#!/usr/bin/env bash

SCRIPT_DIR="$(dirname -- "$(readlink -f -- "${BASH_SOURCE[0]}")")"
cd $SCRIPT_DIR/../

cd public
python -m http.server 3000
