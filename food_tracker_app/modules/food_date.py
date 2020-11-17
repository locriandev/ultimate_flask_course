from flask import Flask, request, redirect, url_for
from modules.food import get_food_id
from modules.dates import get_date_id
from modules.database import get_db


def init(app: Flask):
    @app.route('/addFoodDate', methods=['POST'])
    def _add_food_date():
        food_id = get_food_id(request.form['food'])
        date_id = get_date_id(request.form['date'])
        get_db().execute(
            'insert into food_date (food_id, log_date_id) '
            f'values ({food_id}, {date_id})'
        )
        get_db().commit()
        return redirect(url_for('_details', db_date=request.form['date']))
