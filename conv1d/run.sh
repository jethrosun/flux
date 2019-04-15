#!/bin/bash

start=`date +%s`

python conv1d.py | tee conv1d-${start}.log

end=`date +%s`

runtime=$((end-start))

