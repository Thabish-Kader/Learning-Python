"""Sets dont allow dublicates
 insertion order is not maintained"""
vowels = {'a', 'e', 'i', 'o', 'u', 'u'}
print(vowels)

"""Useing union operator"""
word = 'hello'
u = vowels.union(set(word))
"""now, to sort the set """
u_list = sorted(list(u))
print(u_list)
"""Useing difference operator"""
d = vowels.difference(set(word))
print(d)
"""Useing intersection operator"""
i = vowels.intersection(set(word))
print(i)

# --------------------------------------------------------
newvowels = set('aeiou')
Inputword = input("Provide a word to search for vowels: ")
newfound = vowels.intersection(set(Inputword))

for found in newfound:
    print(found)
