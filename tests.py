from unittest import TestCase

from app import create_app
from db import db
from models.models import BookModel, UserModel

app = create_app('TEST')


class Testing(TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        data = {'author': 'Kapa', 'name': 'Stop', 'edition': 'Sunshine',
                'year': 2017, 'user': 'Tony', 'translator': 'Stefano'}
        book = BookModel(**data)
        db.session.add(book)
        data1 = {'name': 'Tony', 'email': 'tony@gmail.com'}
        user = UserModel(**data1)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_book(self):
        resp = app.test_client().get('/add_book')._status_code
        self.assertEqual(resp, 200)

    def test_get_book(self):
        resp = app.test_client().get('/bookStop')._status_code
        self.assertEqual(resp, 200)

    def test_hide_book(self):
        resp = app.test_client().get('/hideStop')._status_code
        self.assertEqual(resp, 302)

    def test_show_book(self):
        resp = app.test_client().get('/showStop')._status_code
        self.assertEqual(resp, 302)

    def test_hideall_book(self):
        resp = app.test_client().get('/hideallTony')._status_code
        self.assertEqual(resp, 302)

    def test_add_wanted_book(self):
        resp = app.test_client().get('/add_wanted_bookTony')._status_code
        self.assertEqual(resp, 200)

    def test_add_user(self):
        resp = app.test_client().get('/add_user')._status_code
        self.assertEqual(resp, 200)

    def test_get_user(self):
        resp = app.test_client().get('/userTony')._status_code
        self.assertEqual(resp, 200)

    def test_send_email(self):
        resp = app.test_client().get('/send_emailTony')._status_code
        self.assertEqual(resp, 200)

    def test_library(self):
        resp = app.test_client().get('/library')._status_code
        self.assertEqual(resp, 200)

    def test_home(self):
        resp = app.test_client().get('/')._status_code
        self.assertEqual(resp, 200)

    def test_errors(self):
        resp = app.test_client().get('/test')._status_code
        self.assertEqual(resp, 404)


if __name__ == '__main__':
    Testing.run()

