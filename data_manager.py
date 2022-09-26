import requests

API_ENDPOINT = ""  # Type Your Own Copy of the Starting Google Sheet


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.response = requests.get(url=API_ENDPOINT)
        self.cities_lowestPrices_dict = self.get_cities(self.response.json()["prices"])

    def get_cities(self, cities: dict) -> dict:
        self.cities_lowestPrices_dict = {city_row["city"]: city_row['lowestPrice'] for city_row in cities}
        return self.cities_lowestPrices_dict



