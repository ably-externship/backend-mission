from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Question, Answer
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    products = Product.objects.all().order_by('-pub_date')
    paginator = Paginator(products, 4)
    page = int(request.GET.get('page', 1))
    product_list = paginator.get_page(page)
    return render(request, 'home.html', {'product_list':product_list})

def productNew(request):
    return render(request, 'productNew.html')

def productCreate(request):
    new_product = Product()
    new_product.name = request.POST['name']
    new_product.writer = request.user
    new_product.marcket = request.POST['marcket']
    new_product.pub_date = timezone.now()
    new_product.price = request.POST['price']
    new_product.stock = request.POST['stock']
    new_product.description = request.POST['description']
    if request.FILES.get('image'):
        new_product.image = request.FILES.get('image')
    else:
        new_product.image = 0
    
    if request.FILES.get('detailImage'):
        new_product.detailImage = request.FILES['detailImage']
    else:
        new_product.detailImage = 0
    new_product.save()
    return redirect('main:productDetail', new_product.id)

def productDetail(request, id):
    product = get_object_or_404(Product, pk = id)
    all_questions = product.questions.all().order_by('-created')
    all_answers = []
    for question in all_questions:
        all_answers += list(Answer.objects.filter(question = question))
    return render(request, 'productDetail.html', {'product':product, 'questions': all_questions, 'answers':all_answers})

def productEdit(request, id):
    edit_product = Product.objects.get(pk = id)
    return render(request, 'productEdit.html', {'product' : edit_product})

def productUpdate(request, id):
    update_product = Product.objects.get(pk = id)
    update_product.name = request.POST['name']
    update_product.writer = request.user
    update_product.marcket = request.POST['marcket']
    update_product.pub_date = timezone.now()
    update_product.price = request.POST['price']
    update_product.stock = request.POST['stock']
    update_product.description = request.POST['description']
    if request.FILES.get('image'):
        update_product.image = request.FILES.get('image')
    if request.FILES.get('detailImage'):
        update_product.detailImage = request.FILES.get('detailImage')
    update_product.save()
    return redirect('main:productDetail', update_product.id)

def productDelete(request, id):
    delete_product = Product.objects.get(pk = id)
    delete_product.delete()
    return redirect('main:home')

def questionCreate(request, productId):
    new_question = Question()
    new_question.content = request.POST['content']
    new_question.writer = request.user
    new_question.created = timezone.now()
    new_question.product = get_object_or_404(Product, pk = productId)
    new_question.save()
    return redirect('main:productDetail', productId)

def questionEdit(request, productId, questionId):
    product = get_object_or_404(Product, pk = productId)
    edit_question = Question.objects.get(pk = questionId)
    return render(request, 'questionEdit.html', {'product':product, 'question':edit_question})

def questionUpdate(request, productId, questionId):
    update_question = Question.objects.get(pk = questionId)
    update_question.content = request.POST['content']
    update_question.save()
    return redirect('main:productDetail', productId)

def questionDelete(request, productId, questionId):
    delete_question = Question.objects.get(pk = questionId)
    delete_question.delete()
    return redirect('main:productDetail', productId)

def answerCreate(request, productId, questionId):
    new_answer = Answer()
    new_answer.content = request.POST['content']
    new_answer.writer = request.user
    new_answer.created = timezone.now()
    new_answer.question = get_object_or_404(Question, pk = questionId)
    new_answer.save()
    return redirect('main:productDetail', productId)

def search(request):
    products = Product.objects.all().order_by('-pub_date')
    word = request.POST.get('word', "")

    if word:
        products = products.filter(name__icontains=word)
        paginator = Paginator(products, 4)
        page = int(request.GET.get('page', 1))
        product_list = paginator.get_page(page)
        return render(request, 'search.html', {'product_list' : product_list, 'word':word})

    else:
        return render(request, 'search.html')

