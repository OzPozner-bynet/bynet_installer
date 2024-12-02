#!/bin/bash

#change to check if /etc/os-relase contain ID_LIKE=fedora
if grep -qEi 'id_like=.*debian.*' /etc/os-release; then
    echo "This system is like Debian."
    sudo apt update -y
    sudo apt install python3-is-python python3-pip -y
    sudo apt-get update -y
    sudo apt-get install cron -y
elif grep -qEi 'id_like=.*fedora.*' /etc/os-release; then
    echo "This system is like Fedora."
    sudo yum update -y
    sudo yum install python3 python3-pip -y
    sudo yum install cronie -y
else
    echo "This system is not like Debian or Fedora."
    echo "please contact oz at 972-548-949464"
fi

#install venv
sudo pip install virtualenv  
#clone installer
cd /opt
sudo git clone https://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@github.com/OzPozner-bynet/bynet_installer.git
sudo virtualenv /opt/bynet_installer
source /opt/bynet_installer/.venv/bin/activate
cd /opt/bynet_installer
pip install -r /opt/bynet_installer/src/requirements.txt
#pip3 install -r /opt/bynet_installer/src/requirements.txt
sudo chmod a+rw /opt/bynet_installer/src/.env
sudo chmod a+x /opt/bynet_installer/src/which_cloud.sh
/opt/bynet_installer/src/which_cloud.sh
sudo python /opt/bynet_installer/src/aws_info.py
sudo chmod a+x /opt/bynet_installer/src/install_start.sh
#on start run script using rc.local
if [  -f /etc/rc.d/rc.local ]; then
  sudo chmod +x /etc/rc.d/rc.local
  sh /opt/bynet_installer/src/install_start.sh
else  
#on start run script using systemd
  if [ -d /run/systemd/system  ]; then
    echo "install reboot using systemd"
    sudo cp /opt/bynet_installer/src/bynet_installer.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl enable bynet_installer.service
    sudo systemctl start bynet_installer.service
  else
    echo "installing reboot using crontab"
    NEW_CRON_LINE="@reboot /opt/bynet_installer/src/install_start.sh"
    echo "$NEW_CRON_LINE" | crontab -l | cat - | sudo crontab -
  fi  
fi
echo "to start please run:"
echo "/opt/bynet_installer/src/install_start.sh"
echo "auto starting ..."
/opt/bynet_installer/src/install_start.sh
