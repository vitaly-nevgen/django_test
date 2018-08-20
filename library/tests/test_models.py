from datetime import datetime

from django.contrib.auth.models import User
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

    def test_created_by(self):
        user = User.objects.create(
            username="test_user",
            password="123"
        )
        self.author = Author.objects.create(
            first_name="John",
            last_name="Doe",
            bday=datetime.now()
        )
        self.assertEqual(
            self.author.get_user_username(),
            None
        )
        self.author.created_by = user
        self.author.save()
        self.author.refresh_from_db()

        self.assertEquals(
            self.author.get_user_username(),
            user.username
        )

