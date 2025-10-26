import requests
from datetime import datetime

MY_LAT = 20.574672
MY_LONG = -103.439353


def is_ISS_close() -> bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if ((iss_latitude - 5) <= MY_LAT <= (iss_latitude + 5)) and ((iss_longitude - 5) <= MY_LONG <= (iss_longitude + 5)):
        return True
    
    return False


def is_it_dark() -> bool:
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, #this turns OFF 12-hour time display and shows it in 24-hour Unix format
    "tzid": "America/Mexico_City" #for my location, this is the closest time zone ID
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    curr_time_hour = time_now.hour
    
    if curr_time_hour >= sunset_hour and curr_time_hour <= sunrise_hour:
        return True
    
    return False


#Your position is within +5 or -5 degrees of the ISS position.

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
# print(f'My latitude is: {MY_LAT} and ISS latitude is: {iss_latitude}')
# print(f'My longitude is: {MY_LONG} and ISS longitude is: {iss_longitude}')
# print(f'Current time now at my location is: {time_now} and sunset is at: {data["results"]["sunset"]}')

if is_ISS_close() and is_it_dark():
    print("ISS is close to your current position AND it is currently DARK!!")
    print("Sending you email...")
else:
    print("Either ISS is not +5 or -5 from your position OR it is not yet dark (sun has NOT set yet!!)")


