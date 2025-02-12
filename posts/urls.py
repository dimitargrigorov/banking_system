from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('message/', views.show_message, name="message"),
    path('welcome/', views.welcome, name="welcome"),
    path('profile/', views.profile, name="profile"),
]