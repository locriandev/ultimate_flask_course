from flask import session, jsonify


def init(app):
    @app.route('/greet', defaults={'name': 'Flask'})
    @app.route('/greet/<name>')
    def greet(name):
        session['name'] = name
        return f'<h1>Hello {name} </h1>'

    @app.route('/json', methods=['GET', 'POST'])
    def json():
        session.pop('name', None)
        return jsonify({
            'obj': 'a',
            'list': [1, 2, 3]
        })

    @app.route('/list', defaults={'n': 10})
    @app.route('/list/<int:n>')
    def listf(n):
        if session.get('name'):
            return jsonify([session['name'] for _ in range(n)])
        else:
            return jsonify([x for x in range(n)])
