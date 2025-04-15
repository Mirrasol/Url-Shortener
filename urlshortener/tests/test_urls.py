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
    
    def test_create_user_successful(self):
        new_user = {
            "username": "Devonian",
            "password1": "paleozoic04",
            "password2": "paleozoic04",
        }

        self.client.logout()

        response = self.client.get(reverse_lazy('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')

        response = self.client.post(reverse_lazy('sign_up'), new_user)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertTrue(get_user_model().objects.filter(username='Devonian').exists())
        self.assertEqual(get_user_model().objects.get(id=4).username, 'Devonian')

    def test_create_user_username_taken(self):
        new_user = {
            "username": "Ordovician",
            "password1": "paleozoic048",
            "password2": "paleozoic048",
        }

        self.client.logout()

        response = self.client.get(reverse_lazy('sign_up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')

        response = self.client.post(reverse_lazy('sign_up'), new_user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors['username'], ['A user with that username already exists.'])

    def test_read_url_list_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('urls_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/urls/index/')

    def test_read_url_list_authenticated(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('urls_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'links/urls_list.html')
        self.assertTrue(response.context['urls'].contains(self.url1))
        self.assertFalse(response.context['urls'].contains(self.url3))

    def test_create_url_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('shorten_url'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/urls/shorten_url/')

    def test_create_url_authenticated(self):
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
    
    def test_redirect_to_shortened_unauthenticated(self):
        url = "https://www.example.com/"
        hash = "423274e422"

        self.client.logout()

        response = self.client.get(reverse_lazy('redirect_url', kwargs={'hash': hash}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url, fetch_redirect_response=False)
    
    def test_redirect_to_shortened_authenticated(self):
        url = "https://www.example.com/"
        hash = "423274e422"

        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('redirect_url', kwargs={'hash': hash}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url, fetch_redirect_response=False)
