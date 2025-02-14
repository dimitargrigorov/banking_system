from django.urls import reverse
from django.test import TestCase, Client
from account.models import Account, MessageFromUser, MessageFromEmployee, MessageFromThird, Check, Redem
from users.models import CustomUser, Employee
from bank.models import Bank
from django.core.exceptions import PermissionDenied
class TestOpenAccount(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.bank = Bank.objects.create(bank_name='SuperBank')

    def test_open_account_GET_authenticated(self):
        self.client.login(username=self.user.username, password='password123')
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


class TestCloseAccount(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.bank = Bank.objects.create(bank_name='SuperBank')
    
    def test_close_account_GET_authenticated(self):
        self.client.login(username=self.user.username, password='password123')
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
        with self.assertRaises(Account.DoesNotExist):  
            Account.objects.get(owner=self.user, bank=self.bank)


class TestChangeBank(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.user = Employee.objects.create_user(
            username='testemployee',
            email='employee@gmail.com',
            password='password2025',
            role='Служител'
        )
        self.bank1 = Bank.objects.create(bank_name='Bank1')
        self.bank2 = Bank.objects.create(bank_name='Bank2')
        self.account = Account.objects.create(
            owner = self.user,
            bank = self.bank1,
            balance = 33.23,
            user_number = 3414151512
        )


    def test_change_bank_GET_authenticated(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.get(reverse('account:change_bank'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change.html')
    
    def test_change_bank_not_existed_bank(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.post(reverse('account:change_bank'), {
            'current_bank_name': self.bank1.bank_name,
            'new_bank_name': 'BancaIntesa',
            'user_number':3414151512
        })
        self.assertEqual(response.status_code, 403)

    def test_change_bank_succes(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.post(reverse('account:change_bank'), {
            'current_bank_name': self.bank1.bank_name,
            'new_bank_name': self.bank2.bank_name,
            'user_number':3414151512
        })
        self.assertEqual(response.status_code, 200)
    


        


    




    

