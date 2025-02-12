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

class Employee(CustomUser):
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)
    employment = models.BooleanField(default= False)


class CreateEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)


class MessageFromUser(models.Model):
    user_from = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True, related_name="sent_messages_from_user")
    user_to = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True, related_name="received_messages_from_employee")
    message = models.CharField(max_length=300, blank=True, null=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)


class MessageFromEmployee(models.Model):
    user_from = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, blank=True, related_name="sent_messages_from_employee")
    user_to = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True,related_name="received_messages_from_user")
    message = models.CharField(max_length=300, blank=True, null=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)








