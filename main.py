import phonenumbers
from colorama import init
from phonenumbers import geocoder
from termcolor import colored
init()
print(" ")
print(colored(" ███    ██     ██ ███    ██ ███████  ██████   ", "red"))
print(colored(" ████   ██     ██ ████   ██ ██      ██    ██  ", "magenta"))
print(colored(" ██ ██  ██  -  ██ ██ ██  ██ █████   ██    ██  ", "yellow"))
print(colored(" ██  ██ ██     ██ ██  ██ ██ ██      ██    ██  ", "green"))
print(colored(" ██   ████     ██ ██   ████ ██       ██████   ", "blue"))
print(" ")
print(colored(" Number Service Shower & Country @Paul 2021", "green"))
print(" ")
number = input(" Number: ")
de_nmber = phonenumbers.parse(number, "DE")
print(geocoder.description_for_number(de_nmber, "de"))
from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "de"))