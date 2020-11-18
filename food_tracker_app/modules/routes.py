from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from modules.database import *


def init(app: Flask):
    @app.route('/', methods=['GET', 'POST'])
    def _index():
        if request.method == 'POST':
            if 'delete' in request.form:
                delete_date(request.form)
            else:
                add_new_date(request.form['date'])
        return render_template('home.html', dates=get_dates())

    @app.route('/food', methods=['GET', 'POST'])
    def _food():
        if request.method == 'POST':
            if 'add' in request.form:
                handle_new_food(request.form)
            else:
                delete_food(request.form['delete'])

        return render_template('add_food.html', food=get_all_food())

    @app.route('/details/<int:db_date>')
    def _details(db_date):
        if not date_exists(db_date):
            return '<h1>not found</h1>'

        return render_template(
            'day.html',
            date=db_date,
            pretty_date=pretty_date(db_date),
            food_list=get_all_food(),
            daily_food=get_daily_food(db_date)
        )

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
