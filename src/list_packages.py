#!/usr/bin/env python3
import json
import requests
import os
import dotenv 
from dotenv import load_dotenv

def get_packages():
  try:
    load_dotenv()
    api_key = os.getenv("API_KEY") or  "123"
    aws_account_id = os.getenv("AWS_ACCOUNT_ID") or "umbrella"
    snow_url = os.getenv("SNOW_URL")
    url = f"{snow_url if snow_url else 'https://bynetprod.service-now.com/api/x_bdml_nimbus/v1/nimbus_api/'}get_packages"
    # Set headers with your API key
    headers = {"x_api_key": api_key, "Accept" : "application/json"}
    # Set parameters
    params = {"aws_account_id": aws_account_id, "cloud_provider": "GCP"}

    # Send GET request with headers and parameters
    response = requests.get(url, headers=headers, params=params)
    
    # Check for successful response
    if response.status_code == 200:
      # Parse JSON response
      data = json.loads(response.text)
      #print(data)
      packages = data['result']
      print(f"repsone packages { packages} \n params: \n {params}")
    else:
      print("Error:", response.status_code)
      print("Error Message: ", response.text)
      packages = {
         f"Can't find packages for Account ID: {aws_account_id if aws_account_id else 'unknown account id '} please request private offer": "x",
      }
    return packages
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")  # Print the exception message, which includes the status code and response text


