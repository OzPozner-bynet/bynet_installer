#!/bin/bash
cd /opt
sudo git clone https://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@github.com/OzPozner-bynet/bynet_installer.git
cd bynet_installer
sudo python src/aws_info.py
sudo chmod a+x ./install_start.sh
sudo cp ./bynet_installer.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable bynet_installer.service
sudo systemctl start bynet_installer.service
