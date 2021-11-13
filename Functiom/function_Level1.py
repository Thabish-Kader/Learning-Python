"""Function is a reusable piece of code just like methods in java"""

def searchforvowels():
    vowels = set('aeiou')
    word = input("Enter a word to search for vowels ")
    found = vowels.intersection(set(word))
    for vowels in found:
        print (vowels)

