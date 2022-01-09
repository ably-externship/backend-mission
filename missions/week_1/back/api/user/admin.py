from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


admin.register(User, UserAdmin)