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



    
    ## 페이징 ##
    # paginate_by = 3
    # context ={}

    # context['is_paginated']=True

    # all_store = Store.objects.all()
    # paginator=Paginator(all_store,paginate_by)
    # page_number_range = 3
    # current_page = int(request.GET.get('page',1))
    # context['current_page'] = current_page

    # start_index = int((current_page-1)/page_number_range)*page_number_range
    # end_index = start_index + page_number_range

    # current_page_group_range = paginator.page_range[start_index:end_index]
    # print('current_page_group_range',current_page_group_range)

    # start_page = paginator.page(current_page_group_range[0])
    # end_page = paginator.page(current_page_group_range[-1])

    # has_previous_page = start_page.has_previous()
    # has_next_page = end_page.has_next()

    # context['current_page_group_range'] = current_page_group_range
    # if has_previous_page:
    #     context['has_previous_page'] = has_previous_page
    #     context['previous_page'] = start_page.previous_page_number

    # if has_next_page:
    #     context['has_next_page'] = has_next_page
    #     context['next_page'] = end_page.next_page_number

    # e = paginate_by * current_page
    # s = e - paginate_by
    # print('내용 Index', s, e)
    # store_list = Store.objects.all()[s:e]

    # ## 쇼핑몰 리스트 (체크박스 용도) ##
    # # context['store_list'] = all_store

    # return render(request, 'post_list.html',context)

def post_redstore(request):
    return render(request,'red_store.html')

def post_redshirt(request):
    items = Item.objects.filter(name='Red Shirt')
    colors=set()
    sizes=[]
    for item in items:
        colors.add(item.color)
        sizes.append(item.size)
    colors = list(colors)
    context = {'colors':colors,'sizes':sizes} 
    return render(request,'red_shirt.html', context)

def post_redskirt(request):
    return render(request,'red_skirt.html')

def post_reddress(request):
    return render(request,'red_dress.html')

# def select(request):


