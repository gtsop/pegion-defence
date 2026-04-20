#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR/../

RPI_NODE_BIN=$(realpath ./workspaces/rpi-node/bin/)/rpi-node
RPI_NODE_API_BIN=$(realpath ./workspaces/rpi-node/bin/)/rpi-node-api

sed "s%RPI_NODE_BIN%$RPI_NODE_BIN%g" ./workspaces/rpi-node/rpi-node.service.template > rpi-node.service
sudo mv rpi-node.service /lib/systemd/system/rpi-node.service

echo "To run the pegion defence service run:"
echo ""
echo "    systemctl start rpi-node"
echo ""

sed "s%RPI_NODE_API_BIN%$RPI_NODE_API_BIN%g" ./workspaces/rpi-node/rpi-node-api.service.template > rpi-node-api.service
sudo mv rpi-node-api.service /lib/systemd/system/rpi-node-api.service

echo "To run the pegion defence api service run:"
echo ""
echo "    systemctl start rpi-node-api"
echo ""

