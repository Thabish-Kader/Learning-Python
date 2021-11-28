import sys
#Version 1
try:
    with open('myFile.txt') as fh:
        file_data = fh.read()
        print(file_data)
except FileNotFoundError:
    print('The data file is missing')
# Version 2 with two except
try:
    with open('myFile.txt') as fh:
        file_data = fh.read()
        print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('Not allowed')

# version 3 with catch all except
try:
    with open('myFile.txt') as fh:
        file_data = fh.read()
        print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('Not allowed')
except:
    print('Something whent wrong')

#Version 4

try:
    1/0
except:
    err = sys.exc_info()
    for e in err:
        print(e)

# version 5
try:
    with open('myFile.txt') as fh:
        file_data = fh.read()
        print(file_data)
except PermissionError:
    print('Not allowed')
except Exception as err:
    print('Something whent wrong' + err)





