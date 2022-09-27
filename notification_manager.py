import smtplib

smtp_address = "smtp.gmail.com"
my_email = ""  # Type your email
my_password = ""  # Type your password


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.smtp_address = smtp_address
        self.my_email = my_email
        self.my_password = my_password

    def send_message(self, to_adders, departure_airport_IATA_code, destination_airport_IATA_code, departure_city,
                     destination_city, flight_price, data_departure, data_arrival, stop_overs=0, via_city=""):
        google_flight_link = f"https://www.google.co.uk/flights?hl=en#flt={departure_airport_IATA_code}.{destination_airport_IATA_code}.{data_departure}*{departure_airport_IATA_code}.{destination_airport_IATA_code}.{data_arrival}"
        message = f"Only £{flight_price} to fly from " \
                  f"{departure_city}-{departure_airport_IATA_code} to {destination_city}-{destination_airport_IATA_code}," \
                  f" from {data_departure} to {data_arrival}."
        if stop_overs != 0:
            message = message + f"\nFlight has {stop_overs} stop over, via {via_city} City."
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_adders,
                msg=f"Subject:Low Price Alert!\n\n{message}\n{google_flight_link}".encode('utf-8')
                    )
        print(message)
