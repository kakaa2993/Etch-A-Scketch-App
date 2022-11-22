# The Best Flight-Deals Finder

A small script that detects the best and the cheapest flight deal for the cities that you are interested to go to, and send you an email if there is a flight dead or decrease in the flight prices for the upcomming days.<br>
Also this script collect list of emails and send the flight deals to all the people in email list.


- This script use Sheety API to get all the cities that he should looking for. 
Make Your Own Copy of the Starting Google Sheet<br>
Make a copy of the Google sheet (``https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?usp=sharing``).


- It use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.<br>
You should get Kiwi Partners Flight Search API key (Free Signup) - (``https://partners.kiwi.com/``)


- If the price is lower than the lowest price listed in the Google Sheet then it send an email to all the email list in the user google sheet that you hould create and use it in ``https://sheety.co/`` to turn in to an api .

## What You Need To Run The Script

1- Use this  the Google sheet (``https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?usp=sharing``) Api.


2-You should get Kiwi Partners Flight Search API key (Free Signup) - (``https://partners.kiwi.com/``)
