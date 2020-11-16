from flask import Flask, render_template


APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'JtiPWt7jC3K3'


@APP.route('/')
def index():
    return render_template('home.html')


@APP.route('/view')
def view():
    return render_template('day.html')


@APP.route('/food')
def food():
    return render_template('add_food.html')


if __name__ == '__main__':
    APP.run(debug=True)
