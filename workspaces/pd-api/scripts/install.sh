#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(dirname -- "$(readlink -f -- "${BASH_SOURCE[0]}")")"
cd $SCRIPT_DIR/../

# 1. Build the project
./scripts/build.sh

# 2. Symlink the binary
sudo ln -sf $(realpath ./bin/pd-api) /usr/local/bin/pd-api

# 3. Register the systemd service
sudo cp ./config/pd-api.service /lib/systemd/system/pd-api.service

echo "To start the pegion defence service run:"
echo ""
echo "    systemctl start pd-api"
echo ""


