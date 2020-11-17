from flask import Flask, render_template, request
from modules import dates


def init(app: Flask):
    @app.route('/', methods=['GET', 'POST'])
    def _index():
        if request.method == 'POST':
            if 'delete' in request.form:
                dates.delete_date(request.form)
            else:
                dates.add_new_date(request.form['date'])
        return render_template('home.html', dates=dates.get_dates())
