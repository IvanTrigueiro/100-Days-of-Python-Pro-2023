import os
import requests
sheety_username = os.environ.get("SHEETY_USERNAME")
sheety_token = os.environ.get("SHEETY_TOKEN")
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Get Flight Data
        sheety_get_endpoint = f"https://api.sheety.co/{sheety_username}/flightDeals/prices"
        get_response = requests.get(url=sheety_get_endpoint, headers=sheety_headers)
        get_data = get_response.json()
        self.destination_data = get_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheety_put_endpoint = f"https://api.sheety.co/{sheety_username}/flightDeals/prices/{city['id']}"
            put_response = requests.put(url=sheety_put_endpoint, headers=sheety_headers, json=new_data)
            print(put_response.text)






