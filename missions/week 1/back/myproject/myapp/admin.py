from django.contrib import admin

# Register your models here.
from .models import Brand
from .models import Sangpum
from .models import Type
from .models import User

admin.site.register(Brand)
admin.site.register(Sangpum)
admin.site.register(Type)
admin.site.register(User)
