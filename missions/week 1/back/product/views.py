from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator # 페이징
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Product
from qna.models import Product_qna
from user.models import User

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

    return render(request, 'index.html', context)

# 상세보기
def detailProduct(request, product_id):
    print("@@@@@@@@@@@")
    product = get_object_or_404(Product, pk=product_id)
    qnas = Product_qna.objects.filter(product_id=product_id)
    return render(request, 'detail.html', {'product': product, 'qnas': qnas})

# 질문
# @login_required
def createQna(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        title = request.POST.get('title')
        content = request.POST.get('content')
    conn_user = request.user
    user = User.objects.get(username=conn_user)
    Product_qna.objects.create(product_id=product_id, user_id=user.id,content=content,title=title)

    return HttpResponseRedirect(reverse('detailProduct',args=(product_id,)))

