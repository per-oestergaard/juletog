#!/bin/bash

echo "run.sh"

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`

while :
do
echo "run.sh"
git pull
  sudo python $SCRIPT_DIR/run.py > ~/run.log 2> ~/run.err
  echo "---------"
  echo "run.log"
  cat ~/run.log
  echo "-----"
  echo "run.err"
  cat ~/run.err
  sleep 15s
done
