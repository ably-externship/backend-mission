from django.contrib import admin
from .models import Item, Quantity, Question, Brand

admin.site.register(Item)
admin.site.register(Quantity)
admin.site.register(Question)
admin.site.register(Brand)