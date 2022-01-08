from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect

from users.forms import CustomAuthenticationForm
from users.models import User


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/product')
    return render(request, 'auth/login.html', {'form': CustomAuthenticationForm})


def logout_call(request):
    logout(request)
    return redirect('/auth/login')


def sign_up(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        User.objects.create_user(username=email, email='', password=password1, name=name)
        return redirect('/auth/login')
    return render(request, 'auth/sign_up.html', {'form': UserCreationForm})


def email_duplicate_check(request):
    username = request.GET['username']
    try:
        User.objects.get(username=username)
        return JsonResponse({'data': False})
    except User.DoesNotExist:
        return JsonResponse({'data': True})
