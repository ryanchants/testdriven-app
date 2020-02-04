# services/users/project/tests/test_user_model.py

import unittest

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase

from sqlalchemy.exc import IntegrityError

from project.tests.utils import add_user


class TestUserModel(BaseTestCase):
    def test_add_user(self):
        user = add_user(username="justatest", email="test@test.com")
        self.assertTrue(user.id)
        self.assertEqual(user.username, "justatest")
        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):
        add_user(username="justatest", email="test@test.com")
        with self.assertRaises(IntegrityError):
            add_user(username="justatest", email="test@test2.com")

    def test_add_user_duplicate_email(self):
        add_user(username="justatest", email="test@test.com")
        with self.assertRaises(IntegrityError):
            add_user(username="justanothertest", email="test@test.com")

    def test_to_json(self):
        user = add_user(username="justatest", email="test@test.com")
        self.assertTrue(isinstance(user.to_json(), dict))


if __name__ == '__main__':
    unittest.main()
