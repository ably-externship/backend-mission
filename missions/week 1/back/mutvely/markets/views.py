from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from markets.models import Outwear, Onepiece, Top, Pants, Skirt, Qna, Cart

def main(request):
    prod_list = Outwear.objects.all()
    values = {
        'cateegory':'all',
        'prod_list':prod_list
    }
    return render(request, 'markets/main.html', values)

def outer(request):
    prod_list = Outwear.objects.all()
    values = {
        'category':'outer',
        'prod_list':prod_list
    }
    return render(request, 'markets/item-lists.html', values)

def top(request):
    prod_list = Top.objects.all()
    values = {
        'category':'top',
        'prod_list':prod_list
    }
    return render(request,'markets/item-lists.html', values)

def onepiece(request):
    prod_list = Onepiece.objects.all()
    values = {
        'category':'onepiece',
        'prod_list':prod_list
    }
    return render(request, 'markets/item-lists.html', values)

def pants(request):
    prod_list = Pants.objects.all()
    values = {
        'category':'pants',
        'prod_list':prod_list
    }
    return render(request, 'markets/item-lists.html', values)

def skirt(request):
    prod_list = Skirt.objects.all()
    values = {
        'category':'skirt',
        'prod_list':prod_list
    }
    return render(request, 'markets/item-lists.html', values)

def search(request, category):
    if request.method == 'POST':
        query = request.POST['query']
        category = request.POST['category']
        if category == 'outer':
            search = Outwear.objects.filter(prodname__contains=query)
        elif category == 'top':
            search = Top.objects.filter(prodname__contains=query)
        elif category == 'onepiece':
            search = Onepiece.objects.filter(prodname__contains=query)
        elif category == 'pants':
            search = Pants.objects.filter(prodname__contains=query)
        elif category == 'skirt':
            search = Skirt.objects.filter(prodname__contains=query)
        return HttpResponse(search)
    return HttpResponse('error')


def detail(request, category, id):
    if category == 'outer':
        detail = Outwear.objects.get(id=id)
    elif category == 'top':
        detail = Top.objects.get(id=id)
    elif category == 'onepiece':
        detail = Onepiece.objects.get(id=id)
    elif category == 'pants':
        detail = Pants.objects.get(id=id)
    elif category == 'skirt':
        detail = Skirt.objects.get(id=id)
    return render(request, 'markets/detail.html', {'category':category,'item':detail})

@login_required
def qna(request, category, id):
    if request.method == 'POST':
        writer = request.POST['writer']
        title = request.POST['title']
        content = request.POST['contents']
        newQna = Qna.objects.create(category=category, prod_id=id, content=content, writer=writer, title=title)
        newQna.save()
        return redirect('main')
    else :
        return render(request, 'markets/qna.html', {'category':category, 'id':id})

@login_required
def addcart (request):
    if request.method == 'POST':
        user = request.user.id
        category = request.POST['category']
        prod_id = request.POST['id']
        newCart = Cart.objects.create(user_id = user, category=category, prod_id= prod_id, prod_num=1)
        newCart.save()
        return HttpResponse('done')
    return HttpResponse('error')

@login_required
def cartCount (request):
    if request.method == 'POST':
        user = request.user.id
        cartItem_id = request.POST['id']
        changeNum = request.POST['changeNum']
        cartItem = Cart.objects.get(id = cartItem_id, user_id = user)
        cartItem.prod_num = changeNum
        cartItem.save()
        return HttpResponse('done')
    return HttpResponse('error')

@login_required
def removeCart (request):
    if request.method == 'POST':
        user = request.user.id
        cart_prod_id = request.POST['id']
        deleteItem = Cart.objects.get(user_id = user, id= cart_prod_id)
        deleteItem.delete()
        return HttpResponse('done')
    return HttpResponse('error')