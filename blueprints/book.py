from flask import Blueprint, request, render_template
from wtforms import Form, StringField, validators, IntegerField

app_book = Blueprint('book', __name__)


class Book:
    def __init__(self, author, name, edition, year, translator='No translator'):
        self.author = author
        self.name = name
        self.edition = edition
        self.year = year
        self.translator = translator


books_list = [Book('Stiven King', 'Horror', 'Kazochka', 1998, 'Ya'),
              Book('Stiven Hawking', 'Jane Eyre', 'Walk', 1992, 'Sofiia'),
              Book('Den', 'Detective', 'Kazochka', 1998),
              Book('Bronte', 'Eye', 'Walk', 1992, 'Jennis'),
              Book('Agata Kristi', 'University secrets', 'Kazochka', 1998, 'My'),
              Book('Bronte', 'Start of the end', 'Walk', 1992),
              Book('Kristi Janes', 'Paris', 'Kolobok', 1992),
              Book('Santiago', 'Illusion', 'Svit', 1821, 'Migren')]


class BookForm(Form):
    author = StringField('author', validators=[validators.input_required()])
    name = StringField('name', validators=[validators.input_required()])
    edition = StringField('edition', validators=[validators.input_required()])
    year = IntegerField('year', validators=[validators.input_required()])
    translator = StringField('translator', validators=[validators.optional()])


@app_book.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form1 = BookForm()
    if request.method == 'POST':
        data = {'author': request.form['author'], 'name': request.form['name'], 'edition': request.form['edition'],
                'year': request.form['year'], 'translator': request.form['translator']}
        if data['translator'] == '':
            data['translator'] = 'No translator'
        books_list.append(Book(**data))
        return render_template('home.html')
    return render_template('add_book.html', form=form1)


@app_book.route('/<name>')
def get_book(name):
    for book in books_list:
        if book.name == name:
            author = book.author
            edition = book.edition
            year = book.year
            translator = book.translator
    return render_template('book.html', name=name, author=author, edition=edition, year=year, translator=translator)
