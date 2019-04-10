#!/bin/bash

mkdir -p log
python ffnn.py | tee log/ffnn.log
