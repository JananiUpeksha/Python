import requests

response = requests.get('https://api.github.com/events')

if response.status_code == 200:
    print(response)
    print(response.status_code)
    
    """
    print(response.headers)
    content_type = response.headers['Content-Type']
    print(content_type)
    """

    #print(response.text)
    if 'application/json' in response.headers.get('Content-Type', ''):
        data = response.json()
        print(data)
        print(f"Type of data: {type(data)}") 
else:
    print(f"Request failed with status code: {response.status_code}")
