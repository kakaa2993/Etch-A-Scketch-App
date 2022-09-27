import requests

# tequila.kiwi.com
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = ""  # Type your api key


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.parameters = None
        self.headers = None

    def get_city_IATA(self, city):
        self.parameters = {
            "term": city,
            "limit": 1,
        }
        self.headers = {
            "apikey": TEQUILA_API_KEY,
            "Content-Encoding": "gzip",
            "Content-Type": "application/json",
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=self.parameters, headers=self.headers)
        CITY_IATA = response.json()["locations"][0]["code"]
        return CITY_IATA

    def check_lowest_prices(self, deal_price, lowest_price):
        return deal_price < lowest_price
