from django.contrib import admin
from .models import Help


class HelpAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', )


admin.site.register(Help, HelpAdmin)