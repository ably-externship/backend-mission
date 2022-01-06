from django.contrib import admin
from .models import Product_qna
class QnaAdmin(admin.ModelAdmin):
    list_display = ('content', )

admin.site.register(Product_qna,QnaAdmin)
