from django.db import models
from users.models import CustomUser
from bank.models import Bank

class Account(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    user_number = models.IntegerField(default=0, null=True, blank=True)