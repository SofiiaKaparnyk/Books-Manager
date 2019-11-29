from db import db


class BookModel(db.Model):
    author = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, primary_key=True)
    edition = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    translator = db.Column(db.String, nullable=True)
    user = db.Column(db.String, db.ForeignKey('user_model.name'))


class UserModel(db.Model):
    name = db.Column(db.String, nullable=False, primary_key=True)
    email = db.Column(db.String, nullable=False)
    books = db.relationship('BookModel', backref='user_name')

