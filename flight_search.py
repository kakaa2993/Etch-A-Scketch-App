import datetime
import requests

# tequila.kiwi.com
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
API_KEY = "" # Type your api key
CURRENCY = "GBP"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, flay_from: str, flay_to: str):
        self.tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        self.TOMORROW_DATE = self.tomorrow.strftime("%d/%m/%Y")
        self.NEXT_6_MONTH_DATE = (self.tomorrow + datetime.timedelta(180)).strftime("%d/%m/%Y")
        self.FLAY_FROM = flay_from
        self.FLAY_TO = flay_to
        self.parameters = None
        self.headers = None
        self.data = self.get_data()
        self.departure_airport_IATA = self.data["flyFrom"]
        self.destination_airport_IATA = self.data["flyTo"]
        self.date_flight_departure = self.data['utc_departure'].split("T")[0]

    def get_data(self):
        self.parameters = {
            "fly_from": self.FLAY_FROM,
            "fly_to": self.FLAY_TO,
            "dateFrom": self.TOMORROW_DATE,
            "dateTo": self.NEXT_6_MONTH_DATE,
            "curr": CURRENCY,
        }
        self.headers = {
            "apikey": API_KEY,
            "Content-Encoding": "gzip",
            "Content-Type": "application/json",
        }
        response = requests.get(url=KIWI_ENDPOINT, params=self.parameters, headers=self.headers)
        data = response.json()["data"][0]
        # print(data)
        return data

    def get_price(self):
        price = self.data["price"]
        return price

