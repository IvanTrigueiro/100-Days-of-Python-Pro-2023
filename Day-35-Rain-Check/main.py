import requests
import os
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
api_key = os.environ["API_KEY"]
my_number = os.environ["MY_NUMBER"]
twilio_number = os.environ["TWILIO_NUMBER"]

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

params = {
    "lat": -28.678301,
    "lon": -49.370399,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

# Check id of weather for the next 12 hours
weather_slice = weather_data["hourly"][:12]
for hour in weather_slice:
    weather_id = hour["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=f"+{twilio_number}",
        to=f"+{my_number}"
    )
    print(message.status)

