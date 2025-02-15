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
    
    def test_close_account_authenticated(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.get(reverse('account:close_account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'close.html')
    
    def test_close_account_not_authenticated(self):
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
        self.bank1 = Bank.objects.create(bank_name='Bank1')
        self.bank2 = Bank.objects.create(bank_name='Bank2')
        self.account = Account.objects.create(
            owner = self.user,
            bank = self.bank1,
            balance = 33.23,
            user_number = 3414151512
        )
        self.employee = Employee.objects.create_user(
            username='testemployee',
            email='employee@gmail.com',
            password='password2025',
            role='Служител',
            bank= self.bank2,
            employment='False'
        )

    def test_change_bank_authenticated(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.get(reverse('account:change_bank'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'change.html')

    def test_change_bank_not_authenticated(self):
        response = self.client.get(reverse('account:change_bank'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))
    
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

    def test_change_account_not_existed_account(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.post(reverse('account:change_bank'), {
            'current_bank_name': self.bank2.bank_name,
            'new_bank_name': self.bank1.bank_name,
            'user_number':3414151512
        })
        self.assertEqual(response.status_code, 403)

    def test_change_bank_role_not_user(self):
        self.client.login(username=self.employee.username, password='password2025')
        response = self.client.get(reverse('account:change_bank'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))


class TestSendCheck(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='test_third',
            email='test@gmail.com',
            password='password123',
            role='Трето лице'
        )
        self.bank = Bank.objects.create(bank_name='Bank')

        self.employee = Employee.objects.create_user(
            username='testemployee',
            email='employee@gmail.com',
            password='password2025',
            role='Служител',
            bank= self.bank,
            employment='False'
        )

    def test_send_check_authenticated(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.get(reverse('account:send_check'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'send_check.html')

    def test_send_check_not_authenticated(self):
        response = self.client.get(reverse('account:send_check'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))

    def test_change_bank_role_not_third(self):
        self.client.login(username=self.employee.username, password='password2025')
        response = self.client.get(reverse('account:send_check'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))


class TestRedemCheck(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.bank = Bank.objects.create(bank_name='Bank')
        self.employee = Employee.objects.create_user(
            username='testemployee',
            email='employee@gmail.com',
            password='password2025',
            role='Служител',
            bank= self.bank,
            employment='False'
        )
        check = Check.objects.create(
            sender=self.employee,
            reciever=self.user,
            uniq_code='xyxyx',
            value=20,
            bank=self.bank
        )
       
    def test_redem_cehck_authenticated_valid_check(self):
        self.client.login(username=self.user.username, password='password123')
        self.account = Account.objects.create(
            owner = self.user,
            bank = self.bank,
            balance = 33.23,
            user_number = 3414151512
        )
        response = self.client.get(reverse('account:redem_check'),{
            'reciever': self.user.pk,
            'uniq_code': 'xyxyx'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'redem.html')

    def test_redem_check_not_authenticated(self):
        response = self.client.get(reverse('account:redem_check'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))

    def test_redem_check_role_not_user(self):
        self.client.login(username=self.employee.username, password='password2025')
        response = self.client.get(reverse('account:redem_check'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))
    
    def test_redem_check_not_exist(self):
        user2 = CustomUser.objects.create_user(
            username='testuser2',
            email='testuser2@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.client.login(username=user2.username, password='password123')
        response = self.client.post(reverse('account:redem_check'),{
            'reciever': user2.pk,
            'uniq_code': 'xyxyx'
        })
        self.assertEqual(response.status_code, 403)

    def test_redem_account_not_exist(self):
        user2 = CustomUser.objects.create_user(
            username='testuser2',
            email='testuser2@gmail.com',
            password='password123',
            role='Клиент'
        )
        check = Check.objects.create(
            sender=self.employee,
            reciever=user2,
            uniq_code='ccwqz',
            value=10,
            bank=self.bank
        )
        self.client.login(username=user2.username, password='password123')
        response = self.client.post(reverse('account:redem_check'),{
            'reciever': user2.pk,
            'uniq_code': 'ccwqz'
        })
        self.assertEqual(response.status_code, 403)

class TestCheckBalance(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.bank = Bank.objects.create(bank_name='Bank')
        self.account = Account.objects.create(
            owner = self.user,
            bank = self.bank,
            balance = 33.23,
            user_number = 3414151512
        )

    def test_check_baalnce_authenticated_ecist_account(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.get(reverse('account:check_balance'),{
            'bank':self.bank.pk,
            'user_number':self.account.user_number
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'check_balance.html')
        
    def test_send_baalnce_not_authenticated(self):
        response = self.client.get(reverse('account:check_balance'),{
            'bank':self.bank,
            'user_number':self.account.user_number
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))

    def test_check_balance_not_exist_account(self):
        self.client.login(username=self.user.username, password='password123')
        response = self.client.post(reverse('account:check_balance'),{
            'bank':self.bank.pk,
            'user_number':111112222
        })
        self.assertEqual(response.status_code, 403)
