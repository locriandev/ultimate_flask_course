from datetime import datetime
from flask import Flask, render_template, request
from modules import database, dates


def init(app: Flask):
    @app.route('/', methods=['GET', 'POST'])
    def _index():
        if request.method == 'POST':
            if 'delete' in request.form:
                dates.delete_date(request.form)
            else:
                handle_new_date(request.form['date'])
        return render_template('home.html', dates=dates.get_dates())


def handle_new_date(date):
    datetime_obj = datetime.strptime(date, dates.INPUT_DATE_FORMAT)
    db_date = datetime.strftime(datetime_obj, dates.DATABASE_DATE_FORMAT)
    food_db = database.get_db()
    food_db.execute('insert into log_date (entry_date) values (?)',
                    [db_date])
    food_db.commit()
