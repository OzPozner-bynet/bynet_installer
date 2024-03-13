import requests

def is_running_on_cloud():
    try:
        response = requests.get('http://169.254.169.254', timeout=1)
        if response.status_code == 200:
            # Check if the response content indicates AWS or GCP
            if 'computeMetadata' in response.text:
                return "AWS"
            elif 'metadata' in response.text:
                return "GCP"
    except requests.exceptions.RequestException:
        pass
    return "unknown"
print(is_running_on_cloud())