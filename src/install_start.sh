#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern. 
source /opt/bynet_installer/bin/activate
if pgrep -x "python" > /dev/null
then
    echo "Running"
    exit 0
else
    echo "Stopped - restarting"
    directory_path="/opt/bynet_installer/src"
    if [ -d "$directory_path" ]; then
      echo "running from $directory_path"
      python $directory_path/aws_info.py 
      python $directory_path/app.py 
    fi   
    directory_path="~/bynet_installer/src"
    if [ -d "$directory_path" ]; then
      echo "running from $directory_path"
      python $directory_path/aws_info.py
      python $directory_path/app.py 
    fi
fi
if pgrep -x "python" > /dev/null
then
    echo "Running"
    exit 0
else
    echo "didn't find app.py"
    exit 1
fi    