#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern. 

if pgrep -x "app.py" > /dev/null
then
    echo "Running"
    exit 0
else
    echo "Stopped - restarting"
    directory_path="/opt/bynet_installer/src"
    if [ -d "$directory_path" ]; then
      echo "running from $directory_path"
      python $directory_path/app.py &
      exit 0
    fi   
    directory_path="~/bynet_installer/src"
    if [ -d "$directory_path" ]; then
      echo "running from $directory_path"
      python $directory_path/app.py &
      exit 0
    fi
    directory_path="~/bynet_installer/bynet_installer/src"
    if [ -d "$directory_path" ]; then
      echo "running from $directory_path"
      python $directory_path/app.py &
      exit 0
    fi
fi
echo "didn't find app.py"
exit 1