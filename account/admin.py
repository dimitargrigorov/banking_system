from django.contrib import admin
from .models import Account,MessageFromEmployee,MessageFromUser,MessageFromThird,Check
admin.site.register(Account)
admin.site.register(MessageFromEmployee)
admin.site.register(MessageFromUser)
admin.site.register(MessageFromThird)
admin.site.register(Check)