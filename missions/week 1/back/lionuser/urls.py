from django.urls import path

from .views import RegisterView ,userLogin, login,loginTest

from django.urls import path
from . import views
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', userLogin, name="login"),
    path('login/jwt', login, name="login_jwt"),
    path('login/test', loginTest, name="login_test"),

]