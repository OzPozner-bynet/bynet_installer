#!/bin/bash
sudo yum update -y
sudo yum install python3 pip3 -y
sudo pip install virtualenv 
virtualenv /opt/bynet_installer
source /opt/bynet_installer/bin/activate
cd /opt
sudo git clone https://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@github.com/OzPozner-bynet/bynet_installer.git
cd /opt/bynet_installer
pip install -r /opt/bynet_installer/src/requirements.txt
pip3 install -r /opt/bynet_installer/src/requirements.txt
sudo chmod a+rw /opt/bynet_installer/src/.env
sudo chmod a+x /opt/bynet_installer/src/which_cloud.sh
/opt/bynet_installer/src/which_cloud.sh
python /opt/bynet_installer/src/aws_info.py
sudo chmod a+x /opt/bynet_installer/src/install_start.sh
#on start run script using rc.local
if [  -f /etc/rc.d/rc.local ]; then
  sudo chmod +x /etc/rc.d/rc.local
  sh /opt/bynet_installer/src/install_start.sh
else  
#on start run script using systemd
  sudo cp /opt/bynet_installer/src/bynet_installer.service /etc/systemd/system/
  sudo systemctl daemon-reload
  sudo systemctl enable bynet_installer.service
  sudo systemctl start bynet_installer.service
fi
/opt/bynet_installer/src/install_start.sh