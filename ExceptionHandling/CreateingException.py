class ConnectionError(Exception):
    pass


raise ConnectionError('Cannot connect..is it time to panic ?')

try:
    raise ConnectionError('Whoops')
except ConnectionError as err:
    print('Got:', str(err))
