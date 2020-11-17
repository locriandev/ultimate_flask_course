from flask import Flask

from modules import routes, database

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'JtiPWt7jC3K3'
routes.init(APP)
database.init(APP)


if __name__ == '__main__':
    APP.run(debug=True)
