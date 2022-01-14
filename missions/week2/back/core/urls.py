from django.urls import path
from clothes import views as clothes_views

app_name = "core"

urlpatterns = [path("", clothes_views.all_clothes, name="home")]
