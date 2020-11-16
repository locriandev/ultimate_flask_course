from datetime import datetime
from modules import database

INPUT_DATE_FORMAT = '%Y-%m-%d'
OUTPUT_DATE_FORMAT = '%B %d, %Y'
DATABASE_DATE_FORMAT = '%Y%m%d'


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
