#!/bin/bash

# Added in this install function post testing. 
# Terminal prompted that python3.10-venv needed to be installed prior to being able
# to initialise a virtual environment
apt install python3.10-venv 

# Original base script. activate a venv, install colored==2.2.4 as per requirements.txt
# run main.py which is the application. 
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py