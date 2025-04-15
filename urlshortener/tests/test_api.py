from django.contrib.auth import get_user_model
from links.models import URL
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class APITestCase(APITestCase):
    fixtures = ['urls.json', 'users.json']

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.get(id=2)
        self.url1 = URL.objects.get(pk=1)
        self.url2 = URL.objects.get(pk=2)
        self.url3 = URL.objects.get(pk=3)
    
    def test_read_unauthenticated(self):
        self.client.logout()
        
        url = reverse_lazy('api_urls_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_read_authenticated(self):
        self.client.force_login(self.user)
        
        url = reverse_lazy('api_urls_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data, len(response.data) == 1)
        self.assertEqual(response.data[0]['url'], self.url3.url)
    
    def test_create_unauthenticated(self):
        self.client.logout()
        
        url = reverse_lazy('api_shorten_url')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_authenticated(self):
        self.client.force_login(self.user)

        data = {"url": "https://www.larian.com/"}
        url = reverse_lazy('api_shorten_url')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_url(self):
        self.client.force_login(self.user)

        data = {"url": "owly"}
        url = reverse_lazy('api_shorten_url')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
