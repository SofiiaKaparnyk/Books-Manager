from flask import request, render_template, redirect, url_for, Blueprint
from db import db
from forms.forms import BookForm, WantedBookForm
from models.models import BookModel, HiddenBookModel, WantedBookModel

app_book = Blueprint('book', __name__)


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
        book = BookModel.query.filter_by(name=name).first()
        author, edition, year, user, translator = book.author, book.edition, book.year, book.user, book.translator
        return render_template('book.html', name=name, author=author, edition=edition, year=year, user=user,
                               translator=translator)
    except Exception:
        return '<h1>Book is not added</h1>'


@app_book.route('/hide<name>')
def hide_book(name):
    book = BookModel.query.filter_by(name=name).first()

    data = {'author': book.author, 'name': name, 'edition': book.edition,
            'year': book.year, 'user': book.user, 'translator': book.translator}
    book_to_add = HiddenBookModel(**data)

    db.session.delete(book)
    db.session.add(book_to_add)
    db.session.commit()

    return redirect(url_for('library.get_library'))


@app_book.route('/show<name>')
def show_book(name):
    for book in HiddenBookModel.query.filter_by(user=name).all():
        data = {'author': book.author, 'name': book.name, 'edition': book.edition,
                'year': book.year, 'user': name, 'translator': book.translator}
        book_to_add = BookModel(**data)

        db.session.add(book_to_add)
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('library.get_library'))


@app_book.route('/hideall<name>')
def hide_all_books(name):
    for book in BookModel.query.filter_by(user=name).all():
        data = {'author': book.author, 'name': book.name, 'edition': book.edition,
                'year': book.year, 'user': name, 'translator': book.translator}
        book_to_add = HiddenBookModel(**data)

        db.session.add(book_to_add)
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('library.get_library'))


@app_book.route('/add_wanted_book<user_name>', methods=['GET', 'POST'])
def add_wanted_book(user_name):
    form1 = WantedBookForm()
    if request.method == 'POST':
        data = {'author': request.form['author'], 'name': request.form['name'], 'user': user_name}
        book = WantedBookModel(**data)

        db.session.add(book)
        db.session.commit()
        return redirect(url_for('user.get_user', user_name=user_name))
    return render_template('add_wanted_book.html', form=form1)
