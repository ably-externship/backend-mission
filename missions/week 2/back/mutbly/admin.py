from django.contrib import admin
from .models import Item, Quantity, Question

admin.site.register(Item)
admin.site.register(Quantity)
admin.site.register(Question)