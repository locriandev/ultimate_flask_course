from flask import Flask, render_template, request
from modules import database


def init(app: Flask):
    @app.route('/food', methods=['GET', 'POST'])
    def _food():
        if request.method == 'POST':
            if 'add' in request.form:
                handle_new_food(request.form)
            else:
                delete_food(request.form)

        return render_template('add_food.html', food=get_food())


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
    food_db = database.get_db()
    food_db.execute(
        'insert into food '
        '(name, protein, carbohydrates, fats, calories) '
        'values(?, ?, ?, ?, ?) ',
        [food["name"], food["protein"], food["carbs"],
         food["fat"], food["calories"]]
    )
    food_db.commit()


def get_food():
    food_db = database.get_db()
    cursor = food_db.execute('select * from food')
    return cursor.fetchall()


def delete_food(form):
    name = form['delete']
    food_db = database.get_db()
    food_db.execute(f'delete from food where name="{name}"')
    food_db.commit()
