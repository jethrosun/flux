#!/bin/bash

sudo apt install -y python-pip python-matplotlib
sudo apt install -y automake

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

sudo apt install -y libedit-dev


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

