import csv
from pprint import pprint

with open('flightTime.csv') as rawData:
    print(rawData.read())

with open('flightTime.csv') as data:
    for line in csv.reader(data):
        print(line)

with open('flightTime.csv') as data:
    for line in csv.DictReader(data):
        print(line)

# aim : read it into a single dictionary
with open('flightTime.csv') as data:
    ignore = data.readline()  # ignoreing the header info
    flights = {}  # new empty dictionary
    for line in data:
        k, v = line.strip().split(',')  # Break apart the line at the comma, which returns two values: the key (flight time) and value (destination).
        # strip is used to remove unwanted triling newline
        flights[k] = v
print()
print(flights)
print()
pprint(flights)

# Aim 1: Convert the flight times from 24-hour format to AM/PM format
# Aim 2: Convert the destinations from UPPERCASE to Titlecase
# Aim 3: data should be presented with single destinations as keys and a list of flight times as values

from datetime import datetime

def convert2ampm(time24: str) -> str:
    return datetime.strftime(time24,'%H:%M').strftime("I%:%M%p")

with open('flightTime.csv') as data:
    ignore2 = data.readline()
    flights2 = {}
    for line in data:
        k, v = line.strip().split(',')
        flights2[k] = v

    pprint(flights2)
    print()

    flights_v2 = {}
    for k, v in flights_v2.items():
        flights_v2[convert2ampm(k)] = v.title()
    pprint(flights_v2)

# Learning Comprehension

destinations = []
for dest in flights.values():
    destinations.append(dest.title())
# Implementing comprehension
more_dests = [dest2.title() for dest2 in flights.values()]

"""flight_times = []
for ft in flights.keys():
    flight_times.append(convert2ampm(ft))"""
# Useing Comprehension

ft2 = [convert2ampm(fte) for fte in flights.keys()]

# Dictionary Comprehension (dictcomp)

"""    flights_v2 = {}
    for k, v in flights_v2.items():
        flights_v2[convert2ampm(k)] = v.title()
    pprint(flights_v2)"""

more_flights={ convert2ampm(k) : v.title() for k, v in flights.items()}

"""just_freeport = {}
for k, v in flights.items():
    if v == 'FREEPORT': just_freeport[convert2ampm(k)] = v.title()"""

more_flights_V2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}


