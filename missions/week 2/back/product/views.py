from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator # 페이징
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product
from .models import Product_options
from qna.models import Product_qna
from user.models import Account
from django.contrib.auth.models import User
from cart.forms import AddProductForm



# 상품리스트
def index(request):

    products=Product.objects.all()

    # 검색
    search=request.GET.get('search','')
    if search:
        products=products.filter(name__contains=search)

    # 페이징
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context={'products':products, 'page_obj':page_obj}

    # 카카오톡 토큰
    if request.session.get('access_token'):
        context['check'] = True

    return render(request, 'index.html', context)



# 상세보기
def detailProduct(request, product_id):
    # 카카오톡 토큰
    context={}
    if request.session.get('access_token'):
        context['check'] = True

    product = get_object_or_404(Product, pk=product_id)
    context['product']=product

    option = Product_options.objects.filter(product_id=product_id)
    context['qnas']=option

    qnas = Product_qna.objects.filter(product_id=product_id)
    context['qnas']=qnas

    context['add_to_cart']=AddProductForm(initial={'quantity':1, "opt_size":""})


    return render(request, 'detail.html', context)



# QnA 질문
def createQna(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        title = request.POST.get('title')
        content = request.POST.get('content')
    conn_user = request.user
    # print('1111',conn_user)

    user = Account.objects.get(username=conn_user)
    # print('2222',user)
    Product_qna.objects.create(product_id=product_id, user_id=user.id,content=content,title=title)

    return HttpResponseRedirect(reverse('detailProduct',args=(product_id,)))

