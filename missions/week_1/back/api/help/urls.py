from django.urls import path
from missions.week_1.back.api.help import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'help'

urlpatterns = [
    path('', views.get_help_list),
    path('create', csrf_exempt(views.create_help))
]