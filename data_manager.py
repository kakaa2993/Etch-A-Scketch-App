import requests
from flight_data import FlightData
API_ENDPOINT = ""  # Type Your Own Copy of the cities Google Sheet
USERS_API_ENDPOINT = ""# Type Your Own Copy of the users Google Sheet


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.response = requests.get(url=API_ENDPOINT)
        self.cities = self.response.json()["prices"]
        self.cities_lowestPrices_dict = self.get_cities(self.cities)
        self.flight_data = FlightData()

    def get_cities(self, cities: dict) -> dict:
        self.cities_lowestPrices_dict = {city_row["city"]: city_row['lowestPrice'] for city_row in cities}
        return self.cities_lowestPrices_dict

    def update_AITI(self):
        for city in self.cities:
            if city["iataCode"] == '':
                parameter = {
                    'price': {
                        'iataCode': self.flight_data.get_city_IATA(city=city['city'])
                    }
                }
                requests.put(url=API_ENDPOINT+str(city['id']), json=parameter)

    def add_user(self, first_name, last_name, email):
        users_parameters = {
            "user": {
                'firstName': first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        requests.post(url=USERS_API_ENDPOINT, json=users_parameters)

    def get_users_email(self):
        response = requests.get(url=USERS_API_ENDPOINT,)
        email_list = [user["email"] for user in response.json()["users"]]
        return email_list
