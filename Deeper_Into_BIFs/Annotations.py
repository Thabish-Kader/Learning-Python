"""Function annotaions are optional
Function annotaion are informational - such as the return type  and the arguments in a function
 The goal of annotations is not to make life easier for the interpreter; it’s to make life easier for the user of your function."""

def search_for_vowels (word:str) -> set: # We are stating that the “word” argument is expected to be a string. and We are stating that the function returns a set to its caller.
    """Return any vowels found in a supplied word """
    vowels = set('aeiou')
    return vowels.intersection(set(word))

def searchForLetters(phrase:str, letter:str) -> set:
    """Search for letter that user typed based on the phrase"""
    return set(letter).intersection(set(phrase))

print(searchForLetters('Machine Learning is faciantiong disclipline','aeiou'))

"""Assigning a default value"""
def searchForletters_v2(phrase:str, letters:str='aeiou') -> set:
    """Search for letter that user typed based on the phrase"""
    return set(letters).intersection(set(phrase))

print(searchForletters_v2('Deep Learning is another such discpline'))