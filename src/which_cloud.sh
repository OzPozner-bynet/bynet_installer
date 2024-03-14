#!/bin/bash

# Detect the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Check if running on GCP
    if grep -q "Google" /sys/class/dmi/id/product_name; then
        echo "Running on Google Cloud Platform (GCP)"
        # Install google module
        pip3 install google-auth google-auth-httplib2 google-auth-oauthlib
        export cloud_provider="GCP"
    elif grep -q "Amazon" /sys/class/dmi/id/sys_vendor; then
        echo "Running on Amazon Web Services (AWS)"
        # Install boto3
        #pip3 install boto3 dotenv
        export cloud_provider="AWS"
        echo 'export cloud_provider="AWS"'>>~.bashrc
    else
        echo "Unknown cloud provider"
        export cloud_provider="unknown"
    fi
else
    echo "Unsupported operating system"
    exit 1
fi

# You can now use the 'cloud_provider' environment variable in your script
echo "Cloud provider: $cloud_provider"