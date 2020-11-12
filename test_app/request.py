from flask import jsonify, request


def init(app):
    @app.route('/processJson', methods=['POST'])
    def process_json():
        return jsonify(f'keys: {str(request.get_json().keys())},'
                       f'values: {str(request.get_json().values())}')

    @app.route('/overload', methods=['GET'])
    def overload_get():
        return f'called with method {request.method}'

    @app.route('/overload', methods=['POST'])
    def overload_post():
        return f'called with method {request.method}'

    @app.route('/query')
    def query():
        args = request.args
        a = args['a']
        b = args['b']
        return f'a={a}, b={b}'
