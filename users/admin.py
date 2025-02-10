from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'egn', 'age', 'role']
    # Добавете повече полета, които искате да показвате в админ панела

admin.site.register(CustomUser, CustomUserAdmin)
