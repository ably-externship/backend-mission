from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']

        mall = Malls(
            title=title,
            content=content,
            writer=writer,
        )
        mall.save()
        return redirect('main_page')
    else:
        mallForm = MallsForm
        mall = Malls.objects.all()
        context = {
            'boardForm': mallForm,
            'board': mall,
        }
        return render(request, 'main.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('main_page')
            
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main_page')


def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                uesrname=request.POST["username"], 
                password=request.PPOST["password1"],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return redirect('main_page')
        
        return render(request, 'signup.html')
    return render(request, 'signup.html')

