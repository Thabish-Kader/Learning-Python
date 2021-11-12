# Trying out pytjons for loop in list

paranoid_android = 'Marvin'
letters = list(paranoid_android)
for char in letters:
    print('\t', char)

paranoid_android = 'MArvin, the paranoid allegator'
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char)
print()

for char in letters[-7:]:
    """"multiplying 2 for more tabs"""
    print('\t'*2, char)
print()

for char in letters[12:20]:
    """"multiplying 3 for more tabs"""
    print('\t'*3, char)
print()
