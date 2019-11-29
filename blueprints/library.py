from flask import Blueprint, render_template

from blueprints.book import hidden_books
from models.models import UserModel, BookModel

app_library = Blueprint('library', __name__)


@app_library.route('/library')
def get_library():
    book_list = [i for i in BookModel.query.all() if i.name not in hidden_books]
    # for i in UserModel.query.all():
    #     for j in i.books:
    #         print(j.name)
    return render_template('library.html', user_list=UserModel.query.all())