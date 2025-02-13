from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('message/', views.show_message, name="message"),
    path('welcome/', views.welcome, name="welcome"),
    path('profile/', views.profile, name="profile"),
    path('approve_open/<int:message_id>/', views.approve_open, name='approve_open'),
    path('reject/<int:message_id>/', views.reject, name='reject'),
    path('approve_close/<int:message_id>/', views.approve_close, name='approve_close'),
    path('approve_change/<int:message_id>/', views.approve_change, name='approve_change'),
]