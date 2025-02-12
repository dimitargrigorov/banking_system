from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from account.models import MessageFromUser,MessageFromEmployee,Employee,CustomUser,Account
# Create your views here.


def profile(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    user = request.user
    return render(request, 'posts/profile.html', {'user': user})


def show_message(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    if request.user.role == "Клиент" or request.user.role == "Трето лице":
        messages = MessageFromEmployee.objects.filter(user_to = request.user)
        return render(request, 'posts/user_message.html', {'messages': messages})
    else:
        messages = MessageFromUser.objects.filter(user_to = request.user)
        return render(request, 'posts/employee_message.html', {'messages': messages})
    

def welcome(request):
    return render(request, 'posts/welcome.html')


def chose_action(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Одобри':
            pass
        elif action == 'Откажи':
            pass
    else:
        return render(request, 'show_message.html')
    

def approve_account(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(MessageFromUser, id=message_id)
        account = Account(owner=message.user_from, bank=message.bank, balance=message.balance, user_number=message.user_number)
        content_message = f"Одобрено отваряне на сметка от служител {message.user_to}."
        message_to_send = MessageFromEmployee(user_from = message.user_to, user_to =message.user_from, message=content_message, user_number=message.user_number)
        message_to_send.save()
        account.save()
        message.delete()
        return redirect("posts:message")

    return redirect("posts:message")


def reject_account(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(MessageFromUser, id=message_id)
        message.delete()
        return redirect("posts:message")
    return redirect("posts:message")
    
    