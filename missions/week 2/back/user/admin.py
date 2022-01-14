from django.contrib import admin
from .models import Account

class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Account,UserAdmin)
