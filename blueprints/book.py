from flask import Blueprint, request, render_template
from wtforms import Form, StringField, validators, IntegerField

app_book = Blueprint('book', __name__)


class Book:
    def __init__(self, author, name, edition, year, translator=None):
        self.author = author
        self.name = name
        self.edition = edition
        self.year = year
        self.translator = translator


books_list = [Book('Stiven King', 'Horror', 'Kazochka', 1998, 'Ya'),
              Book('Stiven Hawking', 'Jane Eyre', 'Walk', 1992, 'Sofiia'),
              Book('Den', 'Detective', 'Kazochka', 1998, 'Ty'),
              Book('Bronte', 'Eye', 'Walk', 1992, 'Sofiia'),
              Book('Agata Kristi', 'University secrets', 'Kazochka', 1998, 'My'),
              Book('Bronte', 'Start of the end', 'Walk', 1992, 'Sofiia')]


class BookForm(Form):
    author = StringField('author', validators=[validators.input_required()])
    name = StringField('name', validators=[validators.input_required()])
    edition = StringField('edition', validators=[validators.input_required()])
    year = IntegerField('year', validators=[validators.input_required()])
    translator = StringField('translator', validators=[validators.optional()])


@app_book.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if request.method == 'POST':
        data = {'author': request.form['author'], 'name': request.form['name'], 'edition': request.form['edition'],
                'year': request.form['year'], 'translator': request.form['translator']}
        books_list.append(Book(data['author'], data['name'], data['edition'], data['year'], data['translator']))
        for i in books_list:
            print(i.author, i.year)
        return render_template('home.html')
    return render_template('add_book.html', form=form)


@app_book.route('/<author>/<name>/<edition>/<year>/<translator>')
def get_book(author, name, edition, year, translator):
    return render_template('book.html', author=author, name=name, edition=edition, year=year, translator=translator)
