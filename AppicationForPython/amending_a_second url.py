from flask import Flask
from Deeper_Into_BIFs.Annotations import searchForLetters

app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4')
def do_search():
    return str(searchForLetters('life ! is myterious in many ways','eiru' ))
app.run()



