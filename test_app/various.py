def init(app):
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
