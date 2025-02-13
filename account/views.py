from django.shortcuts import render,redirect
from .forms import OpenForm, CloseForm, Account
from account.models import Employee, MessageFromUser
from bank.forms import ChangeForm
from bank.models import Bank


def open_account(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    if request.method == "POST":
        form = OpenForm(request.POST)
        if form.is_valid():
            bank = form.cleaned_data['bank']
            balance = form.cleaned_data['balance']
            user_number = id((bank, request.user))
            user_from = request.user
            employee = Employee.objects.filter(bank=bank, employment =False).first()
            message = f"Клиент {user_from.username} желае да отвори сметка."
            message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = bank, balance = balance, user_number = user_number)
            message_to_send.save()
            employee.employment = True
    else:
        form = OpenForm()

    return render(request, 'open.html', {'form': form})


def close_account(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    if request.method == "POST":
        form = CloseForm(request.POST)
        if form.is_valid():
            try:
                bank = form.cleaned_data['bank']
                user_number = form.cleaned_data['user_number']
                user_from = request.user
                account = Account.objects.get(bank=bank, user_number=user_number)
                employee = Employee.objects.filter(bank=bank, employment =False).first()
                message = f"Клиент {user_from.username} желае да затвори сметка."
                message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = bank, balance=account.balance, user_number=account.user_number)
                message_to_send.save()
                employee.employment = True
                return redirect('account:open_account')
            except Account.DoesNotExist:
                form.add_error(None, "Акаунтът не е намерен.")
    else:
        form = CloseForm()

    return render(request, 'close.html', {'form': form})


def change_bank(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    if request.method == "POST":
        form = ChangeForm(request.POST)
        if form.is_valid():
            current_bank_name = form.cleaned_data['current_bank_name']
            new_bank_name = form.cleaned_data['new_bank_name']
            user_number = form.cleaned_data['user_number']
            try:
                current_bank = Bank.objects.get(bank_name = current_bank_name)
                new_bank = Bank.objects.get(bank_name = new_bank_name)
                current_account = Account.objects.get(bank = current_bank, user_number = user_number)
                owner = current_account.owner
                balance = current_account.balance
                new_account = Account(owner = owner, bank = new_bank, balance = balance, user_number = user_number)

                user_from = request.user
                employee = Employee.objects.filter(bank=new_bank, employment =False).first()
                message = f"Клиент {user_from.username} желае да премести сметката от банка {current_bank_name} в банка {new_bank_name}."
                message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = new_bank,balance = balance,user_number = user_number)
                message_to_send.save()
                employee.employment = True

            except Account.DoesNotExist:
                form.add_error(None, "Акаунтът не е намерен.")
            except Bank.DoesNotExist:
                form.add_error(None, f"Банка с име {current_bank_name} или {new_bank_name} не е намерена")
    else:
        form = ChangeForm()

    return render(request, 'change.html', {'form': form})