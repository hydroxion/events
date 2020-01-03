#!/bin/bash

# Run: source virtualenv.sh

# Install the system dependencies
apt install python3 python3-dev python3-setuptools python3-wheel python3-pip python3-venv -y

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the project dependencies
pip3 install -r requirements.txt --no-cache-dir