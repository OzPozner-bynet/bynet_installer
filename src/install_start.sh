#!/bin/bash

# Check if gedit is running
# -x flag only match processes whose name (or command line if -f is
# specified) exactly match the pattern. 
file_path="/opt/bynet_installer/.venv/bin/activate"

if [ -f "$file_path" ]; then
  echo "sourced .venv"
  source "$file_path"
fi

file_path="/opt/bynet_installer/bin/activate"
if [ -f "$file_path" ]; then
  echo "sourced /opt"
  source "$file_path"
fi

if pgrep -x "python" > /dev/null
then
    echo "found python Running before update not updateing"
    #exit 0
fi
echo "checking /opt dir"
file_path="/opt/bynet_installer"
if [ -d "$file_path" ]; then
    echo "updating /opt"
    directory_path="/opt/bynet_installer/src"
    if [ -d "$directory_path" ]; then
      echo "running from $directory_path"
      cd $directory_path
      cd ..
      git pull
      cd $directory_path
      $directory_path/gcp.sh
      python $directory_path/app.py 
    fi
    echo " updating from installer path ~"
    directory_path="~/bynet_installer/src"
    if [ -d "$directory_path" ]; then
      echo "running from $directory_path"
      cd $directory_path
      cd ..
      git pull
      sudo chmod a+x setup.sh
      ./setup.sh
      cd $directory_path
      directory_path="/opt/bynet_installer/src"
      cd $directory_path
      $directory_path/gcp.sh
      python $directory_path/app.py 
    fi
fi
if pgrep -x "python" > /dev/null
then
    echo "found python Running on Exit"
else
    echo "didn't find python running on exit running from  $directory_path"
    exit 1
fi
