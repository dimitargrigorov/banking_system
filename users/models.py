from django.contrib.auth.models import AbstractUser
from django.db import models
from bank.models import Bank

class CustomUser(AbstractUser):
    egn = models.CharField(max_length=10, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    role = models.CharField(max_length= 20, default='Клиент', blank=True)
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

class Employee(CustomUser):
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)
    employment = models.BooleanField(default= False, blank=True)


class CreateEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=False)
    bank = models.ForeignKey(Bank, null=True, blank=False, on_delete=models.SET_NULL)