#!/usr/bin/env python3
import json
import requests
import os
from dotenv import load_dotenv

def get_packages():
  api_key = os.getenv("API_KEY")
  aws_account_id = os.getenv("AWS_ACCOUNT_ID")
  snow_url = os.getenv("SNOW_URL")
  url = f"{snow_url if snow_url else 'https://bynetprod.servicenow.com/api/x_bdml_nimbus/v1/nimbus_api/'}get_packages"
  # Set headers with your API key
  headers = {"x-api-key": api_key, "Accept" : "application/json"}
  # Set parameters
  params = {"aws_account_id": aws_account_id}

  # Send GET request with headers and parameters
  response = requests.get(url, headers=headers, params=params)

  # Check for successful response
  if response.status_code == 200:
    # Parse JSON response
    data = json.loads(response.text)
    #print(data)
    packages = data
  else:
    print("Error:", response.status_code)
    packages = {
       "Can't find packages for Account ID "+aws_account_id + " please request private offer": "x",
    }
  return packages

