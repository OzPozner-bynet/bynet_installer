from google.auth import default
from google.auth.transport.requests import Request
from google.auth.credentials import Credentials

# Get default credentials
credentials, _ = default()

# Access the IAM API using credentials
# Example: Get the current authenticated account's email
email = credentials.get_account_info().email
info = credentials.get_account_info(
print(f"Authenticated account email: {email}")
print(f"Authenticated account info: {info}")