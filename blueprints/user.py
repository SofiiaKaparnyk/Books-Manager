from flask import request, render_template, redirect, url_for, Blueprint

from config_email import send_email_to_user
from db import db
from forms.forms import UserForm, Email
from models.models import UserModel, WantedBookModel

app_user = Blueprint('user', __name__)


@app_user.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if request.method == 'POST':
        data = {'name': request.form['name'], 'email': request.form['email']}
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('book.add_book'))
    return render_template('add_user.html', form=form)


@app_user.route('/user<user_name>')
def get_user(user_name):
    try:
        for user in UserModel.query.all():
            if user.name == user_name:
                email = user.email
                books = user.books
                wanted_books = WantedBookModel.query.all()
        return render_template('user.html', name=user_name, email=email.replace('%', '@'), books=books,
                               wanted_books=wanted_books)
    except Exception:
        return '<h1>User is not added</h1>'


@app_user.route('/send_email<user_name>', methods=['GET', 'POST'])
def send_email(user_name):
    form1 = Email()
    if request.method == 'POST':
        email = UserModel.query.filter_by(name=user_name).first().email
        books = request.form['books']

        send_email_to_user(email, books)
        return redirect(url_for('user.get_user', user_name=user_name))
    return render_template('email.html', form=form1)
