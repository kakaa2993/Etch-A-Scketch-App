import smtplib

smtp_address = "smtp.gmail.com"  # type your smtp_address
my_email = ""  # Type your email
my_password = ""  # Type your password


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.smtp_address = smtp_address
        self.my_email = my_email
        self.my_password = my_password

    def send_message(self, departure_airport_IATA_code, destination_airport_IATA_code, departure_city,
                     destination_city, flight_price, data_departure, data_arrival):
        message = f"Subject:Low Price Alert!\n\nOnly {flight_price} EUR to fly from " \
                  f"{departure_city}-{departure_airport_IATA_code} to {destination_city}-{destination_airport_IATA_code}," \
                  f" from {data_departure} to {data_arrival}."
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)
