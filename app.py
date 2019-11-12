from flask import Flask, render_template, request

from blueprints.book import app_book
from blueprints.library import app_library
from blueprints.user import app_user

app = Flask(__name__)
app.register_blueprint(app_user)
app.register_blueprint(app_book)
app.register_blueprint(app_library)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
