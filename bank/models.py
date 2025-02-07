from django.db import models
from users.models import CustomUser


class Bank(models.Model):
    bank_name = models.CharField(max_length=75)
    def __str__(self):
        return self.bank_name
    
    def add_bank(self, bank_name):
        bank = Bank.objects.create(name=bank_name)
        return bank


    def check_balance(self, egn):
        return self.bank_accounts[egn]


class Account(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)