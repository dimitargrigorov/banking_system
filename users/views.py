from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login, logout

from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматично влизане след регистрация
            return redirect("posts:list")  # Пренасочване след успешна регистрация
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request): 
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            login(request, form.get_user())
            return redirect("posts:list")

    else: 
        form = AuthenticationForm()
    return render(request, "login.html", { "form": form })


def logout_view(request):
    if request.method == "POST": 
        logout(request) 
        return redirect("posts:list")
    

