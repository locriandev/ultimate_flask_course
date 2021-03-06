from flask import render_template


def init(app):
    @app.route('/bool/<value>')
    def _boolean(value):
        return render_template('if.html', val=value == 'True')

    @app.route('/list2/<int:n>')
    def _list2(n):  # pylint: disable=invalid-name
        return render_template('list.html', n=n)

    @app.route('/listOfDicts')
    def _list_of_dicts():
        l_of_d = [
            {'key': 'value 1'},
            {'key': 'value 2'},
            {'key': 'value 3'}
        ]
        return render_template('listofdicts.html', list_of_dicts=l_of_d)
