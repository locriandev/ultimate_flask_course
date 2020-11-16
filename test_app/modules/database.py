import sqlite3
from flask import g, Flask, render_template


DB_NAME = 'data.db'
DB_ATTRIB_NAME = 'sqlite_db'


def init(app: Flask):
    @app.teardown_appcontext
    def _close_db(error):
        if hasattr(g, DB_ATTRIB_NAME):
            get_db().close()
        if error:
            print(error)

    @app.route('/viewResults')
    def _view_results():
        database = get_db()
        cursor = database.execute('select * from users')
        results = cursor.fetchall()
        for result in results:
            print(f'{result["id"]} - {result["name"]} - {result["location"]}')
        return render_template('database.html', results=results)


def connect_db():
    database = sqlite3.connect(DB_NAME)
    database.row_factory = sqlite3.Row
    return database


def get_db():
    if not hasattr(g, DB_ATTRIB_NAME):
        g.sqlite_db = connect_db()
    return g.sqlite_db
