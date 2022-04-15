type="module"
import requests

response = requests.get('https://g21z1pb3pa.execute-api.us-east-1.amazonaws.com/prod')
response.status_code
200
response = requests.post('https://g21z1pb3pa.execute-api.us-east-1.amazonaws.com/prod')
print(response.json())
if response.status_code == 404:
    print("Result not found!")
    # Code here will react to failed requests
