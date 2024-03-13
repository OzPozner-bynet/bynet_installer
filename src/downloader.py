#!/usr/bin/env python3

import dotenv 
from dotenv import load_dotenv
import requests, os

# Global variables
url_prefix = os.getenv("URL_PREFIX")
URL_PREFIX = "https://bynetawsmarketplace.s3.eu-west-1.amazonaws.com/bynet-installer/"
path_prefix = os.getenv("PATH_PREFIX")
PATH_PREFIX = "/tmp/"
path_prefix = f"{ path_prefix if path_prefix else PATH_PREFIX }"
url_prefix = f"{ url_prefix if url_prefix else URL_PREFIX }"
def download_file(obj_url):
    """
    @obj_url: Object URL from S3 bucket to download
    :return: Downlads a new script gile and saves it in /tmp/ directory
    """
    response = requests.get(obj_url)
    local_file_path = PATH_PREFIX + "/" +str(obj_url.split("/")[4])
    with open (local_file_path, "wb") as file:
         file.write(response.content)



