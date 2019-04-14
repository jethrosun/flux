#!/bin/bash

mkdir -p log



python mixed-lstm.py | tee log/mixed-lstm.log
#python cu-dnn-gru.py | tee test.log
