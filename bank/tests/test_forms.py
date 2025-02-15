from django.test import TestCase
from bank.forms import BankForm,ChangeForm
from bank.models import Bank, Change


class TestForms(TestCase):

    def setUp(self):
        self.bank1 = Bank.objects.create(
            bank_name='Bank1'
        )
        self.bank2 = Bank.objects.create(
            bank_name='Bank2'
        )

    def test_BankForm_valid_data(self):
        form = BankForm(data={
            'bank_name': self.bank1.bank_name,
        })
        self.assertTrue(form.is_valid())

    def test_BankForm_no_data(self):
        form = BankForm(data={})
        self.assertFalse(form.is_valid())
    
    def test_ChangeForm_valid_data(self):
        form = ChangeForm(data={
            'current_bank_name': self.bank1.bank_name,
            'new_bank_name':self.bank2.bank_name,
            'user_number':1231412
        })
        self.assertTrue(form.is_valid())

    def test_ChangeForm_no_data(self):
        form = ChangeForm(data={})
        self.assertFalse(form.is_valid())