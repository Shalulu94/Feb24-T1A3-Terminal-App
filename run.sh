#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    You currently do not have python installed. Python is required to run this application.
    To install Python, check out https://www.python.org/downloads/' >&2
  exit 1
fi


python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

python3 main.py

$(command -v python3 install colored)

