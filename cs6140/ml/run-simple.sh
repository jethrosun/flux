#!/bin/bash

mkdir -p log

# Set version to 3.7.3

python ffnn.py | tee log/ffnn.log
python lstm.py | tee log/lstm.log

# Reset version
