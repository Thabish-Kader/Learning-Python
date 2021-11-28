from pprint import pprint

with open('flightTime.csv') as data:
    ignore = data.readline()  # ignoreing the header info
    flights = {}  # new empty dictionary
    for line in data:
        k, v = line.strip().split(
            ',')  # Break apart the line at the comma, which returns two values: the key (flight time) and value (destination).
        # strip is used to remove unwanted triling newline
        flights[k] = v

dests = set(flights.values())
print(dests)

# wests = []
# for k, v in flights.items():
#     if v == 'WEST END':
#         wests.append(v)
# wests_v2 = [v for k, v in flights.items() if v == 'WEST END']
#
# for dests2 in set(flights.values()):
#     print(dests2, '-> ', [k for k, v in flights.items() if v == dests2])

# storeing this data in a dictionary

when = {}
for dest in set(flights.values()):
    when[dest] = [k for k, v in flights.items() if v == dest]

pprint(when)

# useing ditcomp for the above code
when2 = {dest2 : [k for k,v in flights.values() if v == dest] for dest2 in set(flights.values())}