from django.shortcuts import render, redirect
from .forms import *
from .models import * 
# Create your views here.

def post(request):
    return render(request,'post_list.html')

def post_redstore(request):
    return render(request,'red_store.html')

def post_redshirt(request):
    return render(request,'red_shirt.html')

def post_redskirt(request):
    return render(request,'red_skirt.html')

def post_reddress(request):
    return render(request,'red_dress.html')

