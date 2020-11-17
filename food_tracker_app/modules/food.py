from flask import Flask, render_template, request
from modules.database import get_db


def init(app: Flask):
    @app.route('/food', methods=['GET', 'POST'])
    def _food():
        if request.method == 'POST':
            if 'add' in request.form:
                handle_new_food(request.form)
            else:
                delete_food(request.form['delete'])

        return render_template('add_food.html', food=get_all_food())


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


def get_all_food():
    cursor = get_db().execute('select * from food')
    return cursor.fetchall()


def delete_food(name):
    food_db = get_db()
    food_db.execute(f'delete from food where name="{name}"')
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
