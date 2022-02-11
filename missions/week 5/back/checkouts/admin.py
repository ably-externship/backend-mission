from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PaymentMethod)
admin.site.register(Transaction)
admin.site.register(TransactionItem)
