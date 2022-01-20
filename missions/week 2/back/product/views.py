from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from product.models import Product, ProductDetail, Board, Cart
from user.models import User
from shop.models import Shop
from django.core.paginator import Paginator
# from user.login_check import login_check
# django rest api
from rest_framework import viewsets
from .serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




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
    except (KeyError, User.DoesNotExist):
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
            'search_word': search_word,
            'classification': classification
        }

        return render(request, 'product/search.html', context=context)


def detail(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(id=product_id)
        option_list = ProductDetail.objects.filter(product_id=product)
        board = Board.objects.filter(product_id=product).order_by('-date')
        context = {
            'product': product,
            'option_list': option_list,
            'board_list': board
        }
    return render(request, 'product/detail.html', context=context)


def write(request, product_id):
    if request.method == "POST" and 'user' in request.session:
        user_id = User.objects.get(user_id=request.session['user'])
        product = Product.objects.get(id=product_id)
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


# 장바구니
def add_cart(request, product_id):
    print("여기는 됐니?")
    if 'user' in request.session:
        try:
            user = User.objects.get(user_id=request.session['user'])

        except User.DoesNotExist:
            return redirect('product:main')

        option = request.POST.get('option')
        cnt = int(request.POST.get('cnt'))
        product = Product.objects.get(id=product_id)
        product_detail = ProductDetail.objects.get(id=option)
        try:
            item_check = Cart.objects.get(user=user, product=product, option=product_detail)

        except Cart.DoesNotExist:
            add_item = Cart(user=user,
                            product=product,
                            option=product_detail,
                            count=cnt)
            add_item.save()
        else:

            item_check.count += cnt
            item_check.save()

        return redirect('product:cart')

    else:
        context = {
            'message': '로그인이 필요한 기능입니다.'
        }
        return render(request, 'user/login.html', context=context)
    pass


# 총 결제 금액 계산
def price_total(cart_items):
    total = 0
    for item in cart_items:
        total += item.count * item.product.product_price
    return total


def cart(request):
    context = {}
    try:
        user = User.objects.get(user_id=request.session['user'])
        cart_items = Cart.objects.filter(user_id=user)

        if cart_items.count() == 0:
            raise Exception()

        total = price_total(cart_items)
        context['product_list'] = cart_items
        context['total'] = total

    except (Cart.DoesNotExist, Exception):
        context['message'] = "텅!"

    return render(request, 'product/cart.html', context=context)


def detail_change(request, detail_id):
    try:
        if request.method == "POST":
            ch_detail = Cart.objects.get(id=detail_id)

            opt = request.POST.get('option')
            cnt = int(request.POST.get('cnt'))
            # 옵션 선택 했을 경우
            if opt != "default":
                ch_detail.option = ProductDetail.objects.get(id=opt)

            ch_detail.count = cnt
            ch_detail.save()
    except:
        return redirect('product:main')

    return redirect('product:cart')


def item_delete(request, detail_id):
    try:
        item = Cart.objects.get(option=detail_id)
        item.delete()

    except:
        return redirect('product:main')

    return redirect('product:cart')


# 결제
def pay(request):
    pass
