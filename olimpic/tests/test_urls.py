from django.test import SimpleTestCase
from django.urls.base import reverse



class AdminTest(SimpleTestCase):

    def test_admin_status(self):
        '''Teste da url admin'''
        resp = self.client.get('admin/')
        self.assertEqual(resp.status_code, 200)

    def test_url_path(self):
        '''Teste da url da rota'''
        resp = self.client.get(reverse('personal'))
        self.assertEqual(resp.status_code,200)
        



