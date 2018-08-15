from django.test import TestCase


class TestView(TestCase):

    def test_views(self):
        response = self.client.get('/123')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/123', data={
            'render': 'true'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'test.html')
