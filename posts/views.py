from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from account.models import MessageFromUser,MessageFromEmployee,Employee,CustomUser,Account,MessageFromThird


def profile(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    user = request.user
    return render(request, 'posts/profile.html', {'user': user})


def show_message(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    if request.user.role == "Клиент":
        messages_from_employee = MessageFromEmployee.objects.filter(user_to = request.user)
        messages_from_third = MessageFromThird.objects.filter(user_to=request.user)
        messages = list(messages_from_employee) + list(messages_from_third)
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
    

def approve_open(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(MessageFromUser, id=message_id)
        account = Account(owner=message.user_from, bank=message.bank, balance=message.balance, user_number=message.user_number)
        content_message = f"Одобрено отваряне на сметка от служител {message.user_to}."
        message_to_send = MessageFromEmployee(user_from = message.user_to, user_to =message.user_from, message=content_message, user_number=message.user_number)
        message_to_send.save()
        account.save()
        message.user_to.employment = False
        message.user_to.save()
        message.delete()
        return redirect("posts:message")

    return redirect("posts:message")


def approve_close(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(MessageFromUser, id=message_id)
        account = Account.objects.get(user_number = message.user_number)
        content_message = f"Успешно затвяряне на сметка, служител {message.user_to}."
        message_to_send = MessageFromEmployee(user_from = message.user_to, user_to =message.user_from, message=content_message, user_number=message.user_number)
        message_to_send.save()
        account.delete()
        message.user_to.employment = False
        message.user_to.save()
        message.delete()
        return redirect("posts:message")

    return redirect("posts:message")


def reject(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(MessageFromUser, id=message_id)
        message.user_to.employment = False
        message.user_to.save()
        message.delete()
        return redirect("posts:message")
    return redirect("posts:message")


def approve_change(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(MessageFromUser, id=message_id)
        account = Account.objects.get(user_number = message.user_number)
        content_message = f"Одобрено смяна на банката, служител {message.user_to}."
        message_to_send = MessageFromEmployee(user_from = message.user_to, user_to =message.user_from, message=content_message, user_number=message.user_number)
        new_account = Account(owner=message.user_from, bank=message.bank, balance=message.balance, user_number=message.user_number)
        message_to_send.save()
        account.delete()
        new_account.save()
        message.user_to.employment = False
        message.user_to.save()
        message.delete()
        return redirect("posts:message")

    return redirect("posts:message")

    
    