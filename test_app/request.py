import flask


def init(app):
    @app.route('/processJson', methods=['POST'])
    def _process_json():
        return flask.jsonify(f'keys: {str(flask.request.get_json().keys())},'
                       f'values: {str(flask.request.get_json().values())}')

    @app.route('/overload', methods=['GET'])
    def _overload_get():
        return f'called with method {flask.request.method}'

    @app.route('/overload', methods=['POST'])
    def _overload_post():
        return f'called with method {flask.request.method}'

    @app.route('/query')
    def _query():
        args = flask.request.args
        a_arg = args['a']
        b_arg = args['b']
        return f'a={a_arg}, b={b_arg}'
