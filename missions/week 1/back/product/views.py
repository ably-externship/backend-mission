from django.shortcuts import render, get_object_or_404
from .models import Product
from qna.models import Product_qna


def index(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request, 'index.html', context)

# 상세보기
def detailProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    qnas = Product_qna.objects.filter(product_id=product_id)
    return render(request, 'detail.html', {'product': product, 'qnas': qnas})
