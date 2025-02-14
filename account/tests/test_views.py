from django.urls import reverse
from django.test import TestCase, Client
from account.models import Account, MessageFromUser, MessageFromEmployee, MessageFromThird, Check, Redem
from users.models import CustomUser, Employee
from bank.models import Bank
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_open_account_GET_authenticated(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('account:open_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'open.html')
    
    def test_open_account_GET_not_authenticated(self):
        response = self.client.get(reverse('account:open_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))

    def test_open_account_GET_role_third(self):
        user = CustomUser.objects.create(
            username='user2',
            email='user2@gmail.com',
            password='password123', 
            role='Трето лице'
        )
        self.client.login(username='user2', password='password123')
        response = self.client.get(reverse('account:open_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))
    
    def test_open_account_GET_role_employee(self):
        user = CustomUser.objects.create(
            username='user2',
            email='user2@gmail.com',
            password='password123', 
            role='Служител'
        )
        self.client.login(username='user2', password='password123')
        response = self.client.get(reverse('account:open_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))
    
    def test_close_account_GET_authenticated(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('account:close_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'close.html')
    
    def test_close_account_GET_not_authenticated(self):
        response = self.client.get(reverse('account:close_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))

    def test_close_account_GET_role_third(self):
        user = CustomUser.objects.create(
            username='user2',
            email='user2@gmail.com',
            password='password123', 
            role='Трето лице'
        )
        self.client.login(username='user2', password='password123')
        response = self.client.get(reverse('account:close_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))
    
    def test_close_account_GET_role_employee(self):
        user = CustomUser.objects.create(
            username='user2',
            email='user2@gmail.com',
            password='password123', 
            role='Служител'
        )
        self.client.login(username='user2', password='password123')
        response = self.client.get(reverse('account:close_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))

    def test_close_not_existent_account(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        bank = Bank.objects.create(bank_name='SuperBank')
        with self.assertRaises(Account.DoesNotExist):  
            Account.objects.get(owner=user, bank=bank)

    




    

