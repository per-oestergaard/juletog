#!/bin/bash

echo "run.sh"

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`
LOG_DIR="$SCRIPT_DIR/logs"
mkdir -p $LOG_DIR

while :
do
echo "run.sh"
git pull
  sudo python $SCRIPT_DIR/run.py > $LOG_DIR/run.log 2> $LOG_DIR/run.err
  echo "---------"
  echo "run.log"
  cat $LOG_DIR/run.log
  echo "-----"
  echo "run.err"
  cat $LOG_DIR/run.err
  sleep 10s
done
