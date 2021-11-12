"""
Goal is to display  "on tap"
by manipulating the "Don't panic!"
"""
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
"""iterates 4 times"""
for i in range(4):
    """removes the last 4 characters """
    plist.pop()
"""removes D """
plist.pop(0)
"""removes the "'" """
plist.remove("'")
"""checking how the plist appears"""
print(plist)
"""first removes a and then p 
then inserts a first then p"""
plist.extend([plist.pop(), plist.pop()])
"""removes the white space and attaches it in the 2nd postion of the list"""
plist.insert(2, plist.pop(3))
print(plist)
"""Coverts to string"""
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
