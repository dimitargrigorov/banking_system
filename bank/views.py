from django.shortcuts import render,redirect
from .forms import BankForm, ChangeForm 
from account.models import Account
from bank.models import Bank

def create_bank(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('users:login')
    if request.method == "POST":
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BankForm()

    return render(request, 'bank_form.html', {'form': form})
