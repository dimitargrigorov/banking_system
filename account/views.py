from django.shortcuts import render,redirect
from .forms import OpenForm, CloseForm, Account,CheckForm,RedemForm,BalanceForm
from account.models import Employee, MessageFromUser,Check,MessageFromThird
from bank.forms import ChangeForm
from bank.models import Bank
from django.core.exceptions import PermissionDenied


def open_account(request):
    if not request.user.is_authenticated or request.user.role != 'Клиент':
        return redirect('users:login')
    if request.method == 'POST':
        form = OpenForm(request.POST)
        if form.is_valid():
            bank = form.cleaned_data['bank']
            user_from = request.user
            balance = form.cleaned_data['balance']
            try:
                account = Account.objects.get(owner=user_from, bank=bank)
            except Account.DoesNotExist:
                user_number = id((bank, request.user))
                employee = Employee.objects.filter(bank=bank, employment =False).first()
                message = f'Клиент {user_from.username} желае да отвори сметка.'
                message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = bank, balance = balance, user_number = user_number)
                message_to_send.save()
                employee.employment = True
                employee.save()
            else:
                form.add_error(None, f'Вече притежавате акаунт в {bank.bank_name}! ' )
                raise AssertionError

    else:
        form = OpenForm()

    return render(request, 'open.html', {'form': form})


def close_account(request):
    if not request.user.is_authenticated or request.user.role != 'Клиент':
        return redirect('users:login')
    if request.method == 'POST':
        form = CloseForm(request.POST)
        if form.is_valid():
            try:
                bank = form.cleaned_data['bank']
                user_number = form.cleaned_data['user_number']
                user_from = request.user
                account = Account.objects.get(bank=bank, user_number=user_number)
                employee = Employee.objects.filter(bank=bank, employment =False).first()
                message = f'Клиент {user_from.username} желае да затвори сметка.'
                message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = bank, balance=account.balance, user_number=account.user_number)
                message_to_send.save()
                employee.employment = True
                employee.save()
                return redirect('account:open_account')
            except Account.DoesNotExist:
                form.add_error(None, 'Акаунтът не е намерен или вече е изтрит!')
            except Employee.DoesNotExist:
                form.add_error(None, 'В монента няма служител който да одобри затварянето моля исчакайте.')
            
    else:
        form = CloseForm()

    return render(request, 'close.html', {'form': form})


def change_bank(request):
    if not request.user.is_authenticated or request.user.role != 'Клиент':
        return redirect('users:login')
    if request.method == 'POST':
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
                message = f'Клиент {user_from.username} желае да премести сметката от банка {current_bank_name} в банка {new_bank_name}.'
                message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = new_bank,balance = balance,user_number = user_number)
                message_to_send.save()
                employee.employment = True
                employee.save()
            except Account.DoesNotExist:
                form.add_error(None, 'Акаунтът не е намерен.')
                raise PermissionDenied
            except Bank.DoesNotExist:
                form.add_error(None, f'Банка с име {current_bank_name} или {new_bank_name} не е намерена')
                raise PermissionDenied
    else:
        form = ChangeForm()

    return render(request, 'change.html', {'form': form})


def send_check(request):
    if not request.user.is_authenticated or request.user.role != 'Трето лице':
        return redirect('users:login')
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            form.save()
            content_message = f'{request.user.username} ви изпраща чек на стойност {form.cleaned_data['value']}!'
            message_to_send = MessageFromThird(user_from=request.user, user_to=form.cleaned_data['reciever'], message=content_message,uniq_code=form.cleaned_data['uniq_code'] )
            message_to_send.save()
            return redirect('posts:message')
    else:
        form = CheckForm()

    return render(request, 'send_check.html', {'form': form})


def redem_check(request):
    if not request.user.is_authenticated or request.user.role != 'Клиент':
        return redirect('users:login')
    if request.method == 'POST':
        form = RedemForm(request.POST)
        if form.is_valid():
            reciever = form.cleaned_data['reciever']
            uniq_code = form.cleaned_data['uniq_code']
            try:
                check = Check.objects.get(reciever=reciever,uniq_code=uniq_code)
                bank = check.bank
                account = Account.objects.get(owner=reciever,bank=bank)
                account.balance += check.value
                account.save()
                check.delete()
                form.save()
            except Check.DoesNotExist:
                form.add_error(None, 'Невалиден чек')
                raise PermissionDenied

            except Account.DoesNotExist:
                form.add_error(None, 'Акаунтът не е намерен.')
                raise PermissionDenied
    else:
        form = RedemForm()

    return render(request, 'redem.html', {'form': form})

def check_balance(request):
    if not request.user.is_authenticated or request.user.role != 'Клиент':
        return redirect('users:login')
    balance = None
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            bank = form.cleaned_data['bank']
            user_number = form.cleaned_data['user_number']
            try:
                account = Account.objects.get(bank=bank, user_number=user_number)
                balance = account.balance
            except Account.DoesNotExist:
                form.add_error(None, 'Акаунтът не е намерен.')
                raise PermissionDenied
    else:
        form = BalanceForm()

    return render(request, 'check_balance.html', {'form': form, 'balance':balance})