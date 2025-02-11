from django.shortcuts import render,redirect
from .forms import BankForm, OpenForm, CloseForm,Account

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