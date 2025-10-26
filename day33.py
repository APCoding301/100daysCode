import requests

#Below is the correct endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")

#Below, the endpoint is misspelled to demonstrate error handling
#response = requests.get(url="http://api.open-notify.org/is-now.json")

#print(response)
#raise_for_status()  # This will raise an error/exception for bad responses.
#check the terminal for the error message(s)
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude) #create a tuple

print(f"The ISS is currently at (longitude, latitude) --> {iss_position}.")

