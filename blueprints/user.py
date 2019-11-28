from flask import request, render_template, redirect, url_for, Blueprint
from wtforms import Form, StringField, validators

from db import db
from models.models import UserModel

app_user = Blueprint('user', __name__)


class UserForm(Form):
    name = StringField('name', validators=[validators.input_required()])
    email = StringField('email', validators=[validators.input_required()])
    library = StringField('library', validators=[validators.input_required()])


@app_user.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if request.method == 'POST':
        data = {'name': request.form['name'], 'email': request.form['email'],
                'library': request.form['library']}
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('book.add_book'))
    return render_template('add_user.html', form=form)


@app_user.route('/<name>/<email>/<library>')
def get_user(name, email, library):
    return render_template('user.html', name=name, email=email.replace('%', '@'), library=library)
