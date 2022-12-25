#!/bin/bash
set -x
echo "`date +%H:%M:%S` run2.sh"

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`

while :
do
date %m%d
echo "`date +%H:%M:%S` git pull"
git pull
echo "`date +%H:%M:%S` python testhat.py"
python $SCRIPT_DIR/testhat.py || { sudo mpg321 -g 50 $SCRIPT_DIR/sounds/No-HAT.mp3; sleep 120; sudo reboot now; }
echo "`date +%H:%M:%S` python run.py"
sudo python $SCRIPT_DIR/run.py
echo "`date +%H:%M:%S` sleep"
sleep 10s
done
