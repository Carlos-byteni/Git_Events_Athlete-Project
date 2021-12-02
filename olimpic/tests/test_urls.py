from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class URLTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_url_returns_200(self):
        url = '/game/personal'
        #response = self.client.get(url)
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)