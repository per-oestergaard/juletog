#!/bin/bash

echo "`date +%H:%M:%S` run.sh"

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`
LOG_DIR="$SCRIPT_DIR/logs"
mkdir -p $LOG_DIR
log="$LOG_DIR/`date +run-%m%d.log`"
err="$LOG_DIR/`date +run-%m%d.err`"
echo "`date +%H:%M:%S` Log is $log"
echo "`date +%H:%M:%S` Err is $err"


while :
do
echo "`date +%H:%M:%S` run2.sh"
bash $SCRIPT_DIR/run2.sh >> $log 2>> $err
echo "`date +%H:%M:%S` sleep 10"
sleep 10s
done
