from django.shortcuts import render,redirect
from .models import Post

# Create your views here.


def posts_list(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    user = request.user
    return render(request, 'posts/posts_list.html', {'user': user})


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})