from databaseContextManager import UseDatabase

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB', }

with UseDatabase(dbconfig) as cursor:
    _SQL = """show table"""
    cursor.execute(_SQL)
    data = cursor.fetchall()
