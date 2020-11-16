from flask import Flask, render_template

from modules import database, food

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'JtiPWt7jC3K3'
food.init(APP)
database.init(APP)


@APP.route('/')
def index():
    return render_template('home.html')


@APP.route('/view')
def view():
    return render_template('day.html')


if __name__ == '__main__':
    APP.run(debug=True)
