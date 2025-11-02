import requests
import os

# Before running this program, set environment variable OWM_API_KEY
# use command -- "export OWM_API_KEY=<AP's OpenWeather API key"

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
OWM_api_key = os.environ.get("OWM_API_KEY")

#api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=be9709ae75673b58126078e9a00f88cc
weather_params = {
    "q": "Guadalajara,Mexico",
    "APPID": OWM_api_key
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(response.status_code)
#print(weather_data["weather"][0]["main"])
print(weather_data)
