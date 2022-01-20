from django.core import paginator
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from collections import defaultdict


# Create your views here.


def page(request):
    store_list = Store.objects.all()
    # # store_list 페이징 처리
    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(store_list, '3') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장

    # print(page)
    return render(request, 'post_list.html', {'page_obj':page_obj})




def post_RedStore(request):
    redstore_obj = Item.objects.filter(store_id_store='S0001')
    redstore_name=[]
    for name in redstore_obj:
        redstore_name.append(name.name)

    redstore_name=list(set(redstore_name))
    redstore_name.sort()
    # print(page)
    return render(request, 'red_store.html', {'redstore_name':redstore_name})

def post_RedShirt(request):
    items = Item.objects.filter(name='Red Shirt')
    colors=set()
    sizes=[]
    for item in items:
        colors.add(item.color)
        sizes.append(item.size)
    colors = list(colors)
    context = {'colors':colors,'sizes':sizes} 
    return render(request,'red_shirt.html', context)

def post_RedSkirt(request):
    return render(request,'red_skirt.html')

def post_RedDress(request):
    return render(request,'red_dress.html')

# def select(request):


