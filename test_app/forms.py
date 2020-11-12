from flask import render_template, request, jsonify


FORM_TEMPLATE = 'form.html'


def init(app):
    @app.route('/form')
    def form():
        return render_template(
            'form.html',
            action="/processForm"
        )

    @app.route('/processForm', methods=['POST'])
    def process_form():
        return str(request.form)

    @app.route('/form2', methods=['GET', 'POST'])
    def form2():
        if request.method == 'GET':
            return render_template('form.html', action="/form2")
        else:
            return jsonify(str(request.form))

    @app.route('/form3', methods=['GET', 'POST'])
    def form3():
        if request.method == 'GET':
            return render_template(FORM_TEMPLATE, action="/form3")
        else:
            form_element = request.form
            return redirect(
                url_for('greet_name',
                        name=f'{form_element["name"]} {form_element["lastname"]}',
                        ciccio='asdasdasdsad'))