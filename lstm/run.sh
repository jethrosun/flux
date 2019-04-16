#!/bin/bash

mkdir -p log

python lstm.py | tee lstm-neurons.log
#python cu-dnn-gru.py | tee test.log
