from flask import Flask, render_template

from modules import database, food, index

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'JtiPWt7jC3K3'
food.init(APP)
database.init(APP)
index.init(APP)


@APP.route('/view')
def view():
    return render_template('day.html')


if __name__ == '__main__':
    APP.run(debug=True)
