from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('open_account/', views.open_account, name="open_account"),
    path('close_account/', views.close_account, name="close_account"),
]