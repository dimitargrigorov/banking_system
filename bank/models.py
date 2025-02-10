from django.db import models
from users.models import CustomUser


class Bank(models.Model):
    bank_name = models.CharField(max_length=75)
    def __str__(self):
        return self.bank_name
    



class Account(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.SET_NULL)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    user_number = models.IntegerField(default=0)