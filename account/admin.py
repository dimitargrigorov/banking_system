from django.contrib import admin
from .models import Account,MessageFromEmployee,MessageFromUser
admin.site.register(Account)
admin.site.register(MessageFromEmployee)
admin.site.register(MessageFromUser)