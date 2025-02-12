from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate

from .forms import CustomUserCreationForm,EmployeeCreationForm, CreateEmployeeForm

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'Клиент'
            user.save()
            login(request, user)
            return redirect("posts:welcome")
    else:
        form = CustomUserCreationForm()
    return render(request, "register_user.html", {"form": form})


def register_employee(request):
    if request.method == "POST":
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'Служител'
            user.save()
            login(request, user)
            return redirect("posts:welcome")
    else:
        form = EmployeeCreationForm()
    return render(request, "register.employee.html", {"form": form})


def register_third_person(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'Трето лице'
            user.save()
            login(request, user)
            return redirect("posts:welcome")
    else:
        form = CustomUserCreationForm()
    return render(request, "register_third.html", {"form": form})


def login_view(request): 
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("posts:welcome")
            else:
                form.add_error(None, "Невалидни данни за вход.")

    else: 
        form = AuthenticationForm()

    return render(request, "login.html", { "form": form })


def logout_view(request):
    if request.method == "POST": 
        logout(request) 
        return redirect("posts:welcome")
    

def choose_role(request):
    if request.method == "POST":
        role = request.POST.get('role')
        if role in ["Клиент", "Служител", "Трето лице"]:
            request.session["role"] = role
        if role == 'Клиент':
            return redirect('users:register_user')
        elif role == 'Служител':
            return redirect('users:register_employee')
        elif role == 'Трето лице':
            return redirect('users:register_third_person') 
    else:
        return render(request, 'chose_role.html')
    

def add_employee(request):
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            employee.bank = form.cleaned_data['bank']
            employee.save()
           # return redirect("posts:list")
    else:
        form = CreateEmployeeForm()
    return render(request, "add_employee.html", {"form": form})
