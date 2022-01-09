from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from product.models import Product, ProductDetail, Board
from user.models import User
from shop.models import Shop
from django.core.paginator import Paginator
# from user.login_check import login_check


def make_page(request, queryset, num):
    paginator = Paginator(queryset, num)
    page = int(request.GET.get('page', 1))
    content_list = paginator.get_page(page)
    return content_list


def main(request):
    try:
        user_id = request.session['user']
        user = User.objects.get(user_id=user_id)
        context = {
            'user': user
        }
    except KeyError:
        context = {}

    product = Product.objects.all()
    context["product_list"] = make_page(request, product, 4)

    return render(request, 'product/main.html', context=context)


def search(request):
    if request.method == "POST":
        classification = request.POST.get('classification')
        search_word = request.POST.get('search_word')
        if classification == 'product':
            search_list = Product.objects.filter(product_name__contains=search_word)

        else:
            search_list = Shop.objects.filter(shop_name__contains=search_word)

        context = {
            'search_list': make_page(request, search_list, 2),
            'classification': classification
        }

        return render(request, 'product/search.html', context=context)


def detail(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(product_id=product_id)
        option_list = ProductDetail.objects.filter(product_id=product_id)
        board = Board.objects.filter(product_id=product_id).order_by('-date')
        context = {
            'product': product,
            'option_list': option_list,
            'board_list': board
        }
    return render(request, 'product/detail.html', context=context)


def write(request, product_id):
    if request.method == "POST" and 'user' in request.session:
        user_id = User.objects.get(user_id=request.session['user'])
        product = Product.objects.get(product_id=product_id)
        title = request.POST['title']
        content = request.POST['content']
        secret = request.POST.get('secret', False)

        posting = Board(title=title,
                        content=content,
                        secret=secret,
                        user_id=user_id,
                        product_id=product,
                        date=timezone.now())

        posting.save()

    elif 'user' not in request.session:
        context = {
            'message': '로그인이 필요한 기능입니다.'
        }
        return render(request, 'user/login.html', context=context)
    else:
        pass

    return HttpResponseRedirect(reverse('product:detail', args=(product_id,)))
