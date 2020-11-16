#!/usr/bin/env python

from flask import Flask

from modules import database, templates, static, various, session, request, forms, inheritance

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'A!A%371z$IV*'

forms.init(APP)
templates.init(APP)
request.init(APP)  # pylint: disable=no-member
session.init(APP)
inheritance.init(APP)
static.init(APP)
various.init(APP)
database.init(APP)


if __name__ == '__main__':
    APP.run(debug=True)
