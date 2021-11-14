"""Function is a reusable piece of code just like methods in java"""


# version_1
# def search_for_vowels():
#     """Display any vowels found in the word typed by the user"""
#     vowels = set('aeiou')
#     word = input('Enter a word to search for vowels')
#     found = vowels.intersection(set(word))
#     for vowels in found:
#         print (vowels)

# version_2
def search_for_vowels(word):
    """Display any vowels found in the word typed by the user"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowels in found:
        print(vowels)


def search_for_vowels2(word):
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


def search_for_vowels3(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found


# 2nd version of the above function more concise
def search_for_vowels3_v2(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


print(search_for_vowels('hitch-hiker'))
print(search_for_vowels2('Space'))
print(search_for_vowels3('Galaxy'))
print(search_for_vowels3_v2('sky'))  # Returns set() - Got to Deeper_Into_BIFs package for further explanation
