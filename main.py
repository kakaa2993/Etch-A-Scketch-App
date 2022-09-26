#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


DEPARTURE_CITY = "London" # type your city here
data_manager = DataManager()
cities = data_manager.cities_lowestPrices_dict
flight_data = FlightData()
send_message = NotificationManager()
for city in cities:
    city_IATA = flight_data.get_city_IATA(city)
    flight_search = FlightSearch(flay_from="LON", flay_to=city_IATA)
    city_lowest_price = cities[city]
    flight_deal_price = flight_search.get_price()
    is_lowest = flight_data.check_lowest_prices(deal_price=flight_deal_price, lowest_price=city_lowest_price)

    if is_lowest:
        print(f"send message {city}")
        departure_airport_IATA_code = flight_search.departure_airport_IATA
        destination_airport_IATA = flight_search.destination_airport_IATA
        date_arrival = flight_search.date_flight_departure
        date_departure = flight_search.tomorrow.strftime("%Y-%m-%d")
        send_message.send_message(
            departure_airport_IATA_code=departure_airport_IATA_code,
            destination_airport_IATA_code=destination_airport_IATA,
            departure_city=DEPARTURE_CITY,
            destination_city=city,
            flight_price=flight_deal_price,
            data_departure=date_departure,
            data_arrival=date_arrival
            )
        break


