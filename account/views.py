from django.shortcuts import render,redirect
from .forms import OpenForm, CloseForm, Account
from users.models import Employee, MessageFromUser
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
            message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = bank)
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
            bank = form.cleaned_data['bank']
            user_number = form.cleaned_data['user_number']
            user_from = request.user
            employee = Employee.objects.filter(bank=bank, employment =False).first()
            message = f"Клиент {user_from.username} желае да затвори сметка."
            message_to_send = MessageFromUser(user_from = user_from, user_to = employee, message = message, bank = bank)
            message_to_send.save()
            employee.employment = True
            #try:
            #    account = Account.objects.get(bank=bank, user_number=user_number)
            #    account.delete()
            #    return redirect('account:open_account')
            #except Account.DoesNotExist:
            #    form.add_error(None, "Акаунтът не е намерен.")
    else:
        form = CloseForm()

    return render(request, 'close.html', {'form': form})