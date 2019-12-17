from wtforms import Form, StringField, validators, IntegerField


class BookForm(Form):
    author = StringField('author', validators=[validators.input_required()])
    name = StringField('name', validators=[validators.input_required()])
    edition = StringField('edition', validators=[validators.input_required()])
    year = IntegerField('year', validators=[validators.input_required()])
    user = StringField('edition', validators=[validators.input_required()])
    translator = StringField('translator', validators=[validators.optional()])


class WantedBookForm(Form):
    author = StringField('author', validators=[validators.input_required()])
    name = StringField('name', validators=[validators.input_required()])
    user = StringField('edition', validators=[validators.input_required()])


class UserForm(Form):
    name = StringField('name', validators=[validators.input_required()])
    email = StringField('email', validators=[validators.input_required()])


class Email(Form):
    books = StringField('books', validators=[validators.input_required()])
