from flask import session, jsonify


def init(app):
    @app.route('/greet', defaults={'name': 'Flask'})
    @app.route('/greet/<name>')
    def _greet(name):
        session['name'] = name
        return f'<h1>Hello {name} </h1>'

    @app.route('/json', methods=['GET', 'POST'])
    def _json():
        session.pop('name', None)
        return jsonify({
            'obj': 'a',
            'list': [1, 2, 3]
        })

    @app.route('/list', defaults={'n': 10})
    @app.route('/list/<int:length>')
    def _listf(length):
        if session.get('name'):
            return jsonify([session['name']] * length)
        return jsonify(list(range(length)))
