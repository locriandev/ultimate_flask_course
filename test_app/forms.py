from flask import render_template, request, jsonify, url_for
from werkzeug.utils import redirect

from database import get_db


FORM_TEMPLATE = 'form.html'


def init(app):
    @app.route('/form')
    def _form():
        return render_template(
            'form.html',
            action="/processForm"
        )

    @app.route('/processForm', methods=['POST'])
    def _process_form():
        name = request.form['name']
        location = request.form['location']
        database = get_db()
        database.execute(f'insert into users (name, location) values ("{name}", "{location}")')
        database.commit()
        return f'Added user: {name} from {location}'

    @app.route('/form2', methods=['GET', 'POST'])
    def _form2():
        if request.method == 'GET':
            return render_template('form.html', action="/form2")
        return jsonify(str(request.form))

    @app.route('/form3', methods=['GET', 'POST'])
    def _form3():
        if request.method == 'GET':
            return render_template(FORM_TEMPLATE, action="/form3")

        form_element = request.form
        return redirect(
            url_for('greet_name',
                    name=f'{form_element["name"]} {form_element["lastname"]}',
                    ciccio='asdasdasdsad'))
