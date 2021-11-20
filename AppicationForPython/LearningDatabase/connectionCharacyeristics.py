"""our pieces of information you need when connecting to
MySQL: (1) the IP address/name of the computer running the
MySQL server (known as the host), (2) the user ID to use, (3)
the password associated with the user ID, and (4) the name of
the database the user ID wants to interact with.

dictionary (called dbconfig) that associates the four required
“connection keys” with their corresponding value"""
import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB'}

conn = mysql.connector.connect(**dbconfig)  # The ** notation tells the connect function that a dictionary of arguments is being supplied in a single variable

# To send SQL commands to the database (via the just-opened connection)
# as well as receive results from the database, curser is needed.
# Think of a cursor as the database equivalent of the file handle

cursor = conn.cursor()
__SQL = """show table"""
cursor.execute(__SQL)
res = cursor.fetchall()
print(res)

__SQL = """describe log"""
cursor.execute(__SQL)
res = cursor.fetchall()
print(res)

for row in res:
    print(row)

# using db- api placeholders instead of actual data values

__SQL = """insert into log
        (phrase, letters, ip, browser_string, results)
        values
        (%s, %s, %s, %s, %s)""" # useing %s placeholder,  tells DB-API to expect a stringed value to be substituted into the query prior to execution.
cursor.execute(__SQL,('hikeing', 'abc', '127.0.0.1', 'Safari', 'set()')) # there are five %s placeholders above, so the second thing to note is that cursor. execute call is going to expect five additional parameters when called.

conn.commit() #force the database system to commit all potentially cached data to the table using the conn.commit method
__SQL = """select * from log"""
cursor.execute(__SQL)
for row in cursor.fetchall():
    print(row)
    conn.close()
