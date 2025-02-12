from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('create_bank/', views.create_bank, name="create_bank"),
    path('create_employee/', views.create_employee, name="create_employee"),
]