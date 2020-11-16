#!/usr/bin/env python

from flask import Flask

from modules import database, templates, static, various, session, request, forms, inheritance

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A!A%371z$IV*'

forms.init(app)
templates.init(app)
request.init(app)  # pylint: disable=no-member
session.init(app)
inheritance.init(app)
static.init(app)
various.init(app)
database.init(app)


if __name__ == '__main__':
    app.run(debug=True)
