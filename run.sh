#!/bin/bash -l

# Check if python is installed. If not, exit program
# prompt user to install python

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    You currently do not have python installed. Python is required to run this application.
    To install Python, check out https://www.python.org/downloads/' >&2
  exit 1
fi

python3 -m pip install --upgrade pip
python3 -m pip --version



# if ! [[ -x "$(command -v "]]
# Original base script. activate a venv, install colored==2.2.4 as per requirements.txt
# run main.py which is the application. 



if [[ -x "$(command -v python install -r requirements.txt)" ]]
then
  $(command -v python install -r requirements.txt)
  exit 1
fi

if [[ -x "$(command -v pip3 install -r requirements.txt)" ]]
then
  $(command -v pip3 install -r requirements.txt)
  exit 1
fi

if [[ -x "$(command -v pip install -r requirements.txt)" ]]
then
  $(command -v pip install -r requirements.txt)
  exit 1
fi

if [[ -x "$(command -v python3 install -r requirements.txt)" ]]
then
  $(command -v python3 install -r requirements.txt)
  exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python3 main.py

