from flask import Flask

from blueprints.book import app_book
from blueprints.home import app_home
from blueprints.library import app_library
from blueprints.user import app_user

from config import run_config
from db import db


def create_app():
    app = Flask(__name__)
    app.register_blueprint(app_user)
    app.register_blueprint(app_book)
    app.register_blueprint(app_library)
    app.register_blueprint(app_home)
    app.config.from_object(run_config())

    db.init_app(app)
    db.create_all(app=app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
