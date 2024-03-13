#!/bin/bash
sudo cd /opt
sudo git clone https://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@github.com/OzPozner-bynet/bynet_installer.git
sudo cd /opt/bynet_installer
sudo chmod a+x /opt/bynet_installer/which_cloud.sh
sudo /opt/bynet_installer/which_cloud/which_cloud.sh
sudo python /opt/bynet_installer/src/aws_info.py
sudo chmod a+x /opt/bynet_installer/src/install_start.sh
sudo cp /opt/bynet_installer/src/bynet_installer.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable bynet_installer.service
sudo systemctl start bynet_installer.service
