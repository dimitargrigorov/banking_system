from django import forms
from .models import Account

class OpenForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'balance']


class CloseForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'user_number']