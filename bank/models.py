from django.db import models
from users.models import CustomUser


class Bank(models.Model):
    bank_name = models.CharField(max_length=75)
    

    def __str__(self):
        return self.bank_name
    

class Account(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    user_number = models.IntegerField(default=0)


class Task(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    TYPE_OF_TASKS = [
        ('open', 'open'),
        ('close', 'close'),
        ('change', 'change')
    ]
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)
    task = models.CharField(
        max_length=20,
        choices=TYPE_OF_TASKS,
        default='open',
    )
