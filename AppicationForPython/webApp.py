from flask import Flask

app = Flask(__name__)
# line @app.route('/') below is a decorator it can be taught of as the equivalent to java override
@app.route('/')
def hello() -> str:
    return 'Hello world from flask!'

app.run()

