#!/bin/bash

mkdir -p log

# Set version to 3.7.3
export PYENV_VERSION=3.7.3
python ffnn.py | tee log/ffnn.log
python lstm.py | tee log/lstm.log

# Reset version
unset PYENV_VERSION

# Set version to 2.7.16
export PYENV_VERSION=2.7.16
python xgboost_learn.py | tee log/xgboost.log

# Reset version
unset PYENV_VERSION
