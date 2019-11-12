from flask import Blueprint, render_template
from .user import users_list
from .book import books_list


app_library = Blueprint('library', __name__)


@app_library.route('/library')
def get_library():
    return render_template('library.html', user_list=users_list, book_list=books_list)