#!/bin/bash

echo "run.sh"

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`
LOG_DIR="$SCRIPT_DIR/logs"
mkdir -p $LOG_DIR
log=date +run-%m%d.log
err=date +run-%m%d.err


while :
do
echo "run2.sh"
$SCRIPT_DIR/run2.sh >> %log% 2>> %err%
sleep 10s
done
