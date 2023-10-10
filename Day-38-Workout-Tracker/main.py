import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 138
HEIGHT_CM = 177
AGE = 30

# Get environment variables for nutritionix
nutri_api_id = os.environ["NUTRI_API_ID"]
nutri_api_key = os.environ["NUTRI_API_KEY"]
nutri_url_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Get environment variables for sheety
sheety_username = os.environ["SHEETY_USERNAME"]
sheety_url_endpoint = f"https://api.sheety.co/{sheety_username}/myWorkouts/workouts"
sheety_token = os.environ["SHEETY_BEARER_TOKEN"]

# Set headers
nutri_headers = {
    "x-app-id": nutri_api_id,
    "x-app-key": nutri_api_key,
    "x-remote-user-id": "0",
}
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

# Get user input
user_input = input("Tell me what exercises you did: ")
nutri_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=nutri_url_endpoint, json=nutri_params, headers=nutri_headers)
result = response.json()

# For each item in response.json()["exercises"] get the name, duration and calories
for item in result["exercises"]:
    # Get exercise_name
    exercise_name = item["name"].title()
    # Get duration
    duration = int(item["duration_min"])
    # Get calories
    calories = int(item["nf_calories"])

    # Send data to sheety
    today = datetime.today().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%X")
    sheety_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories

        }
    }
    sheety_response = requests.post(url=sheety_url_endpoint, json=sheety_params, headers=sheety_headers)
    print(sheety_response.text)
