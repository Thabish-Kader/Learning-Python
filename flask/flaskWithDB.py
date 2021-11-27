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

# Version 3
from flask import Flask, render_template, request, escape
from Deeper_Into_BIFs.Annotations import searchForLetters
from databaseContextManager import UseDatabase

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results"""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
            (phrase, letters, ip, browser_string, results) 
            values (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
