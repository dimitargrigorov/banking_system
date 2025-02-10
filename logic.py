import os
import django

# Настройки на Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bankSystem.settings")
django.setup()

from bank.models import Bank,Account
from users.models import CustomUser

def createAccount(owner_name, name_of_bank,balance):
    owner = CustomUser.objects.get(username = owner_name)
    bank = Bank.objects.get(bank_name = name_of_bank)
    new_account = Account(owner = owner, bank = bank, balance = balance)
    new_account.save()

def closeAccount(bank_name, egn):
    owner = CustomUser.objects.get(egn = egn)
    bank = Bank.objects.get(bank_name = bank_name)
    account = Account.objects.get(owner = owner, bank = bank)
    account.delete()


closeAccount("UniCredit", 32135)
