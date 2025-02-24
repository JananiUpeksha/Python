import requests
data = {'username':'user','password':'pass'}
response = requests.post('https://httpbin.org/post',data)

if response.status_code == 200:
    print('Login successfull')
    print(response.text)

    print('-------------- URL PARAMETERS----------------')
    #Example url
    url = 'https://example.com/search'
    #Params need to send
    params = {'q':'python','category':'books'}
    #Making reuest
    response = requests.get(url, params = params)
    #Actual url - https://example.com/search?q=python&category=books
    print(response.url)
    print(response.text)

else:
    print('Loggin failed',response.status_code)

