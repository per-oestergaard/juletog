#!/bin/bash

echo "run2.sh"

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`
LOG_DIR="$SCRIPT_DIR/logs"
mkdir -p $LOG_DIR

while :
do
echo "git pull"
git pull
echo "python testhat.py"
python pitrain/testhat.py || { sudo mpg321 -g 50 ./pitrain/sounds/No-HAT.mp3; sleep 10; sudo reboot now; }
echo "python run.py"
sudo python $SCRIPT_DIR/run.py
echo "sleep"
sleep 10s
done
