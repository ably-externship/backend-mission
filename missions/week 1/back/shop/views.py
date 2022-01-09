from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

# 메인 페이지-------
@login_required(login_url='login')
def shop_main(request, category_slug=None):
    selected_category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    # 카테고리 선택
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)

    # 페이지네이터
    page = request.GET.get('page')
    paginator = Paginator(products, 6)
    page_obj = paginator.get_page(page)

    context = {'selected_category': selected_category,
                'categories': categories, 'products': products,
               'page_obj': page_obj}
    return render(request, 'shop/main.html', context)


# 상품 디테일 페이지-------
@login_required(login_url='login')
def product_detail(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id, slug=product_slug)
    categories = Category.objects.all()
    inventories = Inventory.objects.filter(product=product.id)

    # 상품문의
    if request.method == 'POST':
        question = Question()
        question.comment = request.POST['body']
        question.product = product
        question.user = request.user
        question.save()

    # 상품 문의 페이지네이터
    page = request.GET.get('page')
    questions = Question.objects.filter(product=product.id)
    paginator = Paginator(questions, 3)
    page_obj = paginator.get_page(page)

    context = {'product': product, 'categories': categories,
               'questions': questions, 'inventories': inventories,
               'page_obj': page_obj}
    return render(request, 'shop/detail.html', context)


# 상품 문의 삭제 -------
@login_required(login_url='login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    product = get_object_or_404(Product, pk=question.product.id)

    if request.user != question.user:
        # messages.warning(request, '삭제 권한이 없습니다.')
        return redirect(reverse('shop:product_detail', kwargs={'product_id':product.id, 'product_slug':product.slug}))
    else:
        question.delete()
        return redirect(reverse('shop:product_detail', kwargs={'product_id':product.id, 'product_slug':product.slug}))


# 검색 페이지-------
@login_required(login_url='login')
def search(request):
    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all()
    q = request.POST.get('q', "")
    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__contains=q))
        return render(request, 'shop/search.html', {'products':products, 'q':q, 'categories':categories})
    else:
        return render(request, 'shop/search.html', {'categories':categories})