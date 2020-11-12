#!/usr/bin/env python

from flask import Flask
import forms
import templates
import request
import session
import inheritance
import static


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A!A%371z$IV*'
forms.init(app)
templates.init(app)
request.init(app)
session.init(app)
inheritance.init(app)
static.init(app)


@app.route('/test/<int:n>', defaults={'s': 'default string'})
@app.route('/test/<string:s>', defaults={'n': 0})
def test(n, s):
    return str(f'{n}: {type(n)}, {s}: {type(s)}')


@app.route('/multiline')
def multiline():
    return '''
abc
123
defg
456
'''


if __name__ == '__main__':
    app.run(debug=True)
