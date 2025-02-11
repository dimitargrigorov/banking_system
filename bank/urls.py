from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('create_bank/', views.create_bank, name="create_bank"),
    path('open_account/', views.open_account, name="open_account"),
    path('close_account/', views.close_account, name="close_account"),
    path('change_bank/', views. change_bank, name="change_bank"),
]