from datetime import datetime
from modules import database
from modules.database import get_db

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


def get_date_id(date):
    cursor = get_db().execute(
        'select id from log_date'
        f' where entry_date = "{date}"'
    )
    return cursor.fetchone()['id']


def date_exists(date):
    cursor = get_db().execute(
        'select entry_date from log_date'
        ' where entry_date = ?', [date])
    return cursor.fetchone()


def add_new_date(date):
    datetime_obj = datetime.strptime(date, INPUT_DATE_FORMAT)
    db_date = datetime.strftime(datetime_obj, DATABASE_DATE_FORMAT)
    food_db = database.get_db()
    food_db.execute('insert into log_date (entry_date) values (?)',
                    [db_date])
    food_db.commit()
