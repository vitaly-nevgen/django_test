from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.test import TestCase

from library.models import Author


class TestView(TestCase):

    def test_views(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'test.html')

    def test_other_view(self):
        response = self.client.get('/other/', {'exception': 'true'})
        self.assertEqual(response.status_code, 404)

        response = self.client.post('/other/')
        self.assertRedirects(response, '/', target_status_code=200)

        old_count = Author.objects.all().count()

        response = self.client.post('/other/', {
            'first_name': 'John',
            'last_name': 'Doe123',
            'bday': '2006-10-25 14:30:59'
        })

        new_count = Author.objects.all().count()

        self.assertEquals(new_count, old_count + 1)


        Author.objects.all().delete()
        user = User.objects.create_user(username='test1', password='test1')
        is_ok = self.client.login(username='test1', password='test1')
        self.assertTrue(is_ok)

        response = self.client.post('/other/', {
            'first_name': 'John',
            'last_name': 'Doe123',
            'bday': '2006-10-25 14:30:59'
        })

        self.assertEquals(Author.objects.first().created_by, user)
