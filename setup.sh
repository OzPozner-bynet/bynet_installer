#!/bin/bash
cd /opt
sudo git clone https://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@github.com/OzPozner-bynet/bynet_installer.git
cd /opt/bynet_installer
sudo chmod a+x /opt/bynet_installer/src/which_cloud.sh
/opt/bynet_installer/src/which_cloud.sh
pip3 install -r /opt/bynet_installer/src/requirements.txt
sudo python /opt/bynet_installer/src/aws_info.py
sudo chmod a+x /opt/bynet_installer/src/install_start.sh
sudo cp /opt/bynet_installer/src/bynet_installer.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable bynet_installer.service
#sudo systemctl start bynet_installer.service
