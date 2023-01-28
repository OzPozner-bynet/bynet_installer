#!/usr/bin/env python3


import requests, os



# Global variables
URL_PREFIX = "https://bynetawsmarketplace.s3.eu-west-1.amazonaws.com/bynet-installer/jira-install.sh"
PATH_PREFIX = "/tmp/"

def download_file(obj_url):
    """
    @obj_url: Object URL from S3 bucket to download
    :return: Downlads a new script gile and saves it in /tmp/ directory
    """
    response = requests.get(obj_url)
    local_file_path = PATH_PREFIX + "/" +str(obj_url.split("/")[4])
    with open (local_file_path, "wb") as file:
         file.write(response.content)



