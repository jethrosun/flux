#!/bin/bash

sudo apt install -y python-pip python-matplotlib
sudo apt install -y automake

sudo apt install -y libreadline6 libreadline6-dev
sudo apt install -y bzip2 
sudo apt install -y libsqlite3-dev

# Set version to 2.7.10
export PYENV_VERSION=3.7.3

pyenv install $PYENV_VERSION
pip install -r requirements.txt

# Reset version
unset PYENV_VERSION

# Set version to 2.7.10
export PYENV_VERSION=2.7.16


pyenv install $PYENV_VERSION

# Reset version
unset PYENV_VERSION

