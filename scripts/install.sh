#!/usr/bin/env bash

SCRIPT_DIR="$(dirname -- "$(readlink -f -- "${BASH_SOURCE[0]}")")"
cd $SCRIPT_DIR/../

#./workspaces/pd-api/scripts/install.sh
#./workspaces/pd-daemon/scripts/install.sh
#./workspaces/pd-frontend/scripts/install.sh
./workspaces/pd-node/scripts/install.sh
