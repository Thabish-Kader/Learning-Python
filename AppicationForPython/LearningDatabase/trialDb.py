import mysql.connector

config = mysql.connector.connect(user = 'vsearch', password = 'vsearchpasswd', host = 'localhost',database = 'vsearchlogDB' )
print('connection successful')

