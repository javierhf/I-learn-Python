# API Description  
# Show weather information from public weather API
# from flask import Flask, request ONLY for Flask APIs. This is not a Flask API, is consuming an external API

# import libraries, modules  
import requests

# Openweather API Map data structure    

weather_data= {
  "coord": {
    "lon": 10.99,
    "lat": 44.34
  },
  "weather": [
    {
      "id": 501,
      "main": "Rain",
      "description": "moderate rain",
      "icon": "10d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 298.48,
    "feels_like": 298.74,
    "temp_min": 297.56,
    "temp_max": 300.05,
    "pressure": 1015,
    "humidity": 64,
    "sea_level": 1015,
    "grnd_level": 933
  },
  "visibility": 10000,
  "wind": {
    "speed": 0.62,
    "deg": 349,
    "gust": 1.18
  },
  "rain": {
    "1h": 3.16
  },
  "clouds": {
    "all": 100
  },
  "dt": 1661870592,
  "sys": {
    "type": 2,
    "id": 2075663,
    "country": "IT",
    "sunrise": 1661834187,
    "sunset": 1661882248
  },
  "timezone": 7200,
  "id": 3163858,
  "name": "Zocca",
  "cod": 200
}  


# When consuming an external API:
# 1) we DO NOT create a Flask app (app = Flask(__name__) )
# 2) we do not define endpoints/methods: we pass the base url and parameters

# BY CITY NAME request: https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# /weather?city={city=city_name} GET all weather info DEPRECATED but still in use

# BY LON LAT https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# Define function to get the data I want from the weather info API

def get_weather_info(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    # Parameters from the weather API data structure I want to consume
    parameters = {
        "appid": api_key, # Api key
        "q": city_name,
        "units": "metric",
        # "lat": 27.7576,
        # "lon": -15.5841,
        # "zip": "35100"
        }

    response_data = requests.get(base_url, params = parameters)
    response_status_code = response_data.status_code

    if response_status_code == 200:
        return response_data.json()
    else:
        return {"Request response error": response_status_code}

#  Check if the Python script is being run directly (not imported as a module in another script). 
# If the script is being executed directly, the code within this block will run. 
# This is a common idiom in Python to ensure that certain code is only executed when the script is run directly, 
# and not when it is imported.`

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = <you api key here> 
    weather_info = get_weather_info(city, api_key)
    print(weather_info)

# /forecast/?city={city_name} GET query by {city}