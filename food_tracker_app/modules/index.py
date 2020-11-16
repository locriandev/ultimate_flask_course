from datetime import datetime
from flask import Flask, render_template, request
from modules import database


INPUT_DATE_FORMAT = '%Y-%m-%d'
OUTPUT_DATE_FORMAT = '%B %d, %Y'
DATABASE_DATE_FORMAT = '%Y%m%d'


def init(app: Flask):
    @app.route('/', methods=['GET', 'POST'])
    def _index():
        if request.method == 'POST':
            if 'delete' in request.form:
                delete_date(request.form)
            else:
                handle_new_date(request.form['date'])
        return render_template('home.html', dates=get_dates())


def handle_new_date(date):
    datetime_obj = datetime.strptime(date, INPUT_DATE_FORMAT)
    db_date = datetime.strftime(datetime_obj, DATABASE_DATE_FORMAT)
    food_db = database.get_db()
    food_db.execute('insert into log_date (entry_date) values (?)',
                    [db_date])
    food_db.commit()


def get_dates():
    food_db = database.get_db()
    cursor = food_db.execute('select * from log_date order by entry_date desc')
    dates = cursor.fetchall()
    dates = [{'date': date['entry_date'],
              'pretty_date': pretty_date(date['entry_date'])} for date in dates]
    return dates


def pretty_date(date):
    datetime_obj = datetime.strptime(str(date), DATABASE_DATE_FORMAT)
    return datetime.strftime(datetime_obj, OUTPUT_DATE_FORMAT)


def delete_date(form):
    date = form['delete']
    food_db = database.get_db()
    food_db.execute(f'delete from log_date where entry_date = "{date}"')
    food_db.commit()
