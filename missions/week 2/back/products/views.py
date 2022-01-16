from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from questions.models import Question
from .models import *


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)
    return render(request, 'products/index.html', {
        'products': products
    })


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__contains=query)
    return render(request, 'products/search.html', {
        'query': query,
        'products': products,
    })


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    discounted_rate = round((product.original_price - product.discounted_price) / product.original_price * 100)
    options = ProductOption.objects.filter(product=product)
    questions = Question.objects.filter(content_type=ContentType.objects.get_for_model(product), object_id=product_id)

    class SelectOptionForm(forms.Form):
        option = forms.ModelChoiceField(label='옵션', queryset=options)
        quantity = forms.IntegerField(label='수량', min_value=1, initial=1)

    return render(request, 'products/detail.html', {
        'product': product,
        'discounted_rate': discounted_rate,
        'options': options,
        'questions': questions,
        'form': SelectOptionForm()
    })
