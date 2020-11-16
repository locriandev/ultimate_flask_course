from flask import render_template


def init(app):
    @app.route('/child/<int:n>')
    def _child1(n):  # pylint: disable=invalid-name
        return render_template(f'child{n}.html')

    @app.route('/super')
    def _super():
        return render_template('super.html')

    @app.route('/include')
    def _include():
        return render_template(
            'composite.html',
            var1='asodjdaoj',
            var2='43243232432',
            var3='@#[]'
        )
