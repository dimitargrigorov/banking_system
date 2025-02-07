from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    egn = forms.CharField(max_length=10, required=True, label="ЕГН")
    age = forms.IntegerField(required=True, label="Години")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'egn', 'age', 'role', 'password1', 'password2']
