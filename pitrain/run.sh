#!/bin/bash

echo "run.sh"

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`

python $SCRIPT_DIR/run.py
