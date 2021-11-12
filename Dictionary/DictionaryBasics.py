"""dictionary is used to hold a collection of key/value pair
there are two columns, with potentially multiple rows of data.
Name: Ford Prefect
Gender: Male
Occupation: Researcher
Home Planet: Betelgeuse Seven"""

employee = {'Name': 'Ford Prefect',
            'Gender': 'Male',
            'Occupation': 'Researcher',
            'Home Planet': 'Planet Baloney '
            }
print(employee['Name'])

"""Additional Info on Dictionary
    utilizes hashing algorithm which makes it quicker"""

"""Assigning a new key/value pair"""
employee['Age'] = 33
print(employee)

"""Uses of dictionary
    common application is to perform
    a frequency count: processing some data and maintaining a count"""

# program to count the number of times vowels occurs in a word typed by user
vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels:')
found = {}
"""Initializing the value associated with each of the key"""
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

"""the items() method is used to return the dictionary items with key and value"""
for k, v in sorted(found.items()):
    print(k, 'was found', v, ' times')
