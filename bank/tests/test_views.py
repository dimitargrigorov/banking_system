from django.urls import reverse
from django.test import TestCase, Client
from users.models import CustomUser
from bank.models import Bank,Change
class TestCreateBank(TestCase):

    def setUp(self):
        self.super_user = CustomUser.objects.create_superuser(
            username='superUser',
            email='superUser@gmail.com',
            password='password123',
        )
        self.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@gmail.com',
            password='password231'
        )
        self.client = Client()

    def test_create_bank_authenticated(self):
        self.client.login(username=self.super_user.username, password='password123')
        response = self.client.get(reverse('bank:create_bank'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bank_form.html')

    def test_create_bank_not_authenticated(self):
        response = self.client.get(reverse('bank:create_bank'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))

    def test_create_bank_not_superuser(self):
        self.client.login(username=self.user.username, password='password231')
        response = self.client.get(reverse('bank:create_bank'))
        self.assertEqual(response.status_code, 302)

    def test_invalid_form_does_not_create_bank(self):
        self.client.login(username=self.super_user.username, password='password123')
        response = self.client.post(reverse('bank:create_bank'),{'bank_name':''})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Bank.objects.exists())