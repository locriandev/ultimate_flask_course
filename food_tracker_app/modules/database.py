import sqlite3
from datetime import datetime
from flask import g, Flask

DB_NAME = 'food_tracker.db'
DB_ATTRIB_NAME = 'sqlite_db'

INPUT_DATE_FORMAT = '%Y-%m-%d'
DATABASE_DATE_FORMAT = '%Y%m%d'
OUTPUT_DATE_FORMAT = '%B %d, %Y'


def init(app: Flask):
    @app.teardown_appcontext
    def _close_db(error):
        if hasattr(g, DB_ATTRIB_NAME):
            get_db().close()
        if error:
            print(error)


def connect_db():
    database = sqlite3.connect(DB_NAME)
    database.row_factory = sqlite3.Row
    return database


def get_db():
    if not hasattr(g, DB_ATTRIB_NAME):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def get_daily_food(date):
    date_id = get_date_id(date)
    food_for_date = get_food_for_date(date_id)
    return [get_food_from_food_id(food_id)
            for food_id in food_for_date]


def get_dates():
    cursor = get_db().execute('select * from log_date order by entry_date desc')
    dates = cursor.fetchall()
    dates = [{'date': date['entry_date'],
              'pretty_date': pretty_date(date['entry_date'])} for date in dates]
    return dates


def pretty_date(date):
    datetime_obj = datetime.strptime(str(date), DATABASE_DATE_FORMAT)
    return datetime.strftime(datetime_obj, OUTPUT_DATE_FORMAT)


def delete_date(form):
    date = form['delete']
    food_db = get_db()
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
    food_db = get_db()
    food_db.execute('insert into log_date (entry_date) values (?)',
                    [db_date])
    food_db.commit()


def handle_new_food(form):
    food = {
        'name': form['food'],
        'protein': int(form['protein']),
        'carbs': int(form['carbs']),
        'fat': int(form['fat'])
    }
    food['calories'] = compute_calories(food)
    add_food_to_db(food)


def compute_calories(food):
    return food['protein'] * 4 + food['carbs'] * 4 + food['fat'] * 9


def add_food_to_db(food):
    food_db = get_db()
    food_db.execute(
        'insert into food '
        '(name, protein, carbohydrates, fats, calories) '
        'values(?, ?, ?, ?, ?) ',
        [food["name"], food["protein"], food["carbs"],
         food["fat"], food["calories"]]
    )
    food_db.commit()


def get_food_for_date(date_id):
    cursor = get_db().execute(
        'select food_id from food_date '
        f'where log_date_id = "{date_id}"'
    )
    return [element['food_id'] for element in cursor.fetchall()]


def get_food_from_food_id(food_id):
    cursor = get_db().execute(
        f'select * from food where id={food_id}'
    )
    return cursor.fetchone()


def get_food_id(food_name):
    cursor = get_db().execute(
        f'select id from food where name = "{food_name}"'
    )
    return cursor.fetchone()['id']


def delete_food(name):
    food_db = get_db()
    food_id = get_food_id(name)
    food_db.execute(f'delete from food where name="{name}"')
    food_db.execute(f'delete from food_date where food_id="{food_id}"')
    food_db.commit()


def get_all_food():
    cursor = get_db().execute('select * from food')
    return cursor.fetchall()
