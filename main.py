from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Ask the users for their information

print("""Welcome to Zakaria's Flight Club.
We find the best flight deals and email you.""")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")


def do_email_validation():
    is_not_match = True
    while is_not_match:
        email = input("What is your email?\n")
        second_email = input("What is your email again?\n")
        if email == second_email:
            is_not_match = False
            print("You're in the club!")
            return email
        else:
            print("You're wrong,try again.")


email = do_email_validation()

data_manager = DataManager()
email_list = data_manager.get_users_email()
data_manager.add_user(first_name=first_name, last_name=last_name, email=email)
flight_data = FlightData()
send_message = NotificationManager()

DEPARTURE_CITY = "London"  # type your city here
data_manager.update_AITI()
cities = data_manager.cities_lowestPrices_dict
for city in cities:
    city_IATA = flight_data.get_city_IATA(city)
    city_lowest_price = cities[city]
    try:
        flight_search = FlightSearch(flay_from="LON", flay_to=city_IATA)
        flight_deal_price = flight_search.get_price()
    except TypeError:
        continue
    print(city, ":", "£", city_lowest_price)
    is_lowest = flight_data.check_lowest_prices(deal_price=flight_deal_price, lowest_price=city_lowest_price)
    if is_lowest:
        for email in email_list:
            departure_airport_IATA_code = flight_search.departure_airport_IATA
            destination_airport_IATA = flight_search.destination_airport_IATA
            date_arrival = flight_search.date_flight_departure
            date_departure = flight_search.tomorrow.strftime("%Y-%m-%d")
            send_message.send_message(
                to_adders=email,
                departure_airport_IATA_code=departure_airport_IATA_code,
                destination_airport_IATA_code=destination_airport_IATA,
                departure_city=DEPARTURE_CITY,
                destination_city=city,
                flight_price=flight_deal_price,
                data_departure=date_departure,
                data_arrival=date_arrival,
                stop_overs=flight_search.stop_overs,
                via_city=flight_search.via_city
            )
        break
