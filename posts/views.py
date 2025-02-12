from django.shortcuts import render,redirect
from .models import Post
from users.models import MessageFromUser,MessageFromEmployee,Employee,CustomUser
# Create your views here.


def profile(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    user = request.user
    return render(request, 'posts/profile.html', {'user': user})


def show_message(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    messages = MessageFromEmployee.objects.filter(user_to = request.user)
    return render(request, 'posts/show_message.html', {'messages': messages})

def welcome(request):
    return render(request, 'posts/welcome.html')
    
    