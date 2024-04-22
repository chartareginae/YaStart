from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return render_template('main_page.html')


@app.route('/registration_and_login')
def registration_and_login():
    return render_template('login.html')


@app.route('/sphere')
def sphere():
    return render_template('mars.html', title='OK')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
