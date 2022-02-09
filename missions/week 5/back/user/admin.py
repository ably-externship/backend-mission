from django.contrib import admin

from .models import User, User_recommand


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'email')


admin.site.register(User, UserAdmin)


class UserRecommandAdmin(admin.ModelAdmin):
    list_display = ('id', 'keyword1', 'keyword2', 'keyword3','user')


admin.site.register(User_recommand, UserRecommandAdmin)

