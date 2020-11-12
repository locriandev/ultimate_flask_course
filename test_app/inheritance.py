from flask import render_template


def init(app):
    @app.route('/child/<int:n>')
    def child1(n):
        return render_template(f'child{n}.html')

    @app.route('/super')
    def _super():
        return render_template('super.html')

    @app.route('/include')
    def include():
        return render_template(
            'composite.html',
            var1='asodjdaoj',
            var2='43243232432',
            var3='@#[]'
        )
