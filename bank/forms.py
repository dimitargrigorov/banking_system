from django import forms
from .models import Bank, Account

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['bank_name']


class OpenForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['owner', 'bank', 'balance', 'user_number']

class CloseForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'user_number']