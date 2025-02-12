from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('message/', views.show_message, name="message"),
    path('welcome/', views.welcome, name="welcome"),
    path('profile/', views.profile, name="profile"),
    path('approve_account/<int:message_id>/', views.approve_account, name='approve_account'),
    path('reject_account/<int:message_id>/', views.reject_account, name='reject_account'),
]