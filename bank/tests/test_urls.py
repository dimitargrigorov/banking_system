from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bank.views import create_bank

class TestUrls(SimpleTestCase):
    def test_create_bank(self):
        url = reverse('bank:create_bank')
        self.assertEqual(resolve(url).func, create_bank)