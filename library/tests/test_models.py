from datetime import datetime
from django.test import TestCase

from library.models import Author


class TestModels(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="John",
            last_name="Doe",
            bday=datetime.now()
        )

    def test_author(self):
        self.assertEqual(
            str(self.author),
            "John, Doe"
        )

    def test_get_user_username(self):
        self.assertEqual(
            self.author.get_user_username(),
            self.author.created_by
        )

