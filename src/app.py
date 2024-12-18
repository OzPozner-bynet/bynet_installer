#!/usr/bin/env python3

# External modules
from flask import Flask, render_template, request, flash, redirect, url_for
import secrets, datetime, pytz, requests, logging
import dotenv, os, json 
from dotenv import load_dotenv, dotenv_values
import boto3  # Import boto3 for AWS interaction (optional)
import requests

# Internal modules
import list_packages, downloader


# Global variables
TEMPLATES_FOLDER = "../templates"
EXPOSED_PORT = 8080
HOST = "0.0.0.0"

# Load environment variables from .env
def load_env():
    try:
        with open('/opt/bynet_installer/src/.env') as f:
	        for line in f:
	            key, value = line.strip().split('=')
	            os.environ[key] = value
	            #print(line)
    except FileNotFoundError as e:
        print(f"Error: .env file not found: {e}")

load_env()

# Function to detect cloud provider (modify based on your logic)
def get_cloud_provider():
    if 'CLOUD_PROVIDER' in os.environ:
        return os.environ['CLOUD_PROVIDER']
    elif 'PROJECT ID' in os.environ:
        return 'GCP'
    elif 'GCP_PROJECT_ID' in os.environ:
        return 'GCP'
    elif 'AWS_ACCESS_KEY_ID' in os.environ:
        return 'AWS'
    else:
        return 'Unknown'

# Time zone configuration
tz = pytz.timezone("Asia/Jerusalem")


# App config
app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
app.config['SECRET_KEY'] = secrets.token_hex(16)

logging.basicConfig(level=logging.DEBUG)
def create_log(data, logType):
    ts = datetime.datetime.now()
    if logType == "ERROR":
        app.logger.error(" |{}| {}".format(ts, data))
    elif logType == "WARN":
        app.logger.warning(" |{}| {}".format(ts, data))
    elif logType == "INFO":
        app.logger.info(" |{}| {}".format(ts, data))

# Page not found (404) handler
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


# Installer route - main application route
@app.route("/", methods=["GET", "POST"])
def installer():
    """
    :return: - GET: installer web page to  select a package.
             - POST: package instalation script downloaded on client machine.
    """

    if request.method == "POST":
        package = request.form.get("package-select")
        package_url = list_packages.get_packages()[package]
        downloader.download_file(package_url)
        package_file_key = package_url.split("/")[4]
        return render_template("success.html", package=package, package_file_key=package_file_key)

    if request.method == "GET":
        packages = list(list_packages.get_packages().keys())
        return render_template("installer.html", packages=packages)


# Details form page
@app.route("/details", methods=["GET", "POST"])
def details():
    """
    :return: - GET: details form web page.
             - POST: new client record has been inserted into package_installer database.
    """

    if cloud_provider == "AWS":
        if "EC2_INSTANCE_ID" not in dotenv_values():
            token = requests.put("http://169.254.169.254/latest/api/token", headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}).text
            ec2_instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id", headers={"X-aws-ec2-metadata-token": token}).text
        else:
            ec2_instance_id = os.getenv("EC2_INSTANCE_ID")
            print(f"AWS Instance ID (from .env): {ec2_instance_id}")
        if "EC2_INSTANCE_ID" not in dotenv_values():
            token = requests.put("http://169.254.169.254/latest/api/token", headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"}).text
            ec2_instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id", headers={"X-aws-ec2-metadata-token": token}).text
            inJSONtext= requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document", headers={"X-aws-ec2-metadata-token": token}).text
            inJSON = json.loads(inJSONtext)
            aws_account_id = inJSON["accountId"]
        else:
            aws_account_id = os.getenv("AWS_ACCOUNT_ID")
            print(f"AWS Account ID (from .env): {aws_account_id}")
    if cloud_provider == "GCP":
        ec2_instance_id = instance_id
        aws_account_id = gcp_account_id

    if request.method == "POST":
        try:
            # Retreive form data
            timestamp = datetime.datetime.now(tz)
            company_name = request.form["company_name"]
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]
            phone_number = request.form["phone_number"]
            package = request.form["package-select"]

            # Retreive EC2 instance ID
            # Send a POST request to Bynet
            api_key = api_key or os.getenv("API_KEY") 
            url = "https://bynetprod.service-now.com/api/x_bdml_nimbus/v1/nimbus_api/new_lic"
            headers = {"Content-Type": "application/json", "Accept": "application/json", "x_api_key": api_key, "Accept" : "application/json"}
            record = {
                "timestamp": str(timestamp),
                "company_name": str(company_name),
                "first_name": str(first_name),
                "last_name": str(last_name),
                "email": str(email),
                "phone_number": str(phone_number),
                "_package_name": str(package),
                "cloud_provider": cloud_provider,
                "aws_account_id": str(aws_account_id),
                "instance_id": str(ec2_instance_id),
                "instance_name" : instance_name,
                "zone" :zone, 
                "machine_type" : machine_type, 
                "project_id" : project_id
            }

            create_log(headers, "INFO")
            create_log(record, "INFO")
            response = requests.post(url, headers=headers, json=record).text
            licInJSON = json.loads(response)
            # Notify about successful change
            flash("Your details saved successfuly!"+response, category="success")
        except Exception as e:
            # Notify about failure in details insertion
            flash("Failed to insert your values!", category="error")
        finally:
            return redirect(url_for("installer"))


    if request.method == "GET":
        packages = list(list_packages.get_packages().keys())
        return render_template("details.html", packages = packages, account = aws_account_id , cloud_provider = cloud_provider, machine = machine_type, zone = zone, project = project_id, instance_id = instance_id, instance_name = instance_name)


if __name__ == "__main__":
    load_env()
    load_dotenv()


    try:
        api_key = api_key or "123"
    except NameError:
        print("api_key is not defined")
        api_key = "123"
    print(f"Api key = {api_key}")
    cloud_provider = get_cloud_provider()
    print(f"Cloud Provider:{cloud_provider}")
    if cloud_provider == 'GCP':
        instance_id = os.environ['INSTANCE_ID']
        instance_name = os.environ['INSTANCE_NAME']
        zone = os.environ['ZONE']
        machine_type = os.environ['MACHINE_TYPE']
        project_id = os.environ['PROJECT_ID']
        gcp_account_id = os.environ['GCP_ACCOUNT_ID']
    elif cloud_provider == 'AWS':
        # Use boto3 to fetch AWS instance information (example)
        ec2 = boto3.client('ec2')
        instance = ec2.describe_instances(InstanceIds=[os.environ['INSTANCE_ID']])['Reservations'][0]['Instances'][0]
        instance_id = instance['InstanceId']
        instance_name = instance.get('Tags', [])[0].get('Value', 'Unknown')  # Get name from tag (optional)
        zone = instance['Placement']['AvailabilityZone']
        machine_type = instance['InstanceType']
        project_id = 'N/A'  # AWS doesn't have a direct project concept
        gcp_account_id = 'N/A'  # Not applicable for AWS
    else:
        instance_id = 'Unknown'
        instance_name = 'Unknown'
        zone = 'Unknown'
        machine_type = 'Unknown'
        project_id = 'Unknown'
        gcp_account_id = 'Unknown'
    if "BYNET_INSTALLER_DEBUG" not in dotenv_values():
        debugFlask = False
    else:
        debugFlask = os.getenv("BYNET_INSTALLER_DEBUG")
    app.run(host=HOST, port=EXPOSED_PORT, debug=debugFlask)
