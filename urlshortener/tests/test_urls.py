from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from links.models import URL
from django.urls import reverse_lazy


class URLsTestCase(TestCase):
    fixtures = ['urls.json', 'users.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(id=1)
        self.url1 = URL.objects.get(pk=1)
        self.url2 = URL.objects.get(pk=2)
        self.url3 = URL.objects.get(pk=3)

    def test_read_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('urls_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/urls/index/')

    def test_read_authenticated(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('urls_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/urls_list.html')

    def test_create_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('shorten_url'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/urls/shorten_url/')

    def test_create_authenticated(self):
        new_url = {
            "url": "https://www.larian.com/",
            "hash": "42874e422",
            "visits_count": 0,
            "created_at": "2025-04-04 00:02:02.000001+03",
            "user_id": 1
        }

        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('shorten_url'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/shortener.html')

        response = self.client.post(reverse_lazy('shorten_url'), new_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(URL.objects.get(id=5).url, 'https://www.larian.com/')
