from google.cloud import compute_v1

def get_gcp_account_and_email(project_id, zone, instance_name):
  """Gets the GCP account and email for the VM running in GCP.

  Args:
    project_id: The project ID of the GCP project.
    zone: The zone of the VM.
    instance_name: The name of the VM.

  Returns:
    A tuple containing the GCP account and email, or None if an error occurs.
  """

  try:
    # Create a Compute Engine client.
    client = compute_v1.ComputeClient()

    # Get the instance.
    instance = client.get_instance(project=project_id, zone=zone, instance=instance_name)

    # Get the service account email.
    service_account_email = instance.service_account

    # Get the GCP account ID.
    account_id = service_account_email.split('@')[1]

    return account_id, service_account_email

  except Exception as e:
    print(f'Error getting GCP account and email: {e}')
    return None

# Replace the placeholders with your actual values
project_id = 'your-project-id'
zone = 'your-zone'
instance_name = 'your-instance-name'

account_id, service_account_email = get_gcp_account_and_email(project_id, zone, instance_name)

if account_id and service_account_email:
  print(f'GCP Account ID: {account_id}')
  print(f'Service Account Email: {service_account_email}')
else:
  print('Failed to retrieve GCP account and email.')
