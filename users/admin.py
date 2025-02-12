from django.contrib import admin
from .models import CustomUser,Employee,MessageFromUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'egn', 'age', 'role']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Employee)
admin.site.register(MessageFromUser)
