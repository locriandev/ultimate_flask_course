from flask import Flask, render_template


def init(app: Flask):
    @app.route('/food', methods=['GET', 'POST'])
    def _food():
        return render_template('add_food.html')
