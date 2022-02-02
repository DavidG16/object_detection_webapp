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

#
if [ $1 = "prod" ]
then
  gunicorn --worker-class gthread --workers 1 --bind 0.0.0.0:5000 app.__main__:daemon_app  --timeout 1000
else
  python -m app
fi

