from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product, ProductQuestion, ProductOption


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)
    return render(request, 'markets/index.html', {
        'products': products
    })


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__contains=query)
    return render(request, 'markets/search.html', {
        'query': query,
        'products': products,
    })


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    discounted_rate = round((product.original_price - product.discounted_price) / product.original_price * 100)
    options = ProductOption.objects.filter(product=product)
    return render(request, 'markets/detail.html', {
        'product': product,
        'discounted_rate': discounted_rate,
        'options': options
    })


def question(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    class QuestionForm(forms.ModelForm):
        class Meta:
            model = ProductQuestion
            fields = ['title', 'private', 'question']
            labels = {
                'title': '제목',
                'private': '비밀글',
                'question': '문의 내용'
            }

    return render(request, 'markets/question.html', {
        'product': product,
        'form': QuestionForm()
    })


def question_submit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    title = request.POST['title']
    content = request.POST['question']
    product_question = ProductQuestion(product=product, user=request.user, title=title, question=content)
    product_question.save()
    return render(request, 'markets/question_submit.html', {
        'product': product,
        'question': product_question
    })
