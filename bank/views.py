from django.shortcuts import render,redirect
from .forms import BankForm,ChangeForm, Bank
from account.models import Account
from users.models import Employee, MessageFromUser

def create_bank(request):
    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BankForm()

    return render(request, 'bank_form.html', {'form': form})


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
                message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = bank)
                message_to_send.save()
                employee.employment = True

            except Account.DoesNotExist:
                form.add_error(None, "Акаунтът не е намерен.")
            except Bank.DoesNotExist:
                form.add_error(None, f"Банка с име {current_bank_name} или {new_bank_name} не е намерена")
    else:
        form = ChangeForm()

    return render(request, 'change.html', {'form': form})


def create_employee(request):
    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BankForm()

    return render(request, 'bank_form.html', {'form': form})
