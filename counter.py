import requests
response = requests.get('https://g21z1pb3pa.execute-api.us-east-1.amazonaws.com/prod')
print(response.json())
