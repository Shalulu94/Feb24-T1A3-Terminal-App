#!/bin/bash

apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py