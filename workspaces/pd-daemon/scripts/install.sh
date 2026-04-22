#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR/../

# 1. Build the project
./scripts/build.sh

# 2. Symlink the binary
sudo ln -sf $(realpath ./bin/pd-daemon) /usr/local/bin/pd-daemon

# 3. Register the systemd service
sudo cp ./config/pd-daemon.service /lib/systemd/system/pd-daemon.service

echo "To start the pegion defence service run:"
echo ""
echo "    systemctl start pd-daemon"
echo ""


