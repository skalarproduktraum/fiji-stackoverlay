#!/bin/sh

FIJI_PATH="/Applications/Fiji.app"

if [ ! -d $FIJI_PATH ]; then
    echo "Fiji.app does not exist in /Applications. Please specify the path to Fiji.app manually as argument, e.g. $0 /path/to/Fiji.app"
    exit 1
fi

IJ_JAR=`ls $FIJI_PATH/jars | grep 'ij-' | head -n1`
JYTHON_INTERPRETER_JAR=`ls $FIJI_PATH/plugins | grep 'Jython_Interpreter' | head -n1`
FIJI_SCRIPTING_JAR=`ls $FIJI_PATH/jars | grep 'fiji-scripting-' | head -n1`

javac -classpath .:$FIJI_PATH/jars/$IJ_JAR:$FIJI_PATH/jars/$FIJI_SCRIPTING_JAR:$FIJI_PATH/plugins/$JYTHON_INTERPRETER_JAR JythonLauncher.java

if [ ! "$?" = "0" ]; then
    echo "Build failed. Please check javac output for errors"
    exit 1
fi

