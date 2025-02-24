"""
Fetch a website check if the req was succefull, and extract the main handling text from the page's content.
You can assume that the base url is http://example.com
"""
import requests
from bs4 import BeautifulSoup

url = 'https://example.com/'
response =  requests.get(url)

if response.status_code == 200:
    text = response.text
    
    # Parse the HTML document with BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    h1_tag = soup.find('h1')    

    if h1_tag:
        print(h1_tag)
    else:
        print('h1 Tag not found')
    
     
else:
    print(f"Request failed with status code: {response.status_code}")