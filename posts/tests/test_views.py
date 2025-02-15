from django.urls import reverse
from django.test import TestCase, Client
from posts.models import Post
from users.models import CustomUser, Employee
from bank.models import Bank
from account.models import MessageFromUser,MessageFromEmployee
from account.models import Account
class TestProfile(TestCase):

    def test_profile_authenticated_user(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='password231'
        )
        self.client = Client()
        self.client.login(username=self.user.username, password='password231')
        response = self.client.get(reverse('posts:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/profile.html')

    def test_profile_not_authenticated_user(self):
        response = self.client.get(reverse('posts:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))


class TestShowMessage(TestCase):
    def test_show_message_authenticated_user(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='password231',
            role='Клиент'
        )
        self.client = Client()
        self.client.login(username=self.user.username, password='password231')
        response = self.client.get(reverse('posts:message'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/user_message.html')

    def test_show_message_authenticated_employee(self):
        self.user = CustomUser.objects.create_user(
            username='testemployee',
            email='testemployee@gmail.com',
            password='password231',
            role='Служител'
        )
        self.client = Client()
        self.client.login(username=self.user.username, password='password231')
        response = self.client.get(reverse('posts:message'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/employee_message.html')

    def test_profile_not_authenticated_user(self):
        response = self.client.get(reverse('posts:message'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))


class TestOpenCloseChange(TestCase):
    def setUp(self):
        self.client = Client()
        self.bank = Bank.objects.create(
            bank_name="TestBank")
        self.user = CustomUser.objects.create_user(
            username="testuser", 
            email="test@example.com", 
            password="password123", 
            role="Клиент")
        self.employee = Employee.objects.create_user(
            username='testemployee',
            email='employee@gmail.com',
            password='password2025',
            role='Служител',
            bank= self.bank,
            employment='False'
        )
        self.message = MessageFromUser.objects.create(
            user_from=self.user,
            user_to=self.employee,
            message = f'Клиент {self.user.username} желае да затвори сметка.',
            bank=self.bank,
            balance=100,
            user_number=3414151512
        )

    def test_aprove_open_account(self):
        message = MessageFromUser.objects.create(
            user_from=self.user,
            user_to=self.employee,
            message = f'Клиент {self.user.username} желае да отвори сметка.',
            bank=self.bank,
            balance=100.0,
            user_number=123456
        )
        response = self.client.post(reverse('posts:approve_open',args=[message.pk]))
        self.assertTrue(Account.objects.exists())
        self.assertEqual(response.status_code, 302)
        

    def test_aprove_close_account_exist(self):
        
        account = Account.objects.create(
            owner = self.user,
            bank = self.bank,
            balance = 100,
            user_number = 3414151512
        )
        self.assertTrue(Account.objects.exists())
        response = self.client.post(reverse('posts:approve_close',args=[self.message.pk]))
        self.assertFalse(Account.objects.exists())
        self.assertEqual(response.status_code, 302)

    def test_aprove_close_account_not_exist(self):
        self.assertFalse(Account.objects.exists())
        response = self.client.post(reverse('posts:approve_close',args=[self.message.pk]))
        self.assertEqual(response.status_code, 403)

    def test_reject_message_deleted(self):
        response = self.client.post(reverse('posts:reject',args=[self.message.pk]))
        self.assertFalse(MessageFromUser.objects.exists())
        self.assertTrue(self.employee.employment)
        self.assertEqual(response.status_code, 302)

    def test_aprove_change_account_exist(self):
        account = Account.objects.create(
            owner = self.user,
            bank = self.bank,
            balance = 100,
            user_number = 3414151512
        )
        new_bank = Bank.objects.create(
            bank_name = 'Bank2'
        )
        message = MessageFromUser.objects.create(
            user_from=self.user,
            user_to=self.employee,
            message = f'Клиент {self.user.username} желае да премести сметката от банка {self.bank.bank_name} в банка {new_bank.bank_name}.',
            bank=self.bank,
            balance=100,
            user_number=3414151512
        )
        self.assertTrue(Account.objects.exists())
        self.assertFalse(MessageFromEmployee.objects.exists())
        self.assertTrue(MessageFromUser.objects.exists())
        response = self.client.post(reverse('posts:approve_change',args=[message.pk]))
        self.assertTrue(Account.objects.exists())
        self.assertEqual(MessageFromUser.objects.count(), 1)
        self.assertTrue(MessageFromEmployee.objects.exists())
        self.assertEqual(response.status_code, 302)
    