import requests
import os
from flight_data import FlightData
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
tequila_key = os.environ["TEQUILA_API_KEY"]
tequila_headers = {
    "apikey": tequila_key
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name: str):
        tequila_params = {
            "term": city_name,
            "location_types": "city",
        }
        tequila_get_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        tequila_response = requests.get(url=tequila_get_endpoint, headers=tequila_headers, params=tequila_params)
        tequila_data = tequila_response.json()["locations"][0]["code"]
        return tequila_data

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        tequila_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }
        url = f"{TEQUILA_ENDPOINT}/v2/search"
        tequila_response = requests.get(url=url, headers=tequila_headers, params=tequila_params)

        try:
            tequila_data = tequila_response.json()["data"][0]
        except IndexError:
            tequila_params["max_stopovers"] = 2
            tequila_response = requests.get(url=url, headers=tequila_headers, params=tequila_params)
            tequila_data = tequila_response.json()["data"][0]
            flight_data = FlightData(
                price=tequila_data["price"],
                origin_city=tequila_data["route"][0]["cityFrom"],
                origin_airport=tequila_data["route"][0]["flyFrom"],
                destination_city=tequila_data["route"][0]["cityTo"],
                destination_airport=tequila_data["route"][0]["flyTo"],
                out_date=tequila_data["route"][0]["local_departure"].split("T")[0],
                return_date=tequila_data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=tequila_data["price"],
                origin_city=tequila_data["route"][0]["cityFrom"],
                origin_airport=tequila_data["route"][0]["flyFrom"],
                destination_city=tequila_data["route"][0]["cityTo"],
                destination_airport=tequila_data["route"][0]["flyTo"],
                out_date=tequila_data["route"][0]["local_departure"].split("T")[0],
                return_date=tequila_data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data

