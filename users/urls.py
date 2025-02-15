from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('register_third_person/', views.register_third_person, name='register_third_person'),
    path('add_employee/', views.add_employee, name='add_employee'),
]