#!/usr/bin/env python

from flask import Flask

import forms
import templates
import request
import session
import inheritance
import static
import various


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A!A%371z$IV*'

forms.init(app)
templates.init(app)
request.init(app)  # pylint: disable=no-member
session.init(app)
inheritance.init(app)
static.init(app)
various.init(app)


if __name__ == '__main__':
    app.run(debug=True)
