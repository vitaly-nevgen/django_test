from django.test import TestCase
from library.forms import AuthorForm, OtherAuthorForm
from datetime import timedelta, datetime


class TestForm(TestCase):
    def test_author_form(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'bday': datetime.now() - timedelta(days=365)
        }
        form = AuthorForm(data)
        self.assertTrue(form.is_valid())

        data['bday'] = datetime.now() + timedelta(days=365)
        form = AuthorForm(data)
        self.assertFalse(form.is_valid())


class TestOtherAuthorForm(TestCase):
    def test_clean_first_name(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'bday': datetime.now() - timedelta(days=365)
        }
        form = OtherAuthorForm(data)
        self.assertTrue(form.is_valid())

        data['first_name'] = 'Christopher'
        form = OtherAuthorForm(data)
        self.assertFalse(form.is_valid())

    def test_clean_last_name(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'bday': datetime.now() - timedelta(days=365)
        }
        form = OtherAuthorForm(data)
        self.assertTrue(form.is_valid())

        data['last_name'] = 'DRichardson'
        form = OtherAuthorForm(data)
        self.assertFalse(form.is_valid())
