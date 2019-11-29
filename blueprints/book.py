from flask import request, render_template, redirect, url_for, Blueprint
from wtforms import Form, StringField, validators, IntegerField

from db import db
from models.models import BookModel

app_book = Blueprint('book', __name__)


class BookForm(Form):
    author = StringField('author', validators=[validators.input_required()])
    name = StringField('name', validators=[validators.input_required()])
    edition = StringField('edition', validators=[validators.input_required()])
    year = IntegerField('year', validators=[validators.input_required()])
    user = StringField('edition', validators=[validators.input_required()])
    translator = StringField('translator', validators=[validators.optional()])


@app_book.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form1 = BookForm()
    if request.method == 'POST':
        data = {'author': request.form['author'], 'name': request.form['name'], 'edition': request.form['edition'],
                'year': request.form['year'], 'user': request.form['user'], 'translator': request.form['translator']}
        if request.form['translator'] == '':
            data['translator'] = 'None'
        book = BookModel(**data)

        db.session.add(book)
        db.session.commit()
        return redirect(url_for('library.get_library'))
    return render_template('add_book.html', form=form1)


@app_book.route('/book<name>')
def get_book(name):
    try:
        for book in BookModel.query.all():
            if book.name == name:
                author = book.author
                edition = book.edition
                year = book.year
                user = book.user
                translator = book.translator
        return render_template('book.html', name=name, author=author, edition=edition, year=year, user=user,
                               translator=translator)
    except Exception:
        return '<h1>Book is not added</h1>'


hidden_books = []
@app_book.route('/<name>')
def hide_book(name):
    hidden_books.append(name)
    return f'Name: {hidden_books}'
