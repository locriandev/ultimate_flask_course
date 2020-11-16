from flask import Flask, render_template
from modules import dates, food


def init(app: Flask):
    @app.route('/details/<int:db_date>')
    def _details(db_date):
        pretty_date = dates.pretty_date(db_date)
        return render_template(
            'day.html',
            date=pretty_date,
            food_list=food.get_food()
        )
