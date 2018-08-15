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

