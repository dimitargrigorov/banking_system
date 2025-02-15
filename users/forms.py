from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Employee, CreateEmployee

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    egn = forms.CharField(max_length=10, required=True, label="ЕГН")
    age = forms.IntegerField(required=True, label="Години")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'egn', 'age', 'password1', 'password2']

class EmployeeCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    egn = forms.CharField(max_length=10, required=True, label="ЕГН")
    age = forms.IntegerField(required=True, label="Години")

    class Meta:
        model = Employee
        fields = ['username', 'email', 'egn', 'age','password1', 'password2']

    
class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = CreateEmployee
        fields = ['employee', 'bank']