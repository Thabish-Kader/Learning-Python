"""Implemeneting the mysql.connector to def log_request(...)"""
import mysql.connector
from databaseContextManager import UseDatabase
from flask import request
# Version 1
# def log_request(req: 'flask_request', res: str) -> None:
#     """Log details of the web request and the results."""
#     dbconfig = { 'host': '127.0.0.1',
#                  'user': 'vsearch',
#                  'password': 'vsearchpasswd',
#                  'database': 'vsearchlogDB', }
#
#
#     conn = mysql.connector.connect(**dbconfig)
#     cursor = conn.cursor()
#
#     _SQL = """insert into log
#     (phrase, letters, ip, browser_string, results) values
#     (%s, %s, %s, %s, %s)"""
#     cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],req.remote_addr, req.user_agent.browser, res, ))
#
#     conn.commit()
#     cursor.close()
#     conn.close()

# Version 2
# def log_request(req: 'flask_request', res: str) -> None:
#     """Log details of the web request and the results."""
#     dbconfig = { 'host': '127.0.0.1',
#                  'user': 'vsearch',
#                  'password': 'vsearchpasswd',
#                  'database': 'vsearchlogDB', }
#
#
#     conn = mysql.connector.connect(**dbconfig)
#     cursor = conn.cursor()
#
#     _SQL = """insert into log
#     (phrase, letters, ip, browser_string, results) values
#     (%s, %s, %s, %s, %s)"""
#     cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],req.remote_addr, req.user_agent.browser, res, ))
#
#     conn.commit()
#     cursor.close()
#     conn.close()

# Version 3 of log_request function with context manager
def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = { 'host': '127.0.0.1',
                 'user': 'vsearch',
                'password': 'vsearchpasswd',
                 'database': 'vsearchlogDB', }

    with UseDatabase(dbconfig) as cursor:
        _SQL = """show table"""
        cursor.execute(_SQL)
        data = cursor.fetchall()


