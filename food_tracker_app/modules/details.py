from flask import Flask, render_template
from modules import dates, food
from modules.dates import get_date_id, date_exists


def init(app: Flask):
    @app.route('/details/<int:db_date>')
    def _details(db_date):
        if not date_exists(db_date):
            return '<h1>not found</h1>'

        return render_template(
            'day.html',
            date=dates.pretty_date(db_date),
            food_list=food.get_all_food(),
            daily_food=get_daily_food(db_date)
        )


def get_daily_food(date):
    date_id = get_date_id(date)
    food_for_date = food.get_food_for_date(date_id)
    return [food.get_food_from_food_id(food_id)
            for food_id in food_for_date]
