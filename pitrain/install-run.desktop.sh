mkdir -p $HOME/.config/autostart

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`
cp $SCRIPT_DIR/run.desktop $HOME/.config/autostart/run.desktop
cp $SCRIPT_DIR/lxterminal.desktop $HOME/.config/autostart/lxterminal.desktop
chmod +x $SCRIPT_DIR/run.sh
