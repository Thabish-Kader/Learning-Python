from time import sleep

from flask import Flask, render_template, request, escape, session, copy_current_request_context
from Deeper_Into_BIFs.Annotations import searchForLetters
from threading import Thread

from ExceptionHandling.DBcmWithException import UseDatabase_v2, ConnectionError, CredentialError, SQLError
from learningSession2 import check_logged_in

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'





@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    # The decorator, copy_current_request_context, ensures that the HTTP request that is active when a function is
    # called remains active even when the function is subsequently executed in a thread
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(15)
        with UseDatabase_v2(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
            (phrase, letters, ip, browser_string, results) values
            (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],
                                  req.remote_addr, req.user_agent.browser, res,))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(searchForLetters(letters(phrase, letters)))
    try:

        t = Thread(target=log_request, args=(request, results))
        t.start()
    except ConnectionError as err:
        print("error occured " + err)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    try:
        with UseDatabase_v2(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results
            from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
            titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
            return render_template('viewlog.html',
                                   the_title='View Log', the_row_titles=titles, the_data=contents, )

    except ConnectionError as err:
        print(err)

    except CredentialError as err:
        print(err)

    except SQLError as err:
        print(err)
    except Exception as err:
        print('Something wnt wrong ' + err)
    app.secret_key = 'YouWillNeverGuessMySecretKey'
    if __name__ == '__main__': app.run(debug=True)
