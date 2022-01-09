from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from .forms import *
# Create your views here.


def post_view_detail(request):
    sangpums = Sangpum.objects.first()
    brands = Brand.objects.first()
    return render(request, 'detail.html', {
        'sangpums': sangpums,
        'brands': brands,
    })


def post_view_bottom(request):
    sangpums = Sangpum.objects.filter(obj_code=2)

    paginator = Paginator(sangpums, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'bottom.html', {
        'sangpums': sangpums,
        'posts': posts,
    })


def post_view_top(request):
    sangpums = Sangpum.objects.filter(obj_code=1)

    paginator = Paginator(sangpums, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'top.html', {
        'sangpums': sangpums,
        'posts': posts,

    })


def join(request):
    if request.method == 'POST':
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']
        id_num = request.POST['id_num']
        phone = request.POST['phone']
        email = request.POST['email']

        join = User(
            id=id,
            pw=pw,
            name=name,
            id_num=id_num,
            phone=phone,
            email=email,
        )
        join.save()
        return redirect('join')
    else:
        boardForm = BoardForm
        join = User.objects.all()
        context = {
            'boardForm': boardForm,
            'board': join,
        }
        return render(request, 'join.html', context)


def main(request):
    return render(request, 'main.html')


def search(request):
    return render(request, 'search.html')


def login(request):
    if request.method == "POST":
        id = request.POST['id']
        pw = request.POST['pw']

        user = auth.authenticate(
            request, id=id, pw=pw
        )

        if user is not None:
            auth.login(request, user)
            return redirect('main.html')
        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })
    else:
        return render(request, "login.html")
