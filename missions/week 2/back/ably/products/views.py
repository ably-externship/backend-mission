from django.shortcuts import render, redirect
from .models import Product, Question, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    # 페이징
    page = request.GET.get('page', '1')

    products = Product.objects.all().order_by('-created_at')

    paginator = Paginator(products, 2)
    result = paginator.get_page(page)

    context = {
        'products': result,
    }
    return render(request, 'products/index.html', context)


def detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        questions = Question.objects.filter(product=product_id)
        context = {
            'product': product,
            'questions': questions,
        }
        return render(request, 'products/detail.html', context)
    except Product.DoesNotExist:
        return redirect('products:index')


@login_required
def question(request, product_id):
    user = request.user
    content = request.POST['content']
    question = Question(user=user, product_id=product_id, content=content)
    question.save()
    return redirect('products:detail', product_id=product_id)


@login_required
def add(request, product_id):
    user = request.user
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=product_id)

            qs = Basket.objects.filter(user=user, product_id=product_id)

            if not qs.exists():
                new_basket = Basket(user=user, product_id=product_id, count=1)
                new_basket.save()
            else:
                basket: Basket = qs.first()
                basket.count = basket.count + 1
                basket.save()

            return redirect('products:detail', product_id=product.id)

        except Product.DoesNotExist:
            pass
        return redirect('products:index')


@login_required
def basket(request):
    user = request.user
    baskets = Basket.objects.filter(user=user)
    context = {
        'baskets': baskets,
    }
    return render(request, 'products/basket.html', context)


def basket_update(request, id):
    basket = Basket.objects.get(id=id)

    json_data = json.loads(request.body)
    qty = int(json_data.get('count'))

    if qty > 0:
        basket.count = qty
        basket.save()

        return HttpResponse(json.dumps({"result": True, "action": "update", "qty": basket.count}),
                            content_type="application/json")

    return basket_delete(request, id)


def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()

    return HttpResponse(json.dumps({"result": True, "action": "delete"}), content_type="application/json")
