from flask import Flask
from Deeper_Into_BIFs.Annotations import searchForLetters
from flask import render_template, request
from StoreingData.storeingData import log_request

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


# view the log through the web app
@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as readlog:
        contents = readlog.read()
    return contents

if __name__ == '__main__':
    app.run(debug=True)
