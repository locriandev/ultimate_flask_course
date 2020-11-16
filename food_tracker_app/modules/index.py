from flask import Flask, render_template


def init(app: Flask):
    @app.route('/')
    def index():
        return render_template('home.html')
