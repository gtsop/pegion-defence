#!/usr/bin/env bash

SCRIPT_DIR="$(dirname -- "$(readlink -f -- "${BASH_SOURCE[0]}")")"
cd $SCRIPT_DIR/../

sudo mkdir -p /var/www/pd-frontend
sudo cp -R ./public/* /var/www/pd-frontend

sudo mkdir -p /etc/nginx/nginx.d/
sudo cp ./config/nginx/nginx.conf /etc/nginx/nginx.conf

echo "To run the pegion defence frontend service run:"
echo ""
echo "    systemctl start nginx"
echo ""

