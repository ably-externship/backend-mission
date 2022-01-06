from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'product/product_list.html')

def detail(request, product_id):
    context = {'product': product_id}
    return render(request, 'product/product_detail.html', context)

