from flask import render_template, request, Blueprint, redirect, url_for

from wtforms import StringField, Form, validators


app_user = Blueprint('user', __name__)


class User:
    def __init__(self, name, email, library):
        self.name = name
        self.email = email
        self.library = library


users_list = [User('John Harris', 'john@yahoo.com', ['Horror', 'Jane Eyre', 'Detective']),
              User('Leyla Koppi', 'leyla@yahoo.com', ['University secrets', 'Eye', 'Start of the end']),
              User('Cooper', 'cooper@yahoo.com', ['Paris', 'Illusion'])]


class UserForm(Form):
    name = StringField('name', validators=[validators.input_required()])
    email = StringField('email', validators=[validators.input_required()])
    library = StringField('library', validators=[validators.input_required()])


@app_user.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if request.method == 'POST':
        data = {'name': request.form['name'], 'email': request.form['email'], 'library': list(request.form['library'].split(','))}
        users_list.append(User(**data))
        return redirect(url_for('book.add_book'))
    return render_template('add_user.html', form=form)


@app_user.route('/<name>/<email>/<library>', methods=['GET'])
def get_user(name, email, library):
    return render_template('user.html', name=name, email=email.replace('%', '@'), library=library)

