from django import forms
from .models import Account,Check,Redem

class OpenForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'balance']


class CloseForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['bank', 'user_number']


class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['reciever', 'uniq_code', 'value','bank']


class RedemForm(forms.ModelForm):
    class Meta:
        model = Redem
        fields = ['reciever', 'uniq_code']

