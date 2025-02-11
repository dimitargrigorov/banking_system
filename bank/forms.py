from django import forms
from .models import Bank, Account,Change

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['bank_name']


class OpenForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'balance']


class CloseForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'user_number']


class ChangeForm(forms.ModelForm):
    class Meta:
        model = Change
        fields = ['current_bank_name', 'new_bank_name', 'user_number']


