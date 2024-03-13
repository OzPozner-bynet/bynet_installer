import os, requests, boto3
# get data from aws meta-deta
token = requests.put("http://169.254.169.254/latest/api/token", headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}).text
ec2_instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id", headers={"X-aws-ec2-metadata-token": token}).text
aws_account_id = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document", headers={"X-aws-ec2-metadata-token": token}).text
print("adding/updating in .env")
print("ec2_instance_id="+ec2_instance_id)
print("aws_account_id="+aws_account_id )
from dotenv import load_dotenv, dotenv_values
# Load environment variables from the `.env` file
load_dotenv()
# Check if 'aws_account_id' key exists
if "aws_account_id" not in dotenv_values():
  # Key not found, add it with a placeholder value (replace with your desired default)
  with open(".env", "a") as env_file:
    env_file.write("aws_account_id="+aws_account_id+"\n")
if "ec2_instance_id" not in dotenv_values():
  # Key not found, add it with a placeholder value (replace with your desired default)
  with open(".env", "a") as env_file:
    env_file.write("ec2_instance_id="+ec2_instance_id+"\n")

# Now you can access environment variables using os.getenv()
aws_account_id = os.getenv("aws_account_id")
print(f"AWS Account ID (from .env): {aws_account_id}")
ec2_instance_id = os.getenv("ec2_instance_id")
print(f"AWS Instance ID (from .env): {ec2_instance_id}")