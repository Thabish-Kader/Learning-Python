"""Rather than create (and then grapple with) four individual dictionary
variables for each line of data in our table, let’s create a
single dictionary variable, called people. We’ll then use
people to store any number of other dictionaries."""

people = {}
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researchers',
                  'Home Planet': 'Planet Baloney'}
print(people)

people['Arthur'] = {'Name': 'Arthour Dent',
                    'Gender': 'Male',
                    'Occupation': 'Burrito-Maker',
                    'Home Planet': 'Planet Burrito'}
people['Trillian'] = {'Name': 'Trillian Rine',
                      'Gender': 'Female',
                      'Occupation': 'Astronaut',
                      'Home Planet': 'Planet 371'}
people['Hellan'] = {'Name': 'Hellan Ro',
                    'Gender': 'Female',
                    'Occupation': 'Unknown',
                    'Home Planet': 'Planet Chee'}
print(people)

"""Presenting the dictionary of dictionaries more presentable with 'pprint-pretty print' """
import pprint

pprint.pprint(people)

"""Accessing the complex data"""
