from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('open_account/', views.open_account, name='open_account'),
    path('close_account/', views.close_account, name='close_account'),
    path('change_bank/', views.change_bank, name='change_bank'),
    path('send_check/', views.send_check, name='send_check'),
    path('redem_check/', views.redem_check, name='redem_check'),
    path('check_balance/', views.check_balance, name='check_balance'),
]