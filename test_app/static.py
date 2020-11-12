from flask import render_template


def init(app):
    @app.route('/image')
    def image():
        return render_template('image.html')
