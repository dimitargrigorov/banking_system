from django.shortcuts import render,redirect
from .forms import BankForm, OpenForm, CloseForm,Account, ChangeForm, Bank

def create_bank(request):
    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BankForm()

    return render(request, 'bank_form.html', {'form': form})

def open_account(request):
    if request.method == "POST":
        form = OpenForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OpenForm()

    return render(request, 'open.html', {'form': form})


def close_account(request):
    if request.method == "POST":
        form = CloseForm(request.POST)
        if form.is_valid():
            bank = form.cleaned_data['bank']
            user_number = form.cleaned_data['user_number']
            try:
                account = Account.objects.get(bank=bank, user_number=user_number)
                account.delete()
            except Account.DoesNotExist:
                form.add_error(None, "Акаунтът не е намерен.")
    else:
        form = CloseForm()

    return render(request, 'close.html', {'form': form})


def change_bank(request):
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
                current_account.delete()
                new_account.save()
            except Account.DoesNotExist:
                form.add_error(None, "Акаунтът не е намерен.")
            except Bank.DoesNotExist:
                form.add_error(None, f"Банка с име {current_bank_name} или {new_bank_name} не е намерена")
    else:
        form = ChangeForm()

    return render(request, 'change.html', {'form': form})
