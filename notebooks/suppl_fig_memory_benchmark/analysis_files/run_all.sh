#!/usr/bin/env bash

set -e

for SIZE in `seq 100000 10000 100000`; do
  for SPLIT in `seq 0 1 9`; do
    bash _run.sh $1 $SIZE $SPLIT $1
  done
done
