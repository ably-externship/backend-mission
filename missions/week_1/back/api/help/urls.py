from django.urls import path
from missions.week_1.back.api.help import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'help'

urlpatterns = [
    path('', views.help_list_view),
    path('form', views.help_form_view),
    path('create', csrf_exempt(views.create_help))
]