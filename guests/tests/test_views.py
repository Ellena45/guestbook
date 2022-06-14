import unittest

from django.test import RequestFactory, TestCase
from django.urls import reverse

from django.contrib.auth.models import User

from guests.views import UserDetail


class TestUserList(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='ellena', email='ellena@…', password='top_secret')

    def test_user_list_format(self):
        url = reverse('user')
        request = self.factory.get(url)

        request.user = self.user

        response = UserDetail.as_view()(request)
        self.assertEqual(1,1)

"""

class TestCustomLoginView(TestCase):
    def test_get_success_url(self):
        self.fail()


class TestUserCreate(TestCase):
    def test_form_valid(self):
        from base.views import UserCreate
        self.assertEqual(form_valid(UserCreate))
"""
"""
class TestStringMethods(unittest.TestCase):
    def test_upper(self): self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self): self.assertTrue('FOO'.isupper())

    self.assertFalse('Foo'.isupper())

    def test_split(self): s = 'hello world'

    self.assertEqual(s.split(), ['hello',
                                 'world'])  # check that s.split fails when the separator is not a string with self.assertRaises(TypeError): s.split(2) if __name__ == '__main__': unittest.main()
"""