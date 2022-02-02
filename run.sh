#!/usr/bin/env bash

# Fail on any commands that exit with a non-zero code
set -e

# Source the venv
if [ -d "./venv" ]
then
    echo "venv exists, activating..."
else
    echo "venv doesnt exist, creating and activating..."
    source ./setup.sh
fi
source ./venv/bin/activate


python -m app
