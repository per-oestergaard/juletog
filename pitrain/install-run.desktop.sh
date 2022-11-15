mkdir $HOME/.config/autostart

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`
cp $SCRIPT_DIR/run.desktop $HOME/.config/autostart/run.desktop
