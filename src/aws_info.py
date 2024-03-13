import os, requests, boto3, dotenv, json
# get data from aws meta-deta
token = requests.put("http://169.254.169.254/latest/api/token", headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}).text
ec2_instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id", headers={"X-aws-ec2-metadata-token": token}).text
inJSONtext= requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document", headers={"X-aws-ec2-metadata-token": token}).text
inJSON = json.loads(inJSONtext)
print("adding/updating in .env")
print("ec2_instance_id="+ec2_instance_id)
account_id = inJSON["accountId"]
print("account_id="+account_id )
mpProductCodes = inJSON["marketplaceProductCodes"]
from dotenv import load_dotenv, dotenv_values
# Load environment variables from the `.env` file
load_dotenv()
# Check if 'aws_account_id' key exists
if "AWS_ACCOUNT_ID" not in dotenv_values():
  # Key not found, add it with a placeholder value (replace with your desired default)
  with open(".env", "a") as env_file:
    env_file.write("AWS_ACCOUNT_ID="+account_id+"\n")
if "EC2_INSTANCE_ID" not in dotenv_values():
  # Key not found, add it with a placeholder value (replace with your desired default)
  with open(".env", "a") as env_file:
    env_file.write("EC2_INSTANCE_ID="+ec2_instance_id+"\n")

# Now you can access environment variables using os.getenv()
aws_account_id = os.getenv("aws_account_id")
print(f"AWS Account ID (from .env): {aws_account_id}")
ec2_instance_id = os.getenv("EC2_INSTANCE_ID")
print(f"AWS Instance ID (from .env): {ec2_instance_id}")