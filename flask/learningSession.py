from flask import Flask, escape, session

app = Flask(__name__)


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'YOu are now logged in'


app.secret_key = 'YouWillNeverGuessMySecretKey'

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are NOT logged in.'

def check_logged_in() -> str:
    if 'logged_in' in session:
        return True
    return False
