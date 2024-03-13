#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern. 

if pgrep -x "app.py" > /dev/null
then
    echo "Running"
else
    echo "Stopped - restarting"
    python /opt/bynet_installer/src/app.py 
fi