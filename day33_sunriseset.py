import requests
from datetime import datetime

MY_LAT = 20.574672
MY_LONG = -103.439353
#used Google Maps on my smartphone to get coordinates of my location
#press the blue pin and the coordinates will show up in the search bar.
#first number is latitude, second is longitude.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, #this turns OFF 12-hour time display and shows it in 24-hour Unix format
    "tzid": "America/Mexico_City" #for my location, this is the closest time zone ID
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f'Sunrise from API is: {sunrise}')
print(f'Sunset from API is: {sunset}')

time_now = datetime.now()

print(f'Time right now at your location is: {time_now}')

print(f'Splitting based on "T", we get 2 sub-strings -- Sunrise: {sunrise.split("T")}')
print(f'Splitting based on "T" and then ":" for the 2nd list item, we get many sub-strings -- Sunrise: {sunrise.split("T")[1].split(":")}')

# Similarly, do it for "Sunset"
# Then, split similarly for "time_now". In this case, you need to do the
# first split by 'space'.. i.e. ' '. Then, split by ':'
# idea is to get the hour part ONLY for sunrise, sunset and current time NOW at your location.
# Since Intl' Space Station (ISS) is best visible after sunset...
# Final project for this day 33 follows... see other files in this same folder!
print(f'Splitting time_now: {time_now.strftime("%H:%M:%S").split(":")}')