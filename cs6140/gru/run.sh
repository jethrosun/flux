#!/bin/bash

start=`date +%s`

python gru.py | tee gru-${start}.log

end=`date +%s`

runtime=$((end-start))

