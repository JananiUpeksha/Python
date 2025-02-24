import requests

url = 'https://httpbin.org/post'
# Credentials
username = 'user'
password = 'pass'

# Sending POST request with basic auth
response = requests.post(url, auth=(username, password))

if response.status_code == 200:
    print('Authentication successful')
    print(response.text)
else:
    print('Authentication failed', response.status_code)
