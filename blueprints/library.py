from flask import Blueprint, render_template

from models.models import UserModel, BookModel

app_library = Blueprint('library', __name__)


@app_library.route('/library')
def get_library():
    return render_template('library.html', user_list=UserModel.query.all(), book_list=BookModel.query.all())