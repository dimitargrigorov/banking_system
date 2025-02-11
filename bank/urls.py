from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('create_bank/', views.create_bank, name="create_bank"),
]