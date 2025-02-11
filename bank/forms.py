from django import forms
from .models import Bank,Change

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['bank_name']


class ChangeForm(forms.ModelForm):
    class Meta:
        model = Change
        fields = ['current_bank_name', 'new_bank_name', 'user_number']


