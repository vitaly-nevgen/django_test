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

    def test_fields_ok(self):
        data1 = {
            'first_name': 'John',
            'last_name': 'Doe123',
            'bday': datetime.now() - timedelta(days=365)
        }
        form = OtherAuthorForm(data1)
        is_valid = form.is_valid()
        self.assertTrue(is_valid)

    def test_field_first_name_error(self):
        data = {
            'first_name': 'John' * 6,
            'last_name': 'Doe123',
            'bday': datetime.now() - timedelta(days=365)
        }
        form = OtherAuthorForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors['first_name'])
