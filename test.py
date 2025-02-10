import os
import django

# Настройки на Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bankSystem.settings")
django.setup()

# Импортирай моделите
from bank.models import Account

# Извлечи всички акаунти
accounts = Account.objects.all()

# Принтирай данните
for account in accounts:
    print(f"ID: {account.id}, owner: {account.owner}, balance: {account.balance}")
