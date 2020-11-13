import sqlite3
from flask import g, Flask, render_template


DB_NAME = 'data.db'
DB_ATTRIB_NAME = 'sqlite_db'


def init(app: Flask):
    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, DB_ATTRIB_NAME):
            get_db().close()

    @app.route('/viewResults')
    def view_results():
        db = get_db()
        cur = db.execute('select * from users')
        res = cur.fetchall()
        for r in res:
            print(f'{r["id"]} - {r["name"]} - {r["location"]}')
        return render_template('database.html', results=res)


def connect_db():
    db = sqlite3.connect(DB_NAME)
    db.row_factory = sqlite3.Row
    return db


def get_db():
    if not hasattr(g, DB_ATTRIB_NAME):
        g.sqlite_db = connect_db()
    return g.sqlite_db
