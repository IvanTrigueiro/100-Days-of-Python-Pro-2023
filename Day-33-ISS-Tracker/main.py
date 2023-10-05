import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -7.159768
MY_LONG = -34.794959

Username = "contatesteparaprogramar@outlook.com"
Password = "your password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_overhead() and sunrise >= hour_now >= sunset:
        with smtplib.SMTP("smtp.office365.com") as connection:
            connection.starttls()
            connection.login(user=Username, password=Password)
            connection.sendmail(
                from_addr=Username,
                to_addrs=Username,
                msg="Subject: Look Up!\n\nThe ISS is above you in the sky.",
            )
