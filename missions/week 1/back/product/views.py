from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator


@csrf_exempt
def itemIndex(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        posts = paginator.get_page(page)
        serializer = ProductSerializer(posts, many=True)
        return render(request, 'ALLproduct.html', {'product_list': posts})

@csrf_exempt
def allItem(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        posts = paginator.get_page(page)
        serializer = ProductSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def itemSearch(request):
    if request.method == 'POST':
        item_search = request.POST.get('item_search')
        result = Product.objects.filter(product_name__contains=item_search)

        serializer = ProductSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)


