#!/bin/bash

ENV="/opt/bynet_installer/src/.env"

# Get instance metadata
INSTANCE_ID=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/id)
INSTANCE_NAME=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/name)
ZONE=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/zone)
MACHINE_TYPE=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/machine-type)
PROJECT_ID=$(curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/project/project-id)

# Get GCP Account ID (requires gcloud CLI)
GCP_ACCOUNT_ID=$(gcloud config get-value account)

# Create the .env file and write the variables
echo "INSTANCE_ID=$INSTANCE_ID" > "$ENV"
echo "INSTANCE_NAME=$INSTANCE_NAME" >> "$ENV"
echo "ZONE=$ZONE" >> "$ENV"
echo "MACHINE_TYPE=$MACHINE_TYPE" >> "$ENV"
echo "PROJECT_ID=$PROJECT_ID" >> "$ENV"
echo "GCP_ACCOUNT_ID=$GCP_ACCOUNT_ID" >> "$ENV"

# Source the .env file
source "$ENV"

# Echo the variables
echo "Instance ID: $INSTANCE_ID"
echo "Instance Name: $INSTANCE_NAME"
echo "Zone: $ZONE"
echo "Machine Type: $MACHINE_TYPE"
echo "Project ID: $PROJECT_ID"
echo "GCP Account ID: $GCP_ACCOUNT_ID"
