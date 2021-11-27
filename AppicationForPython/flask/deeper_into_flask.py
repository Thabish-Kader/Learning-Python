from flask import Flask, escape, session
from Deeper_Into_BIFs.Annotations import searchForLetters
from flask import render_template, request
from StoreingData.storeingData import log_request
from databaseContextManager import UseDatabase
app = Flask(__name__)


@app.route('/search4', methods=['Post'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(searchForLetters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title=title, the_results=results, the_letters=letters, the_phrase=phrase)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search for letters')


# version 1
# view the log through the web app
#@app.route('/viewlog')
# def view_the_log() -> str:
#     with open('vsearch.log') as readlog:
#         contents = readlog.read()
#     return escape(''.join(contents))

#@app.route('/viewlog')
# version 2 of view_the_log()
# def view_the_log() -> str:
#     contents = []
#     with open('vsearch.log') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     return str(contents)

#@app.route('/viewlog')
# version 4 of view_the_log function
# def view_the_log() -> 'html':
#     contents = []
#     with open('vsearch.log') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     titles = ('From Data', 'Remote_addr', 'USer_agent', 'Results')
#     return render_template('viewlog.html', the_title='View Log',
#                            the_row_title=titles,
#                            the_data=contents)




# version 5 of view_the_log_function ( amending this function)
@app.route('/viewlog')
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL= """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles = titles,
                               the_data=contents,
                               )

app.secret_key = 'YouWillNeverGuess'
@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    """this function accesses the value associated with the
     user key and returns it to the waiting web browser as part
      of the stringed message."""
    return 'User value is currently set to: '+ session['user']
if __name__ == '__main__':
    app.run(debug=True)
