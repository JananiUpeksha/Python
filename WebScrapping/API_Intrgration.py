import requests

"""
# Correct API base URL
base_url = 'https://api.open-meteo.com/v1/forecast'

# Parameters for the API request
params = {
    'latitude': 51.5070,         
    'longitude': -0.1278,        
    'current_weather': 'true',   
}

# Sending the GET request
response = requests.get(base_url, params=params)

if response.status_code == 200:
    # Access and print the JSON response as a dictionary
    weather_data = response.json()
    print(weather_data)
else:
    print(f"Request failed with status code: {response.status_code}")

"""


"""
def fetch_weather(latitude,longitude,current_weather = 'true'):
    base_url = 'https://api.open-meteo.com/v1/forecast'

    params = {
        'latitude': latitude,         
        'longitude': longitude,        
        'current_weather': current_weather   
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()
    print(weather_data)


fetch_weather(51.5070, -0.1278)
"""

#with a function
def fetch_wheather(latitude,longitude,current_info):
    base_url = 'https://api.open-meteo.com/v1/forecast'

    param = {
    'latitude':latitude,
    'longitude':longitude,
    'current': current_info
    }

    response = requests.get(base_url, params=param)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

print(fetch_wheather(51.5074,-0.1278,'temperature_2m'))

#parse
def parse_weather_data(data):
    if data and 'current_weather' in data:
        temperature = data['current_weather'].get('temperature', None) 
        if temperature is not None:
            print(f"The current temperature is {temperature}°C.")
        else:
            print("Temperature information is not available.")
    else:
        print("Invalid weather data or missing 'current_weather' section.")

# Fetch and parse the weather data
fetched_data = fetch_wheather(51.5074, -0.1278, 'temperature')
parse_weather_data(fetched_data)

d
    