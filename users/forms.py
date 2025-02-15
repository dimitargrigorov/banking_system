from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Employee, CreateEmployee

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'egn', 'age', 'password1', 'password2']

class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'email', 'egn', 'age','password1', 'password2']

    
class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = CreateEmployee
        fields = ['employee', 'bank']