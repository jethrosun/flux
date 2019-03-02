#!/bin/bash

for dir in */ ; do
    echo "$dir"
    mkdir -p $dir/input
    mkdir -p $dir/trace
done
