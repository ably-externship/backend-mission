from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from user.forms import UserForm
from django.contrib.auth import login as auth_login


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # for field in form:
        #     print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserForm()

    return render(request, 'user/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form})
