from django.contrib.auth.models import AbstractUser
from django.db import models
from bank.models import Bank

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    egn = models.CharField(max_length=10, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    role = models.CharField(max_length= 20, default='Клиент')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

class Employee(AbstractUser):
    email = models.EmailField(unique=True)
    egn = models.CharField(max_length=10, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    role = models.CharField(max_length= 20, default='Служител')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='employee_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='employee_groups',
        blank=True
    )

    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)


class CreateEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)






