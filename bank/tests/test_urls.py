from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bank.views import create_bank, create_employee

class TestUrls(SimpleTestCase):
    def test_create_bank(self):
        url = reverse('bank:create_bank')
        self.assertEqual(resolve(url).func, create_bank)
    
    def test_create_employee(self):
        url = reverse('bank:create_employee')
        self.assertEqual(resolve(url).func, create_employee)