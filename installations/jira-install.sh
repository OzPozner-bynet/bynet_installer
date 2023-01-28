#!/bin/bash

# download jira
cd /opt
wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-7.3.0-x64$

# make it executable
chmod a+x atlassian-jira-software-7.3.0-x64.bin

# run installation script
./atlassian-jira-software-7.3.0-x64.bin

# remove jira-install.sh
rm -rf /tmp/jira-install.sh
