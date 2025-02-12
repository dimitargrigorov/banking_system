from django.shortcuts import render,redirect
from .models import Post
from account.models import MessageFromUser,MessageFromEmployee,Employee,CustomUser
# Create your views here.


def profile(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    user = request.user
    return render(request, 'posts/profile.html', {'user': user})


def show_message(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    if request.user.role is "Клиент" or request.user.role is "Трето лице":
        messages = MessageFromEmployee.objects.filter(user_to = request.user)
        return render(request, 'posts/show_message.html', {'messages': messages})
    else:
        messages = MessageFromUser.objects.filter(user_to = request.user)
        return render(request, 'posts/show_message.html', {'messages': messages})
    

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
    
    