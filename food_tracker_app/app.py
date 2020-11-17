from flask import Flask

from modules import database, food, index, details, food_date

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'JtiPWt7jC3K3'
database.init(APP)
food.init(APP)
index.init(APP)
details.init(APP)
food_date.init(APP)


if __name__ == '__main__':
    APP.run(debug=True)
