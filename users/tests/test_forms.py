from django.test import TestCase
from users.forms import CustomUserCreationForm, EmployeeCreationForm, CreateEmployeeForm
from bank.models import Bank
from users.models import Employee
class TestForms(TestCase):

    def test_CustomUserCreationForm_valid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'test@gmail.com',
            'egn': '2342345678',
            'age': 22,
            'password1': 'TestPass123!',
            'password2': 'TestPass123!'
        })
        self.assertTrue(form.is_valid())
    
    def test_CustomUserCreationForm_no_data(self):
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())

    def test_EmployeeCreationForm_valid_data(self):
        form = EmployeeCreationForm(data={
            'username': 'testuser',
            'email': 'test@gmail.com',
            'egn': '2342345678',
            'age': 22,
            'password1': 'тestPass123!',
            'password2': 'тestPass123!'
        })
        self.assertTrue(form.is_valid())
    
    def test_EmployeeCreationForm_no_data(self):
        form = EmployeeCreationForm(data={})
        self.assertFalse(form.is_valid())

    def test_CreateEmployeeForm_valid_data(self):
        bank = Bank.objects.create(bank_name='TestBank')
        employee = Employee.objects.create_user(
            username='testemployee',
            email='employee@gmail.com',
            password='password2025',
            role='Служител',
            bank= bank,
            employment='False'
        )
        form = CreateEmployeeForm(data={
            'employee':employee,
            'bank':bank.pk
        })
        self.assertTrue(form.is_valid())
    
    def test_CreateEmployeeForm_no_data(self):
        form = CreateEmployeeForm(data={})
        self.assertFalse(form.is_valid())