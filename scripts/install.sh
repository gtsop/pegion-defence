#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR/../

RPI_NODE_BIN=$(realpath ./workspaces/rpi-node/bin/)

sed "s%RPI_NODE_BIN%$RPI_NODE_BIN/rpi-node%g" ./workspaces/rpi-node/rpi-node.service.template > rpi-node.service
sudo mv rpi-node.service /lib/systemd/system/rpi-node.service

echo "To run the pegion defence service run:"
echo ""
echo "    systemctl start rpi-node"
echo ""

