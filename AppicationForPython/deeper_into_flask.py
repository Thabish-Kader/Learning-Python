from flask import Flask
from Deeper_Into_BIFs.Annotations import searchForLetters
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from flask!'


@app.route('/search4')
def do_search() -> str:
    return str(searchForLetters('life is mysterious in many ways', 'eiru'))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search for letters')


app.run()
