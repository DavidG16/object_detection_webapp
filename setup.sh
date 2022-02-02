#!/usr/bin/env bash

# Fail on any commands that exit with a non-zero code
set -e


##check if brew exists
#if [ "$(command -v brew)" ];
#then
#    echo "command \"brew\" exists on system"
#else
#  echo "install Brew"
#  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#fi
#
#
##install Python 3.7
#brew install python@3.7

# Source the venv
if [ -d "./venv" ]
then
    echo "venv exists, activating..."
else
    echo "venv doesnt exist, creating and activating..."
    virtualenv --python python3.8 venv
fi


if [ -f "./venv/pip.conf" ]
then 
    echo "pip.conf exists"
else 
    echo "pip.conf does not exists, creating one.."
    touch ./venv/pip.conf
    echo "[global]" >> ./venv/pip.conf
    echo "index-url = https://pypi.python.org/simple/" >> ./venv/pip.conf
fi    

source venv/bin/activate

# pip
pip install --upgrade pip
pip install -r requirements.txt



