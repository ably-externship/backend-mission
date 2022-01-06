from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'auth/login.html')

def signUp(request):
    return render(request, 'auth/sign_up.html')