
from django.test import Client
from django.test.testcases import SimpleTestCase
from django.urls import reverse


class TestView(SimpleTestCase):
    '''Teste da das visualizações'''
    def test_get_url_view(self):
        client = Client()
        resp = client.get(reverse('olimpic.urls')) 
        self.assertEquals(resp.status_code, 200)
