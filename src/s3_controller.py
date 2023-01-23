#!/usr/bin/env python3

import boto3


# Global variables
BUCKET = "bynet-installer"


# Create S3 instance
s3 = boto3.client('s3')


def download_file(file_name):
    """
    @file_name: A string containing file name to download.
    :return: Downloaded <file_name> that include package installation script.
    """

    Filename = "./" + str(file_name)

    s3.download_file(
	Bucket=BUCKET, Key=file_name, Filename=Filename
    )



