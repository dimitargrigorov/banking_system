from django.test import TestCase
from account.forms import OpenForm, CloseForm, CheckForm, RedemForm
from bank.models import Bank
from account.models import Account
from users.models import CustomUser

class TestForms(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='password123',
            role='Клиент'
        )
        self.bank = Bank.objects.create(
            bank_name='SuperBank'
        )
        self.account = Account.objects.create(
            owner=self.user,
            bank=self.bank,
            balance=23.5,
            user_number=1232145
        )

    def test_open_form_valid_data(self):
        form = OpenForm(data={
            'bank': self.bank,
            'balance':20
        })
        self.assertTrue(form.is_valid())

    def test_open_form_no_data(self):
        form = OpenForm(data={})
        self.assertFalse(form.is_valid())
    
    def test_close_form_valid_data(self):
        form = CloseForm(data={
            'bank': self.account.bank,
            'user_number':self.account.user_number
        })
        self.assertTrue(form.is_valid())