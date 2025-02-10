import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bankSystem.settings")
django.setup()

from bank.models import Bank,Account
from users.models import CustomUser

MIN_AGE = 18
def createAccount(bank_name, username, egn, age, balance):
    if age < MIN_AGE:
        print(f"Лицето с потребителско име {username} няма 18 години")
        return
    try:
        owner = CustomUser.objects.get(username = username)
        bank = Bank.objects.get(bank_name = bank_name)
        user_number = id((owner.egn, bank))
        new_account = Account(owner = owner, bank = bank, balance = balance, user_number = user_number)
        new_account.save()
    except CustomUser.DoesNotExist:
        print(f"Потребител с име {username} не съществува")
    except Bank.DoesNotExist:
        print(f"Банка с име {bank_name} не съществува")
    

def closeAccount(bank_name, user_number):
    try:
        bank = Bank.objects.get(bank_name = bank_name)
        account = Account.objects.get(bank = bank, user_number = user_number)
        account.delete()
    except Account.DoesNotExist:
        print(f"Сметка с потребителски номер {user_number} в банка {bank_name} не съществува")
    except Bank.DoesNotExist:
        print(f"Банка с име {bank_name} не съществува")


def transfer_balance_to_another_bank(current_bank_name, new_bank_name, user_number):
    if new_bank_name == current_bank_name:
        return
    try:
        current_bank = Bank.objects.get(bank_name = current_bank_name)
        new_bank = Bank.objects.get(bank_name = new_bank_name)
        current_account = Account.objects.get(bank = current_bank, user_number = user_number)
        owner = current_account.owner
        balance = current_account.balance
        new_account = Account(owner = owner, bank = new_bank, balance = balance, user_number = user_number)
        current_account.delete()
        new_account.save()
    except Account.DoesNotExist:
        print(f"Сметка с потребителски номер {user_number} в банка {current_bank_name} не съществува")
    except Bank.DoesNotExist:
        print(f"Банка с име {current_bank_name} не съществува")



def check_balance(user_number, bank_name):
    try:
        bank = Bank.objects.get(bank_name = bank_name)
        account = Account.objects.get(user_number = user_number, bank= bank)
        return account.balance
    except Account.DoesNotExist:
        print("Невалидни данни")
    except Bank.DoesNotExist:
        print(f"Банка с име {bank_name} не съществува")

def create_bank(bank_name):
    bank  = Bank(bank_name = bank_name)
    bank.save()

def send_check(bank_name, egn, uniq_code):
    pass

create_bank("ViscaBank")
