from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for city in sheet_data:
        city["iataCode"] = flight_search.get_destination_code(city["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_tomorrow = tomorrow + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        tomorrow,
        six_month_from_tomorrow
    )
    if flight is None:
        continue
    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_customer_emails(destination["email"])
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        message = (f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                   f" to {flight.destination_city}-{flight.destination_airport},"
                   f" from  {flight.out_date} to {flight.return_date}.")
        if flight.stop_overs > 0:
            message += f"{flight.stop_overs} stopovers, via {flight.via_city}."
            print(message)
        notification_manager.send_emails(emails, message)
