from flask import Flask, render_template


def init(app: Flask):
    @app.route('/details')
    def _details():
        return render_template('day.html')
